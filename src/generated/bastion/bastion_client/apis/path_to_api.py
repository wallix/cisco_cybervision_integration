import typing_extensions

from bastion_client.paths import PathValues
from bastion_client.apis.paths.devices import Devices
from bastion_client.apis.paths.devices_device_id import DevicesDeviceId

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.DEVICES: Devices,
        PathValues.DEVICES_DEVICE_ID: DevicesDeviceId,
    }
)

path_to_api = PathToApi(
    {
        PathValues.DEVICES: Devices,
        PathValues.DEVICES_DEVICE_ID: DevicesDeviceId,
    }
)
