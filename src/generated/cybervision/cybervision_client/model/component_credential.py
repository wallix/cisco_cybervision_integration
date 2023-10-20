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


class ComponentCredential(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            algo = schemas.StrSchema
            componentId = schemas.StrSchema
            creationTime = schemas.Int64Schema
            lastUpdate = schemas.Int64Schema
            password = schemas.StrSchema
            protocol = schemas.StrSchema
            username = schemas.StrSchema
            __annotations__ = {
                "algo": algo,
                "componentId": componentId,
                "creationTime": creationTime,
                "lastUpdate": lastUpdate,
                "password": password,
                "protocol": protocol,
                "username": username,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["algo"]) -> MetaOapg.properties.algo: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["componentId"]) -> MetaOapg.properties.componentId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["creationTime"]) -> MetaOapg.properties.creationTime: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lastUpdate"]) -> MetaOapg.properties.lastUpdate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["password"]) -> MetaOapg.properties.password: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["protocol"]) -> MetaOapg.properties.protocol: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["username"]) -> MetaOapg.properties.username: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["algo", "componentId", "creationTime", "lastUpdate", "password", "protocol", "username", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["algo"]) -> typing.Union[MetaOapg.properties.algo, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["componentId"]) -> typing.Union[MetaOapg.properties.componentId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["creationTime"]) -> typing.Union[MetaOapg.properties.creationTime, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lastUpdate"]) -> typing.Union[MetaOapg.properties.lastUpdate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["password"]) -> typing.Union[MetaOapg.properties.password, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["protocol"]) -> typing.Union[MetaOapg.properties.protocol, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["username"]) -> typing.Union[MetaOapg.properties.username, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["algo", "componentId", "creationTime", "lastUpdate", "password", "protocol", "username", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        algo: typing.Union[MetaOapg.properties.algo, str, schemas.Unset] = schemas.unset,
        componentId: typing.Union[MetaOapg.properties.componentId, str, schemas.Unset] = schemas.unset,
        creationTime: typing.Union[MetaOapg.properties.creationTime, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        lastUpdate: typing.Union[MetaOapg.properties.lastUpdate, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        password: typing.Union[MetaOapg.properties.password, str, schemas.Unset] = schemas.unset,
        protocol: typing.Union[MetaOapg.properties.protocol, str, schemas.Unset] = schemas.unset,
        username: typing.Union[MetaOapg.properties.username, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ComponentCredential':
        return super().__new__(
            cls,
            *_args,
            algo=algo,
            componentId=componentId,
            creationTime=creationTime,
            lastUpdate=lastUpdate,
            password=password,
            protocol=protocol,
            username=username,
            _configuration=_configuration,
            **kwargs,
        )
