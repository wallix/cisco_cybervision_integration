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


class Preset(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Preset Json representation
    """


    class MetaOapg:
        
        class properties:
            activityTagless = schemas.StrSchema
            
            
            class badges(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['PresetBadge']:
                        return PresetBadge
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['PresetBadge'], typing.List['PresetBadge']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'badges':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'PresetBadge':
                    return super().__getitem__(i)
            
            
            class baselines(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['Baseline']:
                        return Baseline
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['Baseline'], typing.List['Baseline']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'baselines':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'Baseline':
                    return super().__getitem__(i)
        
            @staticmethod
            def category() -> typing.Type['Category']:
                return Category
            componentTagless = schemas.StrSchema
            creatorEmail = schemas.StrSchema
            custom = schemas.BoolSchema
            description = schemas.StrSchema
        
            @staticmethod
            def filters() -> typing.Type['PresetFilters']:
                return PresetFilters
            groupless = schemas.StrSchema
            id = schemas.StrSchema
            imported = schemas.BoolSchema
            label = schemas.StrSchema
            lastUpdate = schemas.Int64Schema
            operationalStarred = schemas.BoolSchema
            priority_order = schemas.Int64Schema
            search = schemas.StrSchema
            securityStarred = schemas.BoolSchema
            __annotations__ = {
                "activityTagless": activityTagless,
                "badges": badges,
                "baselines": baselines,
                "category": category,
                "componentTagless": componentTagless,
                "creatorEmail": creatorEmail,
                "custom": custom,
                "description": description,
                "filters": filters,
                "groupless": groupless,
                "id": id,
                "imported": imported,
                "label": label,
                "lastUpdate": lastUpdate,
                "operationalStarred": operationalStarred,
                "priority_order": priority_order,
                "search": search,
                "securityStarred": securityStarred,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["activityTagless"]) -> MetaOapg.properties.activityTagless: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["badges"]) -> MetaOapg.properties.badges: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["baselines"]) -> MetaOapg.properties.baselines: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["category"]) -> 'Category': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["componentTagless"]) -> MetaOapg.properties.componentTagless: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["creatorEmail"]) -> MetaOapg.properties.creatorEmail: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["custom"]) -> MetaOapg.properties.custom: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["filters"]) -> 'PresetFilters': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["groupless"]) -> MetaOapg.properties.groupless: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["imported"]) -> MetaOapg.properties.imported: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["label"]) -> MetaOapg.properties.label: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lastUpdate"]) -> MetaOapg.properties.lastUpdate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["operationalStarred"]) -> MetaOapg.properties.operationalStarred: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["priority_order"]) -> MetaOapg.properties.priority_order: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["search"]) -> MetaOapg.properties.search: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["securityStarred"]) -> MetaOapg.properties.securityStarred: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["activityTagless", "badges", "baselines", "category", "componentTagless", "creatorEmail", "custom", "description", "filters", "groupless", "id", "imported", "label", "lastUpdate", "operationalStarred", "priority_order", "search", "securityStarred", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["activityTagless"]) -> typing.Union[MetaOapg.properties.activityTagless, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["badges"]) -> typing.Union[MetaOapg.properties.badges, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["baselines"]) -> typing.Union[MetaOapg.properties.baselines, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["category"]) -> typing.Union['Category', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["componentTagless"]) -> typing.Union[MetaOapg.properties.componentTagless, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["creatorEmail"]) -> typing.Union[MetaOapg.properties.creatorEmail, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["custom"]) -> typing.Union[MetaOapg.properties.custom, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["filters"]) -> typing.Union['PresetFilters', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["groupless"]) -> typing.Union[MetaOapg.properties.groupless, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["imported"]) -> typing.Union[MetaOapg.properties.imported, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["label"]) -> typing.Union[MetaOapg.properties.label, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lastUpdate"]) -> typing.Union[MetaOapg.properties.lastUpdate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["operationalStarred"]) -> typing.Union[MetaOapg.properties.operationalStarred, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["priority_order"]) -> typing.Union[MetaOapg.properties.priority_order, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["search"]) -> typing.Union[MetaOapg.properties.search, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["securityStarred"]) -> typing.Union[MetaOapg.properties.securityStarred, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["activityTagless", "badges", "baselines", "category", "componentTagless", "creatorEmail", "custom", "description", "filters", "groupless", "id", "imported", "label", "lastUpdate", "operationalStarred", "priority_order", "search", "securityStarred", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        activityTagless: typing.Union[MetaOapg.properties.activityTagless, str, schemas.Unset] = schemas.unset,
        badges: typing.Union[MetaOapg.properties.badges, list, tuple, schemas.Unset] = schemas.unset,
        baselines: typing.Union[MetaOapg.properties.baselines, list, tuple, schemas.Unset] = schemas.unset,
        category: typing.Union['Category', schemas.Unset] = schemas.unset,
        componentTagless: typing.Union[MetaOapg.properties.componentTagless, str, schemas.Unset] = schemas.unset,
        creatorEmail: typing.Union[MetaOapg.properties.creatorEmail, str, schemas.Unset] = schemas.unset,
        custom: typing.Union[MetaOapg.properties.custom, bool, schemas.Unset] = schemas.unset,
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        filters: typing.Union['PresetFilters', schemas.Unset] = schemas.unset,
        groupless: typing.Union[MetaOapg.properties.groupless, str, schemas.Unset] = schemas.unset,
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        imported: typing.Union[MetaOapg.properties.imported, bool, schemas.Unset] = schemas.unset,
        label: typing.Union[MetaOapg.properties.label, str, schemas.Unset] = schemas.unset,
        lastUpdate: typing.Union[MetaOapg.properties.lastUpdate, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        operationalStarred: typing.Union[MetaOapg.properties.operationalStarred, bool, schemas.Unset] = schemas.unset,
        priority_order: typing.Union[MetaOapg.properties.priority_order, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        search: typing.Union[MetaOapg.properties.search, str, schemas.Unset] = schemas.unset,
        securityStarred: typing.Union[MetaOapg.properties.securityStarred, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Preset':
        return super().__new__(
            cls,
            *_args,
            activityTagless=activityTagless,
            badges=badges,
            baselines=baselines,
            category=category,
            componentTagless=componentTagless,
            creatorEmail=creatorEmail,
            custom=custom,
            description=description,
            filters=filters,
            groupless=groupless,
            id=id,
            imported=imported,
            label=label,
            lastUpdate=lastUpdate,
            operationalStarred=operationalStarred,
            priority_order=priority_order,
            search=search,
            securityStarred=securityStarred,
            _configuration=_configuration,
            **kwargs,
        )

from cybervision_client.model.baseline import Baseline
from cybervision_client.model.category import Category
from cybervision_client.model.preset_badge import PresetBadge
from cybervision_client.model.preset_filters import PresetFilters
