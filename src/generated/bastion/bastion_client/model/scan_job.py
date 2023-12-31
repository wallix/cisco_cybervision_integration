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


class ScanJob(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            id = schemas.StrSchema
            
            
            class type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "ad_for_devices": "AD_FOR_DEVICES",
                        "ad_for_accounts": "AD_FOR_ACCOUNTS",
                        "networks_for_devices": "NETWORKS_FOR_DEVICES",
                        "devices_for_accounts": "DEVICES_FOR_ACCOUNTS",
                        "azure_for_devices": "AZURE_FOR_DEVICES",
                    }
                
                @schemas.classproperty
                def AD_FOR_DEVICES(cls):
                    return cls("ad_for_devices")
                
                @schemas.classproperty
                def AD_FOR_ACCOUNTS(cls):
                    return cls("ad_for_accounts")
                
                @schemas.classproperty
                def NETWORKS_FOR_DEVICES(cls):
                    return cls("networks_for_devices")
                
                @schemas.classproperty
                def DEVICES_FOR_ACCOUNTS(cls):
                    return cls("devices_for_accounts")
                
                @schemas.classproperty
                def AZURE_FOR_DEVICES(cls):
                    return cls("azure_for_devices")
            
            
            class error(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 1024
            
            
            class status(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "running": "RUNNING",
                        "cancelled": "CANCELLED",
                        "error": "ERROR",
                        "success": "SUCCESS",
                    }
                
                @schemas.classproperty
                def RUNNING(cls):
                    return cls("running")
                
                @schemas.classproperty
                def CANCELLED(cls):
                    return cls("cancelled")
                
                @schemas.classproperty
                def ERROR(cls):
                    return cls("error")
                
                @schemas.classproperty
                def SUCCESS(cls):
                    return cls("success")
            
            
            class progress(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['ScanJobProgress']:
                        return ScanJobProgress
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['ScanJobProgress'], typing.List['ScanJobProgress']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'progress':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'ScanJobProgress':
                    return super().__getitem__(i)
            start = schemas.StrSchema
            end = schemas.StrSchema
            
            
            class result(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['ScanJobResult']:
                        return ScanJobResult
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['ScanJobResult'], typing.List['ScanJobResult']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'result':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'ScanJobResult':
                    return super().__getitem__(i)
        
            @staticmethod
            def configuration() -> typing.Type['ScanJobConfiguration']:
                return ScanJobConfiguration
            __annotations__ = {
                "id": id,
                "type": type,
                "error": error,
                "status": status,
                "progress": progress,
                "start": start,
                "end": end,
                "result": result,
                "configuration": configuration,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["error"]) -> MetaOapg.properties.error: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["progress"]) -> MetaOapg.properties.progress: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["start"]) -> MetaOapg.properties.start: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["end"]) -> MetaOapg.properties.end: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["result"]) -> MetaOapg.properties.result: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["configuration"]) -> 'ScanJobConfiguration': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "type", "error", "status", "progress", "start", "end", "result", "configuration", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["error"]) -> typing.Union[MetaOapg.properties.error, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["progress"]) -> typing.Union[MetaOapg.properties.progress, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["start"]) -> typing.Union[MetaOapg.properties.start, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["end"]) -> typing.Union[MetaOapg.properties.end, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["result"]) -> typing.Union[MetaOapg.properties.result, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["configuration"]) -> typing.Union['ScanJobConfiguration', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "type", "error", "status", "progress", "start", "end", "result", "configuration", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
        error: typing.Union[MetaOapg.properties.error, str, schemas.Unset] = schemas.unset,
        status: typing.Union[MetaOapg.properties.status, str, schemas.Unset] = schemas.unset,
        progress: typing.Union[MetaOapg.properties.progress, list, tuple, schemas.Unset] = schemas.unset,
        start: typing.Union[MetaOapg.properties.start, str, schemas.Unset] = schemas.unset,
        end: typing.Union[MetaOapg.properties.end, str, schemas.Unset] = schemas.unset,
        result: typing.Union[MetaOapg.properties.result, list, tuple, schemas.Unset] = schemas.unset,
        configuration: typing.Union['ScanJobConfiguration', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ScanJob':
        return super().__new__(
            cls,
            *_args,
            id=id,
            type=type,
            error=error,
            status=status,
            progress=progress,
            start=start,
            end=end,
            result=result,
            configuration=configuration,
            _configuration=_configuration,
            **kwargs,
        )

from bastion_client.model.scan_job_configuration import ScanJobConfiguration
from bastion_client.model.scan_job_progress import ScanJobProgress
from bastion_client.model.scan_job_result import ScanJobResult
