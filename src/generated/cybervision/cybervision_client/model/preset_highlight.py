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


class PresetHighlight(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            devices = schemas.Int64Schema
            events = schemas.Int64Schema
            id = schemas.StrSchema
            label = schemas.StrSchema
            lastRefresh = schemas.Int64Schema
            orphans = schemas.Int64Schema
            riskScore = schemas.Float64Schema
            vulnerabilities = schemas.Int64Schema
            __annotations__ = {
                "devices": devices,
                "events": events,
                "id": id,
                "label": label,
                "lastRefresh": lastRefresh,
                "orphans": orphans,
                "riskScore": riskScore,
                "vulnerabilities": vulnerabilities,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["devices"]) -> MetaOapg.properties.devices: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["events"]) -> MetaOapg.properties.events: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["label"]) -> MetaOapg.properties.label: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lastRefresh"]) -> MetaOapg.properties.lastRefresh: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["orphans"]) -> MetaOapg.properties.orphans: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["riskScore"]) -> MetaOapg.properties.riskScore: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["vulnerabilities"]) -> MetaOapg.properties.vulnerabilities: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["devices", "events", "id", "label", "lastRefresh", "orphans", "riskScore", "vulnerabilities", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["devices"]) -> typing.Union[MetaOapg.properties.devices, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["events"]) -> typing.Union[MetaOapg.properties.events, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["label"]) -> typing.Union[MetaOapg.properties.label, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lastRefresh"]) -> typing.Union[MetaOapg.properties.lastRefresh, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["orphans"]) -> typing.Union[MetaOapg.properties.orphans, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["riskScore"]) -> typing.Union[MetaOapg.properties.riskScore, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["vulnerabilities"]) -> typing.Union[MetaOapg.properties.vulnerabilities, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["devices", "events", "id", "label", "lastRefresh", "orphans", "riskScore", "vulnerabilities", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        devices: typing.Union[MetaOapg.properties.devices, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        events: typing.Union[MetaOapg.properties.events, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        label: typing.Union[MetaOapg.properties.label, str, schemas.Unset] = schemas.unset,
        lastRefresh: typing.Union[MetaOapg.properties.lastRefresh, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        orphans: typing.Union[MetaOapg.properties.orphans, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        riskScore: typing.Union[MetaOapg.properties.riskScore, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        vulnerabilities: typing.Union[MetaOapg.properties.vulnerabilities, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PresetHighlight':
        return super().__new__(
            cls,
            *_args,
            devices=devices,
            events=events,
            id=id,
            label=label,
            lastRefresh=lastRefresh,
            orphans=orphans,
            riskScore=riskScore,
            vulnerabilities=vulnerabilities,
            _configuration=_configuration,
            **kwargs,
        )
