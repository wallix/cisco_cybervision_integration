from typing import Iterable, List, cast, Optional as Op, Protocol, TypeVar, Union as U
from http import client as http_client
import ipaddress
import urllib3

from generated.cybervision.cybervision_client import (
    ApiClient,
    Configuration,
)

from generated.cybervision.cybervision_client.models import (
    Tag,
    Flow,
    UserPropertyTuple,
)

from generated.cybervision.cybervision_client.schemas import (
    Unset,
)


from generated.cybervision.cybervision_client.apis.tags.devices_api import DevicesApi
from generated.cybervision.cybervision_client.apis.tags.components_api import (
    ComponentsApi,
)
from generated.cybervision.cybervision_client.apis.tags.custom_properties_api import (
    CustomPropertiesApi,
)
from generated.cybervision.cybervision_client.apis.tags.presets_api import PresetsApi

from .conf import CONFIG
from .util import APIError


def _get_cv_address():
    if not CONFIG.cybervision.remote_host:
        return "169.254.0.42:4443"  # default local address behind HAproxy
    if CONFIG.cybervision.remote_host in ("localhost", "0.0.0.0", "127.0.0.1"):
        print(
            "warning: cybervision.remote_host contains a local address. This will likely not work. Leave the field empty to run the program locally"
        )
    return f"{CONFIG.cybervision.remote_host}:{CONFIG.cybervision.remote_port}"


def build_api_conf():
    api_conf = Configuration(
        host=f"https://{_get_cv_address()}/api/3.0",
        api_key={"token": CONFIG.cybervision.api_token},
    )

    api_conf.verify_ssl = CONFIG.verify_ssl
    if api_conf.verify_ssl and CONFIG.cybervision.ca_cert_path:
        api_conf.ssl_ca_cert = CONFIG.cybervision.ca_cert_path

    api_conf.debug = CONFIG.debug
    http_client.HTTPConnection.debuglevel = (
        0  # keep it at zero to not log too much (e.g sensitive tokens)
    )

    return api_conf


def find_protocol_port(
    flows: Iterable[Flow], protocol_id: str, component_id: str
) -> Op[int]:
    for flow in flows:
        if (not flow["right"]) or flow["right"]["id"] != component_id:
            continue

        for tag in cast(List[Tag], flow["tags"] or []):
            if tag["id"] == protocol_id:
                port = int(flow["dstPort"])
                if port:
                    return port

    return None


def is_ip_good_candidate(raw_ip: str) -> bool:
    try:
        ip = ipaddress.ip_address(raw_ip)
    except ValueError:
        return False

    if ip.is_loopback or ip.is_unspecified or ip.is_reserved:
        return False

    return isinstance(ip, ipaddress.IPv4Address)


def select_ip(ips: Iterable[str]) -> Op[str]:
    ipv6: Op[ipaddress.IPv6Address] = None

    for raw_ip in ips:
        try:
            ip = ipaddress.ip_address(raw_ip)
        except ValueError:
            continue

        if ip.is_loopback or ip.is_unspecified or ip.is_reserved:
            continue

        if isinstance(ip, ipaddress.IPv4Address):
            return str(ip)

        if not ipv6:
            ipv6 = ip

    if not ipv6:
        return None

    return str(ipv6)


def find_prop(
    device_props: Op[Iterable[UserPropertyTuple]], key: str
) -> Op[UserPropertyTuple]:
    if not device_props:
        return None

    for prop in device_props:
        if prop["key"] == key:
            return prop

    return None


T = TypeVar("T")


class Response(Protocol[T]):
    response: urllib3.HTTPResponse
    body: T


class UnsetResponse(Protocol):
    response: urllib3.HTTPResponse
    body: Unset


def get_body(resp: U[Response[T], UnsetResponse]) -> T:
    """typing helper"""
    return resp.body


class Cybervision(ApiClient):
    def __init__(self):
        super().__init__(build_api_conf())

        self.devices = DevicesApi(self)

        self.components = ComponentsApi(self)

        self.user_props = CustomPropertiesApi(self)

        self.presets_api = PresetsApi(self)

        assert CONFIG.cybervision.timeout > 1, "too short bastion timeout"

    def call_api(self, *args, **kwargs):
        kwargs["timeout"] = CONFIG.cybervision.timeout
        resp = super().call_api(*args, **kwargs)

        if resp.status >= 300:
            body = resp.data.decode()
            raise APIError(
                f"Cybervision client: received response {resp.status} for request {kwargs['method']} {resp.geturl()} containing: {body}",
                resp.status,
            )

        return resp
