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


class ServiceGet(
    schemas.ComposedBase,
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        @staticmethod
        def discriminator():
            return {
                'protocol': {
                    'RAWTCPIP': RawtcpipService,
                    'RDP': RdpService,
                    'RLOGIN': RloginService,
                    'SSH': SshService,
                    'TELNET': TelnetService,
                    'VNC': VncService,
                    'rawtcpip_service': RawtcpipService,
                    'rdp_service': RdpService,
                    'rlogin_service': RloginService,
                    'ssh_service': SshService,
                    'telnet_service': TelnetService,
                    'vnc_service': VncService,
                }
            }
        
        @classmethod
        @functools.lru_cache()
        def one_of(cls):
            # we need this here to make our import statements work
            # we must store _composed_schemas in here so the code is only run
            # when we invoke this method. If we kept this at the class
            # level we would get an error because the class level
            # code would be run when this module is imported, and these composed
            # classes don't exist yet because their module has not finished
            # loading
            return [
                SshService,
                RloginService,
                TelnetService,
                RawtcpipService,
                RdpService,
                VncService,
            ]


    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ServiceGet':
        return super().__new__(
            cls,
            *_args,
            _configuration=_configuration,
            **kwargs,
        )

from bastion_client.model.rawtcpip_service import RawtcpipService
from bastion_client.model.rdp_service import RdpService
from bastion_client.model.rlogin_service import RloginService
from bastion_client.model.ssh_service import SshService
from bastion_client.model.telnet_service import TelnetService
from bastion_client.model.vnc_service import VncService
