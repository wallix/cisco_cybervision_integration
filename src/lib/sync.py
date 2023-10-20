from typing import List, Optional as Op, Tuple, Dict

import logging

import re

from datetime import datetime

from dataclasses import dataclass

from generated.cybervision.cybervision_client.schemas import (
    Unset as CybervisionUnset,
)

from generated.cybervision.cybervision_client.models import (
    Tag as CybervisionTag,
    Device as CybervisionDevice,
    NetworkNodes,
    AddExtraFieldBody,
    Preset,
)

from generated.bastion.bastion_client.models import (
    DevicePost,
    DevicePut,
    Tag as BastionTag,
)

from .conf import CONFIG

from . import bastion, cybervision, cybervision_sync

from .util import schema_iter, Exit, APIError

# {category: [(id, name, description), ...]}
Presets = Dict[str, List[Tuple[str, str, str]]]


@dataclass
class Counters:
    created = 0
    updated = 0
    skipped = 0
    errors = 0


class DeviceNotFound(Exception):
    """exception raised when the device to synchronize on the bastion does not exist"""


class Synchronizer:
    def __init__(
        self,
        bastion_client: bastion.Bastion,
        cybervision_client: cybervision.Cybervision,
    ) -> None:
        self.bastion_client = bastion_client

        self.cybervision_client = cybervision_client

        self.cybervision_synchronizer = cybervision_sync.CybervisionSynchronizer(
            bastion_client, cybervision_client
        )

        self.counters = Counters()

    def _get_presets(self) -> Presets:
        presets = cybervision.get_body(
            self.cybervision_client.presets_api.get_preset_list()
        )

        ret: Presets = {}

        for preset in schema_iter(presets):
            catg = preset["category"]["label"]

            if catg not in ret:
                ret[catg] = []

            ret[catg].append(
                (preset["id"], preset["label"], preset.get("description", ""))
            )

        return ret

    UUID_RGX = re.compile(
        r"^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$"
    )

    def _print_table_sep_line(self, cols_size):
        line = ""
        for col in cols_size:
            line += "+" + "-" * col
        print(line + "+")

    def _print_table_line(self, cols, cols_size):
        line = ""
        for i in range(len(cols)):
            size = cols_size[i]
            col = cols[i]
            line += "| "
            if len(col) <= self.MAX_COL_SIZE:
                line += col + " " * (size - len(col) - 1)
            else:
                line += col[: self.MAX_COL_SIZE - 1] + "… "

        print(line + "|")

    MAX_COL_SIZE = 60

    def show_presets(self):
        """print available presets for the user"""
        presets = self._get_presets()

        print(
            "The available presets IDs are shown below.\n"
            + "Please choose the ID of a preset and paste it in the config file (cybervision.preset_id)"
        )

        cols_names = ["ID", "name", "description"]

        for categ, categ_presets in presets.items():
            cols_size = [len(col) for col in cols_names]

            for preset in categ_presets:
                for i in range(3):
                    if len(preset[i]) > cols_size[i]:
                        cols_size[i] = len(preset[i])

            for i in range(3):
                if cols_size[i] > self.MAX_COL_SIZE:
                    cols_size[i] = self.MAX_COL_SIZE
                cols_size[i] += 2

            print()
            print("-- Category: " + categ)

            self._print_table_sep_line(cols_size)
            self._print_table_line(cols_names, cols_size)
            self._print_table_sep_line(cols_size)
            for preset in categ_presets:
                self._print_table_line(preset, cols_size)
            self._print_table_sep_line(cols_size)

    def check_preset(self):
        preset_id = CONFIG.cybervision.preset_id

        if preset_id and self.UUID_RGX.match(preset_id):
            return

        print(
            "Empty or invalid preset ID. A preset is needed to identify the devices to synchronize with the Bastion."
        )

        self.show_presets()

        raise Exit()

    def sync(self):
        """main function"""

        self.check_preset()

        self.cybervision_synchronizer.sync()

        preset_id = CONFIG.cybervision.preset_id

        logging.info("Fetching devices on preset %s...", preset_id)

        try:
            preset_info = cybervision.get_body(
                self.cybervision_client.presets_api.data_info(
                    path_params={"preset_id": preset_id},
                )
            )
        except APIError as exc:
            if exc.status != 404:
                raise
            print("unknown preset ID: " + preset_id)

            self.show_presets()

            raise Exit() from None

        if not preset_info["presetDataAvailable"]:
            raise RuntimeError("preset data not available. Exiting.")

        if preset_info["lastRefresh"]:
            logging.info(
                "Last preset refresh: %s",
                datetime.utcfromtimestamp(
                    float(preset_info["lastRefresh"]) / 1000
                ).strftime("%x %X UTC"),
            )
        else:
            logging.info("Last preset refresh: never")

        i = 0
        cybervision_devices_ids: List[
            Tuple[str, str]
        ] = []  # [(device_id, device_label), ...]
        while True:
            i += 1
            resp = cybervision.get_body(
                self.cybervision_client.devices.get_device_list(
                    path_params={"preset_id": preset_id},
                    query_params={
                        "page": str(i),
                        "size": "100",
                        "fields": "id,isDevice,originalLabel",
                        # "filter": "isDevice:true",  # does not appear to work
                    },
                )
            )

            for node in schema_iter(resp):
                if node["isDevice"]:
                    cybervision_devices_ids.append((node["id"], node["originalLabel"]))

            if len(resp) < 100:
                break

        if len(cybervision_devices_ids) == 0:
            raise RuntimeError("No devices found in preset. Exiting.")

        logging.info(
            "Found %s devices on preset %s. Starting sync",
            len(cybervision_devices_ids),
            preset_id,
        )

        for id, label in cybervision_devices_ids:
            try:
                self.sync_device_with_bastion(id)
            except APIError as exc:
                logging.error(
                    "failed synchronization of Cybervision device (name=%s, id=%s) with the bastion: %s",
                    label,
                    id,
                    exc,
                )
                self.counters.errors += 1

        logging.info(
            "Finished sync. %s bastion devices successfully updated; %s created; %s ignored. %s synchronization errors",
            self.counters.updated,
            self.counters.created,
            self.counters.skipped,
            self.counters.errors,
        )

    def sync_device_with_bastion(self, cybervision_device_id: str):
        """onboard a cybervision device on a bastion or import its properties"""
        cybervision_device = cybervision.get_body(
            self.cybervision_client.devices.get_device_details(
                path_params={"id": cybervision_device_id},
            )
        )

        custom_props = cybervision_device["userProperties"]

        onboarded_id = None

        for prop in schema_iter(custom_props):
            if prop["key"] == self.BASTION_ID_TAG:
                onboarded_id = prop["value"]
            elif prop[
                "key"
            ] == cybervision_sync.CybervisionSynchronizer.BASTION_IGNORE_TAG and prop[
                "value"
            ].lower() in (
                "1",
                "yes",
                "true",
            ):
                self.counters.skipped += 1
                return

        if onboarded_id:
            # already onboarded
            try:
                self.sync_tags(cybervision_device, onboarded_id)
                self.counters.updated += 1
                return
            except DeviceNotFound:
                self.cybervision_synchronizer.clear_device_properties(
                    cybervision_device
                )
                # continue to onboard device if needed

        if CONFIG.bastion.auto_onboard:
            self.onboard_device(cybervision_device)
            self.counters.created += 1
        else:
            logging.info(
                "skipping onboarding of Cybervision device (name=%s, id=%s) (bastion.auto_onboard is false)",
                cybervision_device["label"],
                cybervision_device_id,
            )

    LAST_SYNC_TAG = "cybervision.lastSync"
    CYBERVISION_ID_TAG = "cybervision.id"
    BASTION_ID_TAG = cybervision_sync.CybervisionSynchronizer.BASTION_ID_TAG

    def build_bastion_tags(
        self, cybervision_device: CybervisionDevice
    ) -> List[BastionTag]:
        """build the list of tags to add or update on the bastion"""
        ret = [
            BastionTag(
                key=self.LAST_SYNC_TAG,
                value=datetime.utcnow().strftime("%x %X UTC"),
            ),
            BastionTag(
                key=self.CYBERVISION_ID_TAG,
                value=str(cybervision_device["id"]),
            ),
        ]

        cybervision_tags = cybervision_device["tags"]

        if cybervision_tags:
            for c_tag in schema_iter(cybervision_tags):
                if (
                    not c_tag["category"]
                    or c_tag["category"]["label"] == "Network analysis"  # not relevant
                ):
                    continue

                ret.append(
                    BastionTag(
                        key=f'cybervision.tag:{str(c_tag["category"]["label"])}:{c_tag["label"]}',
                        value="1",
                    )
                )

        ret.extend(self._convert_cybervision_props(cybervision_device))

        return ret

    def sync_tags(self, cybervision_device: CybervisionDevice, bastion_device_id: str):
        """function called when the device already exist on Bastion. Proceeds to updating its tags when needed"""
        new_tags = self.build_bastion_tags(cybervision_device)

        try:
            device = bastion.get_body(
                self.bastion_client.devices.get_device(
                    path_params={"device_id": bastion_device_id},
                    query_params={"fields": "tags,device_name"},
                )
            )
        except APIError as exc:
            if exc.status != 404:
                raise

            raise DeviceNotFound from None

        device_name = device["device_name"]

        # all tags found on the bastion device
        all_tags: Dict[str, BastionTag] = {}

        # tags names that should be deleted
        unknown_cybervision_tags = set()

        for current_tag in schema_iter(device["tags"]):
            all_tags[current_tag["key"]] = BastionTag(
                key=current_tag["key"], value=current_tag["value"]
            )
            if current_tag["key"].startswith("cybervision."):
                unknown_cybervision_tags.add(current_tag["key"])

        for new_tag in new_tags:
            current_tag = all_tags.get(new_tag["key"])

            if current_tag is None:
                all_tags[new_tag["key"]] = new_tag
                logging.info(
                    "bastion: %s: adding tag %s:%s",
                    device_name,
                    new_tag["key"],
                    new_tag["value"],
                )
            else:
                # known tag. update if needed

                unknown_cybervision_tags.remove(new_tag["key"])

                if current_tag["value"] != new_tag["value"]:
                    # we don't log lastSync change, it changes each time
                    if new_tag["key"] != self.LAST_SYNC_TAG:
                        logging.info(
                            "bastion: %s: updating tag %s:%s --> %s",
                            device_name,
                            new_tag["key"],
                            current_tag["value"],
                            new_tag["value"],
                        )
                    # tags cannot be mutated
                    current_tag = BastionTag(key=new_tag["key"], value=new_tag["value"])
                    all_tags[new_tag["key"]] = current_tag

        for tag_key in unknown_cybervision_tags:
            logging.info(
                "bastion: %s: removing tag %s:%s",
                device_name,
                tag_key,
                all_tags[tag_key]["value"],
            )
            del all_tags[tag_key]

        result = list(all_tags.values())

        self.bastion_client.devices.edit_device(
            path_params={"device_id": bastion_device_id},
            query_params={"force": True},
            body=DevicePut(tags=result),
        )

    def find_services_and_ip(
        self, cybervision_device: CybervisionDevice
    ) -> Tuple[List[bastion.Service], Op[str]]:
        """Find services on the cybervision device which are relevant for the Bastion and their corresponding ports.

        Identify the public IP address that is used for these services (the first that comes)
        """
        search_list = {"SSH", "RDP", "TELNET"}

        svcs = []

        device_ip = None

        for component in schema_iter(cybervision_device["components"]):
            flows = None

            for tag in schema_iter(component["flowsTags"]):
                protocol = tag["id"]
                if protocol in search_list:
                    flows = (
                        flows
                        or self.cybervision_client.components.get_component_flow_list(
                            path_params={"id": component["id"]}
                        ).body
                    )  # compute once only if needed

                    if isinstance(flows, CybervisionUnset):
                        continue

                    port = cybervision.find_protocol_port(
                        flows, protocol, component["id"]
                    )

                    if port:
                        svcs.append(bastion.make_service(protocol, port))

                        if not device_ip and cybervision.is_ip_good_candidate(
                            component["ip"]
                        ):
                            device_ip = component["ip"]

                        search_list.remove(protocol)

                        if not search_list:
                            return svcs, device_ip

        return svcs, device_ip

    def onboard_device(self, cybervision_device: CybervisionDevice):
        """create a Bastion device based on the available information on Cybervision"""

        name = re.sub(
            "[" + re.escape(r'\/:*?"<>|@ ') + "]", "_", str(cybervision_device["label"])
        )

        svcs, device_ip = self.find_services_and_ip(cybervision_device)

        if not device_ip:
            device_ip = cybervision.select_ip(cybervision_device["ip"])

            if not device_ip:
                logging.warning(
                    "no ip for device %s %s",
                    cybervision_device["id"],
                    cybervision_device["label"],
                )
                return

        # Add the device

        device_form = DevicePost(
            device_name=name,
            description=f"Imported from CISCO Cybervision device with name={name} and id={cybervision_device['id']}",
            host=device_ip,
            tags=self.build_bastion_tags(cybervision_device),
            services=svcs,
        )
        self.bastion_client.devices.add_device(device_form)

        bastion_get_devices = bastion.get_body(
            self.bastion_client.devices.get_devices(
                query_params={
                    "q": f"device_name={name}",
                    "limit": 1,
                    "fields": "id,ip,services",
                }
            )
        )

        if not bastion_get_devices:
            logging.error(
                "error: device %s (Cybervision id: %s) was created on Bastion but could not be returned",
                name,
                cybervision_device["id"],
            )
            return

        bastion_device = bastion_get_devices[0]

        svc_names = (
            ",".join([svc["service_name"] for svc in svcs]) or "no service found"
        )

        logging.info(
            "added Cybervision device %s to Bastion devices (id: %s) with services: %s",
            cybervision_device["label"],
            bastion_device["id"],
            svc_names,
        )

        # refresh content of cybervision device
        cybervision_device = cybervision.get_body(
            self.cybervision_client.devices.get_device_details(
                path_params={"id": cybervision_device["id"]},
            )
        )

        self.cybervision_synchronizer.import_device_props(
            cybervision_device, bastion_device
        )

    RELEVANT_PROPERTIES = ("serial-number", "model-ref", "vendor-name", "fw-version")

    def _convert_cybervision_props(
        self, cybervision_device: CybervisionDevice
    ) -> List[BastionTag]:
        ret = []
        for prop in schema_iter(cybervision_device["normalizedProperties"]):
            if prop["key"] in self.RELEVANT_PROPERTIES:
                ret.append(
                    BastionTag(
                        key="cybervision." + prop["key"],
                        value=str(",".join(prop["value"])),
                    )
                )
        return ret
