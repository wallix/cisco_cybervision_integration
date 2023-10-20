from typing import Iterable, Optional as Opt, List, Tuple

import logging

from datetime import datetime

from generated.cybervision.cybervision_client.schemas import (
    Unset as CybervisionUnset,
)

from generated.cybervision.cybervision_client.models import (
    AddExtraFieldBody,
    UpdateExtraFieldBody,
    Device as CybervisionDevice,
)

from . import cybervision, bastion

from .util import schema_iter

from .conf import CONFIG

from generated.bastion.bastion_client.models import DeviceGet


class CybervisionSynchronizer:
    LAST_SYNC_TAG = "bastion.lastSync"
    BASTION_ID_TAG = "bastion.id"
    BASTION_LINK_TAG = "bastion.link"
    BASTION_IGNORE_TAG = "bastion.ignore"

    def __init__(
        self,
        bastion_client: bastion.Bastion,
        cybervision_client: cybervision.Cybervision,
    ) -> None:
        self.bastion_client = bastion_client

        self.cybervision_client = cybervision_client

        self.bastion_devices_by_host: dict[str, DeviceGet] = {}

        self.bastion_devices_by_id: dict[str, DeviceGet] = {}

    def sync(self) -> None:
        logging.info("Importing Bastion devices information into Cybervision...")

        bastion_devices = bastion.get_body(
            self.bastion_client.devices.get_devices(
                query_params={"fields": "id,host,device_name,services"}
            )
        )

        self.bastion_devices_by_host = {
            str(device["host"]): device for device in schema_iter(bastion_devices)
        }

        self.bastion_devices_by_id = {
            str(device["id"]): device for device in schema_iter(bastion_devices)
        }

        i = 0

        cybervision_bastion_pairs: List[Tuple[CybervisionDevice, DeviceGet]] = []

        while True:
            i += 1
            devices = cybervision.get_body(
                self.cybervision_client.devices.get_all(
                    query_params={"page": i, "size": 100}
                )
            )

            for cybervision_device in schema_iter(devices):
                bastion_device = self._find_bastion_device(cybervision_device)
                if bastion_device:
                    cybervision_bastion_pairs.append(
                        (cybervision_device, bastion_device)
                    )

            if len(devices) < 100:
                break

        for cybervision_device, bastion_device in cybervision_bastion_pairs:
            try:
                self.import_device_props(cybervision_device, bastion_device)
            except Exception as exc:
                logging.error(
                    "failed to update properties on Cybervision device %s: %s",
                    cybervision_device["id"],
                    exc,
                )

    def _find_bastion_device(
        self, cybervision_device: CybervisionDevice
    ) -> Opt[DeviceGet]:
        for prop in schema_iter(cybervision_device["userProperties"]):
            if str(prop["key"]) == self.BASTION_ID_TAG:
                return self.bastion_devices_by_id.get(prop["value"])

        if not cybervision_device["ip"]:
            return None

        for ip in schema_iter(cybervision_device["ip"]):
            if ip in self.bastion_devices_by_host:
                return self.bastion_devices_by_host[ip]

        return None

    def import_device_props(
        self, cybervision_device: CybervisionDevice, bastion_device: DeviceGet
    ) -> None:
        services: Iterable[bastion.Service] = bastion_device["services"]
        self.apply_device_property(
            cybervision_device, self.BASTION_ID_TAG, bastion_device["id"]
        )
        self.apply_device_property(
            cybervision_device,
            self.BASTION_LINK_TAG,
            f"https://{CONFIG.bastion.host}/ui/targets/devices/edit/{bastion_device['id']}/general",
        )

        for service in schema_iter(services):
            name = str(service["service_name"]).lower()

            port = str(service["port"])

            label = f"bastion.service.{name}"

            try:
                self.apply_device_property(cybervision_device, label, port)
            except Exception as exc:
                logging.error(
                    "failed to add property %s to Cybervision device %s: %s",
                    label,
                    cybervision_device["id"],
                    exc,
                )

        self.apply_device_property(
            cybervision_device,
            self.LAST_SYNC_TAG,
            datetime.utcnow().strftime("%x %X UTC"),
        )

    def apply_device_property(
        self, cybervision_device: CybervisionDevice, key: str, value: str
    ) -> None:
        current_prop = cybervision.find_prop(cybervision_device["userProperties"], key)
        if current_prop and current_prop["value"] == value:
            return

        logging.debug(
            "upating property %s:%s on device %s. current: %s",
            key,
            value,
            cybervision_device["label"],
            current_prop,
        )

        if current_prop:
            self.cybervision_client.user_props.put_extra_field(
                path_params={
                    "id": cybervision_device["id"],
                    "object": "devices",
                    "propertyId": current_prop["id"],
                },
                body=UpdateExtraFieldBody(label=key, value=value),
            )
            logging.debug(
                "updated property %s:%s of device %s",
                key,
                value,
                cybervision_device["label"],
            )
            return

        self.cybervision_client.user_props.post_extra_field(
            path_params={
                "id": cybervision_device["id"],
                "object": "devices",
            },
            body=AddExtraFieldBody(label=key, value=value),
        )
        logging.debug(
            "added property %s:%s to device %s", key, value, cybervision_device["label"]
        )

    def clear_device_properties(self, cybervision_device: CybervisionDevice):
        device_props = cybervision_device["userProperties"]

        if not device_props:
            return None

        for prop in schema_iter(device_props):
            key = str(prop["key"])
            if key.startswith("bastion.") and key not in (
                self.LAST_SYNC_TAG,
                self.BASTION_IGNORE_TAG,
            ):
                self.remove_device_property(cybervision_device, key)

    def remove_device_property(self, cybervision_device: CybervisionDevice, key: str):
        current_prop = cybervision.find_prop(cybervision_device["userProperties"], key)
        if not current_prop:
            return

        self.cybervision_client.user_props.delete_extra_field(
            path_params={
                "id": cybervision_device["id"],
                "object": "devices",
                "propertyId": current_prop["id"],
            },
        )
        logging.debug(
            "removed property %s:%s from device %s",
            key,
            current_prop["value"],
            cybervision_device["label"],
        )
