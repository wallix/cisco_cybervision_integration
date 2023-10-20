# coding: utf-8

"""
    WALLIX Bastion Rest API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 3.12
    Contact: support@wallix.com
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

from bastion_client import schemas  # noqa: F401


class AdUserAuthentication(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Active Directory authentication object.
    """


    class MetaOapg:
        
        class properties:
            auth_id = schemas.StrSchema
            auth_name = schemas.StrSchema
            __annotations__ = {
                "auth_id": auth_id,
                "auth_name": auth_name,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["auth_id"]) -> MetaOapg.properties.auth_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["auth_name"]) -> MetaOapg.properties.auth_name: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["auth_id", "auth_name", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["auth_id"]) -> typing.Union[MetaOapg.properties.auth_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["auth_name"]) -> typing.Union[MetaOapg.properties.auth_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["auth_id", "auth_name", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        auth_id: typing.Union[MetaOapg.properties.auth_id, str, schemas.Unset] = schemas.unset,
        auth_name: typing.Union[MetaOapg.properties.auth_name, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AdUserAuthentication':
        return super().__new__(
            cls,
            *_args,
            auth_id=auth_id,
            auth_name=auth_name,
            _configuration=_configuration,
            **kwargs,
        )
