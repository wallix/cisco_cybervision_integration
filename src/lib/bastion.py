from typing import Optional, Protocol, TypeVar, Union as U
from http import client as http_client

import urllib3
from urllib3._collections import HTTPHeaderDict

from time import time

from generated.bastion.bastion_client import Configuration

from generated.bastion.bastion_client import ApiClient
from generated.bastion.bastion_client.apis.tags.devices_api import DevicesApi

from generated.bastion.bastion_client import models


from generated.bastion.bastion_client.schemas import Unset

from .conf import CONFIG
from .util import APIError


def build_api_conf():
    if CONFIG.bastion.api_key:
        api_conf = Configuration(
            host=f"https://{CONFIG.bastion.host}:{CONFIG.bastion.port}/api/",
            api_key={
                "ApiAuthKey": CONFIG.bastion.api_key,
                "ApiAuthUser": CONFIG.bastion.username,
            },
        )
    elif CONFIG.bastion.password:
        api_conf = Configuration(
            host=f"https://{CONFIG.bastion.host}:{CONFIG.bastion.port}/api/",
            username=CONFIG.bastion.username,
            password=CONFIG.bastion.password,
        )
    else:
        raise RuntimeError(
            "invalid configuration: either bastion.password or bastion.api_key must be specified"
        )

    api_conf.verify_ssl = CONFIG.verify_ssl
    if api_conf.verify_ssl and CONFIG.bastion.ca_cert_path:
        api_conf.ssl_ca_cert = CONFIG.bastion.ca_cert_path

    api_conf.debug = CONFIG.debug
    http_client.HTTPConnection.debuglevel = (
        0  # keep it at zero to not log too much (e.g sensitive tokens)
    )

    return api_conf


Service = U[models.ServiceSsh, models.ServiceRdp, models.ServiceTelnet]


def make_service(protocol: str, port: int) -> Optional[Service]:
    if protocol == "SSH":
        return models.ServiceSsh(
            service_name="SSH",
            protocol="SSH",
            port=port,
            subprotocols=[
                "SSH_SHELL_SESSION",
                "SSH_REMOTE_COMMAND",
                "SSH_SCP_UP",
                "SSH_SCP_DOWN",
                "SFTP_SESSION",
            ],
            connection_policy="SSH",
        )
    if protocol == "RDP":
        return models.ServiceRdp(
            service_name="RDP",
            protocol="RDP",
            port=port,
            subprotocols=[
                "RDP_CLIPBOARD_UP",
                "RDP_CLIPBOARD_DOWN",
                "RDP_CLIPBOARD_FILE",
                "RDP_PRINTER",
                "RDP_COM_PORT",
                "RDP_DRIVE",
                "RDP_SMARTCARD",
                "RDP_AUDIO_OUTPUT",
                "RDP_AUDIO_INPUT",
            ],
            connection_policy="RDP",
        )
    if protocol == "TELNET":
        return models.ServiceTelnet(
            service_name="TELNET",
            protocol="TELNET",
            port=port,
            connection_policy="TELNET",
        )


class Bastion(ApiClient):
    def __init__(self):
        super().__init__(build_api_conf())

        self.devices = DevicesApi(self)

        self._session_cookies = None
        self._last_request_tm = 0

        assert CONFIG.bastion.timeout > 1, "too short bastion timeout"

    TOKEN_EXPIRES_SECS = 100

    def call_api(self, *args, **kwargs):
        kwargs["timeout"] = CONFIG.bastion.timeout
        resp = super().call_api(*args, **kwargs)

        if resp.status == 401 and self._session_cookies:
            self._session_cookies = None

            # retry
            resp = super().call_api(*args, **kwargs)

        if resp.status >= 300:
            body = resp.data.decode()

            raise APIError(
                f"Bastion client: received response {resp.status} for request {kwargs['method']} {resp.geturl()} containing: {body}",
                resp.status,
            )

        if resp.headers.get("Set-Cookie"):
            self._session_cookies = resp.headers["Set-Cookie"]

        self._last_request_tm = time()

        # fix bug when content type contains additional metadata
        ct: str = resp.headers["content-type"]

        if ";" in ct:
            resp.headers["content-type"] = ct.split(";")[0]

        return resp

    def update_params_for_auth(
        self, headers: HTTPHeaderDict, auth_settings, resource_path, method, body
    ):
        if self._session_cookies:
            if time() - self._last_request_tm < self.TOKEN_EXPIRES_SECS:
                headers["Cookie"] = self._session_cookies
                return
            self._session_cookies = None
        else:
            # during a retry, make sure we clean the cookie previously set
            headers.discard("Cookie")

        super().update_params_for_auth(
            headers, auth_settings, resource_path, method, body
        )


T = TypeVar("T")


class Response(Protocol[T]):
    response: urllib3.HTTPResponse
    body: T


class UnsetResponse(Protocol):
    response: urllib3.HTTPResponse
    body: Unset


def get_body(resp: U[Response[T], UnsetResponse]) -> T:
    return resp.body
