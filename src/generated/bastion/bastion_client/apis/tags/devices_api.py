# coding: utf-8

"""
    WALLIX Bastion Rest API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 3.12
    Contact: support@wallix.com
    Generated by: https://openapi-generator.tech
"""

from bastion_client.paths.devices.post import AddDevice
from bastion_client.paths.devices_device_id.put import EditDevice
from bastion_client.paths.devices_device_id.get import GetDevice
from bastion_client.paths.devices.get import GetDevices


class DevicesApi(
    AddDevice,
    EditDevice,
    GetDevice,
    GetDevices,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass