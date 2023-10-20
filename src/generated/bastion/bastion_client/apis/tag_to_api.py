import typing_extensions

from bastion_client.apis.tags import TagValues
from bastion_client.apis.tags.devices_api import DevicesApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.DEVICES: DevicesApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.DEVICES: DevicesApi,
    }
)
