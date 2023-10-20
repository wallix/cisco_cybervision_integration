# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from cybervision_client.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    COMPONENTS = "/components"
    COMPONENTS_ID = "/components/{id}"
    COMPONENTS_ID_CREDENTIALS = "/components/{id}/credentials"
    COMPONENTS_ID_FLOWS = "/components/{id}/flows"
    COMPONENTS_ID_FLOWS_TAGS = "/components/{id}/flows/tags"
    COMPONENTS_ID_VARIABLES = "/components/{id}/variables"
    COMPONENTS_ID_VULNERABILITIES = "/components/{id}/vulnerabilities"
    DEVICES = "/devices"
    DEVICES_ID = "/devices/{id}"
    DEVICES_ID_ACTIVITIES = "/devices/{id}/activities"
    DEVICES_ID_ACTIVITIES_TAGS = "/devices/{id}/activities/tags"
    DEVICES_ID_CREDENTIALS = "/devices/{id}/credentials"
    DEVICES_ID_RISK_SCORE = "/devices/{id}/riskScore"
    DEVICES_ID_VARIABLES = "/devices/{id}/variables"
    DEVICES_ID_VULNERABILITIES = "/devices/{id}/vulnerabilities"
    HOMEPAGE_PRESETSHIGHLIGHTS = "/homepage/presets-highlights"
    PRESETS = "/presets"
    PRESETS_PRESET_ID = "/presets/{preset_id}"
    PRESETS_PRESET_ID_DATA_INFO = "/presets/{preset_id}/dataInfo"
    PRESETS_PRESET_ID_SETTINGS = "/presets/{preset_id}/settings"
    PRESETS_PRESET_ID_VISUALISATIONS_COMPONENTLIST = "/presets/{preset_id}/visualisations/component-list"
    PRESETS_PRESET_ID_VISUALISATIONS_NETWORKNODELIST = "/presets/{preset_id}/visualisations/networknode-list"
    OBJECT_ID_LABEL = "/{object}/{id}/label"
    OBJECT_ID_USERS_PROPERTIES = "/{object}/{id}/usersProperties"
    OBJECT_ID_USERS_PROPERTIES_PROPERTY_ID = "/{object}/{id}/usersProperties/{propertyId}"
