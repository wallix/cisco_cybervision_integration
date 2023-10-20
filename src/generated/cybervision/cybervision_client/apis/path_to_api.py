import typing_extensions

from cybervision_client.paths import PathValues
from cybervision_client.apis.paths.components import Components
from cybervision_client.apis.paths.components_id import ComponentsId
from cybervision_client.apis.paths.components_id_credentials import ComponentsIdCredentials
from cybervision_client.apis.paths.components_id_flows import ComponentsIdFlows
from cybervision_client.apis.paths.components_id_flows_tags import ComponentsIdFlowsTags
from cybervision_client.apis.paths.components_id_variables import ComponentsIdVariables
from cybervision_client.apis.paths.components_id_vulnerabilities import ComponentsIdVulnerabilities
from cybervision_client.apis.paths.devices import Devices
from cybervision_client.apis.paths.devices_id import DevicesId
from cybervision_client.apis.paths.devices_id_activities import DevicesIdActivities
from cybervision_client.apis.paths.devices_id_activities_tags import DevicesIdActivitiesTags
from cybervision_client.apis.paths.devices_id_credentials import DevicesIdCredentials
from cybervision_client.apis.paths.devices_id_risk_score import DevicesIdRiskScore
from cybervision_client.apis.paths.devices_id_variables import DevicesIdVariables
from cybervision_client.apis.paths.devices_id_vulnerabilities import DevicesIdVulnerabilities
from cybervision_client.apis.paths.homepage_presets_highlights import HomepagePresetsHighlights
from cybervision_client.apis.paths.presets import Presets
from cybervision_client.apis.paths.presets_preset_id import PresetsPresetId
from cybervision_client.apis.paths.presets_preset_id_data_info import PresetsPresetIdDataInfo
from cybervision_client.apis.paths.presets_preset_id_settings import PresetsPresetIdSettings
from cybervision_client.apis.paths.presets_preset_id_visualisations_component_list import PresetsPresetIdVisualisationsComponentList
from cybervision_client.apis.paths.presets_preset_id_visualisations_networknode_list import PresetsPresetIdVisualisationsNetworknodeList
from cybervision_client.apis.paths.object_id_label import ObjectIdLabel
from cybervision_client.apis.paths.object_id_users_properties import ObjectIdUsersProperties
from cybervision_client.apis.paths.object_id_users_properties_property_id import ObjectIdUsersPropertiesPropertyId

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.COMPONENTS: Components,
        PathValues.COMPONENTS_ID: ComponentsId,
        PathValues.COMPONENTS_ID_CREDENTIALS: ComponentsIdCredentials,
        PathValues.COMPONENTS_ID_FLOWS: ComponentsIdFlows,
        PathValues.COMPONENTS_ID_FLOWS_TAGS: ComponentsIdFlowsTags,
        PathValues.COMPONENTS_ID_VARIABLES: ComponentsIdVariables,
        PathValues.COMPONENTS_ID_VULNERABILITIES: ComponentsIdVulnerabilities,
        PathValues.DEVICES: Devices,
        PathValues.DEVICES_ID: DevicesId,
        PathValues.DEVICES_ID_ACTIVITIES: DevicesIdActivities,
        PathValues.DEVICES_ID_ACTIVITIES_TAGS: DevicesIdActivitiesTags,
        PathValues.DEVICES_ID_CREDENTIALS: DevicesIdCredentials,
        PathValues.DEVICES_ID_RISK_SCORE: DevicesIdRiskScore,
        PathValues.DEVICES_ID_VARIABLES: DevicesIdVariables,
        PathValues.DEVICES_ID_VULNERABILITIES: DevicesIdVulnerabilities,
        PathValues.HOMEPAGE_PRESETSHIGHLIGHTS: HomepagePresetsHighlights,
        PathValues.PRESETS: Presets,
        PathValues.PRESETS_PRESET_ID: PresetsPresetId,
        PathValues.PRESETS_PRESET_ID_DATA_INFO: PresetsPresetIdDataInfo,
        PathValues.PRESETS_PRESET_ID_SETTINGS: PresetsPresetIdSettings,
        PathValues.PRESETS_PRESET_ID_VISUALISATIONS_COMPONENTLIST: PresetsPresetIdVisualisationsComponentList,
        PathValues.PRESETS_PRESET_ID_VISUALISATIONS_NETWORKNODELIST: PresetsPresetIdVisualisationsNetworknodeList,
        PathValues.OBJECT_ID_LABEL: ObjectIdLabel,
        PathValues.OBJECT_ID_USERS_PROPERTIES: ObjectIdUsersProperties,
        PathValues.OBJECT_ID_USERS_PROPERTIES_PROPERTY_ID: ObjectIdUsersPropertiesPropertyId,
    }
)

path_to_api = PathToApi(
    {
        PathValues.COMPONENTS: Components,
        PathValues.COMPONENTS_ID: ComponentsId,
        PathValues.COMPONENTS_ID_CREDENTIALS: ComponentsIdCredentials,
        PathValues.COMPONENTS_ID_FLOWS: ComponentsIdFlows,
        PathValues.COMPONENTS_ID_FLOWS_TAGS: ComponentsIdFlowsTags,
        PathValues.COMPONENTS_ID_VARIABLES: ComponentsIdVariables,
        PathValues.COMPONENTS_ID_VULNERABILITIES: ComponentsIdVulnerabilities,
        PathValues.DEVICES: Devices,
        PathValues.DEVICES_ID: DevicesId,
        PathValues.DEVICES_ID_ACTIVITIES: DevicesIdActivities,
        PathValues.DEVICES_ID_ACTIVITIES_TAGS: DevicesIdActivitiesTags,
        PathValues.DEVICES_ID_CREDENTIALS: DevicesIdCredentials,
        PathValues.DEVICES_ID_RISK_SCORE: DevicesIdRiskScore,
        PathValues.DEVICES_ID_VARIABLES: DevicesIdVariables,
        PathValues.DEVICES_ID_VULNERABILITIES: DevicesIdVulnerabilities,
        PathValues.HOMEPAGE_PRESETSHIGHLIGHTS: HomepagePresetsHighlights,
        PathValues.PRESETS: Presets,
        PathValues.PRESETS_PRESET_ID: PresetsPresetId,
        PathValues.PRESETS_PRESET_ID_DATA_INFO: PresetsPresetIdDataInfo,
        PathValues.PRESETS_PRESET_ID_SETTINGS: PresetsPresetIdSettings,
        PathValues.PRESETS_PRESET_ID_VISUALISATIONS_COMPONENTLIST: PresetsPresetIdVisualisationsComponentList,
        PathValues.PRESETS_PRESET_ID_VISUALISATIONS_NETWORKNODELIST: PresetsPresetIdVisualisationsNetworknodeList,
        PathValues.OBJECT_ID_LABEL: ObjectIdLabel,
        PathValues.OBJECT_ID_USERS_PROPERTIES: ObjectIdUsersProperties,
        PathValues.OBJECT_ID_USERS_PROPERTIES_PROPERTY_ID: ObjectIdUsersPropertiesPropertyId,
    }
)
