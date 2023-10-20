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


class Flow(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    JSON flow representation
    """


    class MetaOapg:
        
        class properties:
            
            
            class tags(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['Tag']:
                        return Tag
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['Tag'], typing.List['Tag']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'tags':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'Tag':
                    return super().__getitem__(i)
            bytesCount = schemas.IntSchema
            direction = schemas.StrSchema
            dstPort = schemas.Int64Schema
            firstActivity = schemas.Int64Schema
            id = schemas.StrSchema
            lastActivity = schemas.Int64Schema
        
            @staticmethod
            def left() -> typing.Type['FlowEndpoint']:
                return FlowEndpoint
            packetsCount = schemas.IntSchema
            protocol = schemas.StrSchema
        
            @staticmethod
            def right() -> typing.Type['FlowEndpoint']:
                return FlowEndpoint
            srcPort = schemas.Int64Schema
            __annotations__ = {
                "tags": tags,
                "bytesCount": bytesCount,
                "direction": direction,
                "dstPort": dstPort,
                "firstActivity": firstActivity,
                "id": id,
                "lastActivity": lastActivity,
                "left": left,
                "packetsCount": packetsCount,
                "protocol": protocol,
                "right": right,
                "srcPort": srcPort,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tags"]) -> MetaOapg.properties.tags: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["bytesCount"]) -> MetaOapg.properties.bytesCount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["direction"]) -> MetaOapg.properties.direction: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dstPort"]) -> MetaOapg.properties.dstPort: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["firstActivity"]) -> MetaOapg.properties.firstActivity: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lastActivity"]) -> MetaOapg.properties.lastActivity: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["left"]) -> 'FlowEndpoint': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["packetsCount"]) -> MetaOapg.properties.packetsCount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["protocol"]) -> MetaOapg.properties.protocol: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["right"]) -> 'FlowEndpoint': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["srcPort"]) -> MetaOapg.properties.srcPort: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["tags", "bytesCount", "direction", "dstPort", "firstActivity", "id", "lastActivity", "left", "packetsCount", "protocol", "right", "srcPort", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tags"]) -> typing.Union[MetaOapg.properties.tags, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["bytesCount"]) -> typing.Union[MetaOapg.properties.bytesCount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["direction"]) -> typing.Union[MetaOapg.properties.direction, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dstPort"]) -> typing.Union[MetaOapg.properties.dstPort, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["firstActivity"]) -> typing.Union[MetaOapg.properties.firstActivity, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lastActivity"]) -> typing.Union[MetaOapg.properties.lastActivity, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["left"]) -> typing.Union['FlowEndpoint', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["packetsCount"]) -> typing.Union[MetaOapg.properties.packetsCount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["protocol"]) -> typing.Union[MetaOapg.properties.protocol, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["right"]) -> typing.Union['FlowEndpoint', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["srcPort"]) -> typing.Union[MetaOapg.properties.srcPort, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["tags", "bytesCount", "direction", "dstPort", "firstActivity", "id", "lastActivity", "left", "packetsCount", "protocol", "right", "srcPort", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        tags: typing.Union[MetaOapg.properties.tags, list, tuple, schemas.Unset] = schemas.unset,
        bytesCount: typing.Union[MetaOapg.properties.bytesCount, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        direction: typing.Union[MetaOapg.properties.direction, str, schemas.Unset] = schemas.unset,
        dstPort: typing.Union[MetaOapg.properties.dstPort, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        firstActivity: typing.Union[MetaOapg.properties.firstActivity, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        lastActivity: typing.Union[MetaOapg.properties.lastActivity, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        left: typing.Union['FlowEndpoint', schemas.Unset] = schemas.unset,
        packetsCount: typing.Union[MetaOapg.properties.packetsCount, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        protocol: typing.Union[MetaOapg.properties.protocol, str, schemas.Unset] = schemas.unset,
        right: typing.Union['FlowEndpoint', schemas.Unset] = schemas.unset,
        srcPort: typing.Union[MetaOapg.properties.srcPort, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Flow':
        return super().__new__(
            cls,
            *_args,
            tags=tags,
            bytesCount=bytesCount,
            direction=direction,
            dstPort=dstPort,
            firstActivity=firstActivity,
            id=id,
            lastActivity=lastActivity,
            left=left,
            packetsCount=packetsCount,
            protocol=protocol,
            right=right,
            srcPort=srcPort,
            _configuration=_configuration,
            **kwargs,
        )

from cybervision_client.model.flow_endpoint import FlowEndpoint
from cybervision_client.model.tag import Tag
