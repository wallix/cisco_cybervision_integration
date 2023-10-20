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


class SimpleResponse(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            Msg = schemas.StrSchema
            Status = schemas.Int64Schema
            __annotations__ = {
                "Msg": Msg,
                "Status": Status,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Msg"]) -> MetaOapg.properties.Msg: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Status"]) -> MetaOapg.properties.Status: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["Msg", "Status", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Msg"]) -> typing.Union[MetaOapg.properties.Msg, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Status"]) -> typing.Union[MetaOapg.properties.Status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["Msg", "Status", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        Msg: typing.Union[MetaOapg.properties.Msg, str, schemas.Unset] = schemas.unset,
        Status: typing.Union[MetaOapg.properties.Status, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SimpleResponse':
        return super().__new__(
            cls,
            *_args,
            Msg=Msg,
            Status=Status,
            _configuration=_configuration,
            **kwargs,
        )
