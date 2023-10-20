# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from bastion_client.paths.devices_device_id import Api

from bastion_client.paths import PathValues

path = PathValues.DEVICES_DEVICE_ID