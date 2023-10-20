# coding: utf-8

"""
    Cisco Cyber Vision center v3 API.

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.1
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from cybervision_client import schemas  # noqa: F401


class DeviceRiskScoreStruct(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def activitiesRisk() -> typing.Type['ActivitiesRiskStruct']:
                return ActivitiesRiskStruct
            deviceEngineLastRun = schemas.Int64Schema
        
            @staticmethod
            def deviceTypeRisk() -> typing.Type['DeviceTypeRiskStruct']:
                return DeviceTypeRiskStruct
        
            @staticmethod
            def groupRisk() -> typing.Type['GroupRiskStruct']:
                return GroupRiskStruct
        
            @staticmethod
            def vulnerabilitiesRisk() -> typing.Type['VulnerabilitiesRiskStruct']:
                return VulnerabilitiesRiskStruct
            __annotations__ = {
                "activitiesRisk": activitiesRisk,
                "deviceEngineLastRun": deviceEngineLastRun,
                "deviceTypeRisk": deviceTypeRisk,
                "groupRisk": groupRisk,
                "vulnerabilitiesRisk": vulnerabilitiesRisk,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["activitiesRisk"]) -> 'ActivitiesRiskStruct': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["deviceEngineLastRun"]) -> MetaOapg.properties.deviceEngineLastRun: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["deviceTypeRisk"]) -> 'DeviceTypeRiskStruct': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["groupRisk"]) -> 'GroupRiskStruct': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["vulnerabilitiesRisk"]) -> 'VulnerabilitiesRiskStruct': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["activitiesRisk", "deviceEngineLastRun", "deviceTypeRisk", "groupRisk", "vulnerabilitiesRisk", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["activitiesRisk"]) -> typing.Union['ActivitiesRiskStruct', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["deviceEngineLastRun"]) -> typing.Union[MetaOapg.properties.deviceEngineLastRun, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["deviceTypeRisk"]) -> typing.Union['DeviceTypeRiskStruct', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["groupRisk"]) -> typing.Union['GroupRiskStruct', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["vulnerabilitiesRisk"]) -> typing.Union['VulnerabilitiesRiskStruct', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["activitiesRisk", "deviceEngineLastRun", "deviceTypeRisk", "groupRisk", "vulnerabilitiesRisk", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        activitiesRisk: typing.Union['ActivitiesRiskStruct', schemas.Unset] = schemas.unset,
        deviceEngineLastRun: typing.Union[MetaOapg.properties.deviceEngineLastRun, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        deviceTypeRisk: typing.Union['DeviceTypeRiskStruct', schemas.Unset] = schemas.unset,
        groupRisk: typing.Union['GroupRiskStruct', schemas.Unset] = schemas.unset,
        vulnerabilitiesRisk: typing.Union['VulnerabilitiesRiskStruct', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'DeviceRiskScoreStruct':
        return super().__new__(
            cls,
            *_args,
            activitiesRisk=activitiesRisk,
            deviceEngineLastRun=deviceEngineLastRun,
            deviceTypeRisk=deviceTypeRisk,
            groupRisk=groupRisk,
            vulnerabilitiesRisk=vulnerabilitiesRisk,
            _configuration=_configuration,
            **kwargs,
        )

from cybervision_client.model.activities_risk_struct import ActivitiesRiskStruct
from cybervision_client.model.device_type_risk_struct import DeviceTypeRiskStruct
from cybervision_client.model.group_risk_struct import GroupRiskStruct
from cybervision_client.model.vulnerabilities_risk_struct import VulnerabilitiesRiskStruct
