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


class PropertyTupleWithArrayOfValuesByPosition(
    schemas.ListSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['PropertyTupleWithArrayOfValues']:
            return PropertyTupleWithArrayOfValues

    def __new__(
        cls,
        _arg: typing.Union[typing.Tuple['PropertyTupleWithArrayOfValues'], typing.List['PropertyTupleWithArrayOfValues']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'PropertyTupleWithArrayOfValuesByPosition':
        return super().__new__(
            cls,
            _arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'PropertyTupleWithArrayOfValues':
        return super().__getitem__(i)

from cybervision_client.model.property_tuple_with_array_of_values import PropertyTupleWithArrayOfValues