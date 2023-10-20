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


class DefaultSeverities(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            severityAckDifference = schemas.Int32Schema
            severityDeleteElement = schemas.Int32Schema
            severityDifferenceDetected = schemas.Int32Schema
            severityIgnoreDifference = schemas.Int32Schema
            severityNackDifference = schemas.Int32Schema
            __annotations__ = {
                "severityAckDifference": severityAckDifference,
                "severityDeleteElement": severityDeleteElement,
                "severityDifferenceDetected": severityDifferenceDetected,
                "severityIgnoreDifference": severityIgnoreDifference,
                "severityNackDifference": severityNackDifference,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["severityAckDifference"]) -> MetaOapg.properties.severityAckDifference: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["severityDeleteElement"]) -> MetaOapg.properties.severityDeleteElement: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["severityDifferenceDetected"]) -> MetaOapg.properties.severityDifferenceDetected: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["severityIgnoreDifference"]) -> MetaOapg.properties.severityIgnoreDifference: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["severityNackDifference"]) -> MetaOapg.properties.severityNackDifference: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["severityAckDifference", "severityDeleteElement", "severityDifferenceDetected", "severityIgnoreDifference", "severityNackDifference", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["severityAckDifference"]) -> typing.Union[MetaOapg.properties.severityAckDifference, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["severityDeleteElement"]) -> typing.Union[MetaOapg.properties.severityDeleteElement, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["severityDifferenceDetected"]) -> typing.Union[MetaOapg.properties.severityDifferenceDetected, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["severityIgnoreDifference"]) -> typing.Union[MetaOapg.properties.severityIgnoreDifference, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["severityNackDifference"]) -> typing.Union[MetaOapg.properties.severityNackDifference, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["severityAckDifference", "severityDeleteElement", "severityDifferenceDetected", "severityIgnoreDifference", "severityNackDifference", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        severityAckDifference: typing.Union[MetaOapg.properties.severityAckDifference, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        severityDeleteElement: typing.Union[MetaOapg.properties.severityDeleteElement, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        severityDifferenceDetected: typing.Union[MetaOapg.properties.severityDifferenceDetected, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        severityIgnoreDifference: typing.Union[MetaOapg.properties.severityIgnoreDifference, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        severityNackDifference: typing.Union[MetaOapg.properties.severityNackDifference, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'DefaultSeverities':
        return super().__new__(
            cls,
            *_args,
            severityAckDifference=severityAckDifference,
            severityDeleteElement=severityDeleteElement,
            severityDifferenceDetected=severityDifferenceDetected,
            severityIgnoreDifference=severityIgnoreDifference,
            severityNackDifference=severityNackDifference,
            _configuration=_configuration,
            **kwargs,
        )