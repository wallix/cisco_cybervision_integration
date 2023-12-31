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


class Sensor(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Sensor json representation
when fetched in a Preset
    """


    class MetaOapg:
        
        class properties:
            captureMode = schemas.StrSchema
            centerId = schemas.StrSchema
            id = schemas.StrSchema
            ip = schemas.StrSchema
            label = schemas.StrSchema
            serialNumber = schemas.StrSchema
            __annotations__ = {
                "captureMode": captureMode,
                "centerId": centerId,
                "id": id,
                "ip": ip,
                "label": label,
                "serialNumber": serialNumber,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["captureMode"]) -> MetaOapg.properties.captureMode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["centerId"]) -> MetaOapg.properties.centerId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ip"]) -> MetaOapg.properties.ip: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["label"]) -> MetaOapg.properties.label: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["serialNumber"]) -> MetaOapg.properties.serialNumber: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["captureMode", "centerId", "id", "ip", "label", "serialNumber", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["captureMode"]) -> typing.Union[MetaOapg.properties.captureMode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["centerId"]) -> typing.Union[MetaOapg.properties.centerId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ip"]) -> typing.Union[MetaOapg.properties.ip, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["label"]) -> typing.Union[MetaOapg.properties.label, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["serialNumber"]) -> typing.Union[MetaOapg.properties.serialNumber, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["captureMode", "centerId", "id", "ip", "label", "serialNumber", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        captureMode: typing.Union[MetaOapg.properties.captureMode, str, schemas.Unset] = schemas.unset,
        centerId: typing.Union[MetaOapg.properties.centerId, str, schemas.Unset] = schemas.unset,
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        ip: typing.Union[MetaOapg.properties.ip, str, schemas.Unset] = schemas.unset,
        label: typing.Union[MetaOapg.properties.label, str, schemas.Unset] = schemas.unset,
        serialNumber: typing.Union[MetaOapg.properties.serialNumber, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Sensor':
        return super().__new__(
            cls,
            *_args,
            captureMode=captureMode,
            centerId=centerId,
            id=id,
            ip=ip,
            label=label,
            serialNumber=serialNumber,
            _configuration=_configuration,
            **kwargs,
        )
