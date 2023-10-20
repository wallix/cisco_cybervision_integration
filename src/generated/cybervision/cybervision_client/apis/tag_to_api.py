import typing_extensions

from cybervision_client.apis.tags import TagValues
from cybervision_client.apis.tags.components_api import ComponentsApi
from cybervision_client.apis.tags.custom_properties_api import CustomPropertiesApi
from cybervision_client.apis.tags.devices_api import DevicesApi
from cybervision_client.apis.tags.presets_api import PresetsApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.COMPONENTS: ComponentsApi,
        TagValues.CUSTOM_PROPERTIES: CustomPropertiesApi,
        TagValues.DEVICES: DevicesApi,
        TagValues.PRESETS: PresetsApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.COMPONENTS: ComponentsApi,
        TagValues.CUSTOM_PROPERTIES: CustomPropertiesApi,
        TagValues.DEVICES: DevicesApi,
        TagValues.PRESETS: PresetsApi,
    }
)
