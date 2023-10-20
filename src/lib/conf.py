from dataclasses import dataclass, Field, MISSING, asdict

from typing import Any, cast, Dict

import json

import os

import yaml


@dataclass
class _ConfBase:
    pass


@dataclass
class BastionConf(_ConfBase):
    host: str
    username: str
    password: str = ""
    api_key: str = ""
    auto_onboard: bool = True
    timeout: int = 30
    port: int = 443
    ca_cert_path: str = ""


@dataclass
class CybervisionConf(_ConfBase):
    api_token: str
    preset_id: str
    timeout: int = 30
    remote_host: str = ""
    remote_port: int = 443
    ca_cert_path: str = ""


@dataclass
class Config(_ConfBase):
    cybervision: CybervisionConf
    bastion: BastionConf
    verify_ssl: bool = True
    debug: bool = False

    __initialized__ = False

    def __getattribute__(self, __name: str) -> Any:
        if not super().__getattribute__("__initialized__"):
            raise RuntimeError("config read before initialization")
        return super().__getattribute__(__name)


_conf_path_ = os.getenv("CONFIG_FILE", "config.yaml")

DUMB_CONF = """# cv-bastion integration configuration file.
# When using vim, type "i" to start editing and esc+":wq" to save and exit.

cybervision:  
  # CISCO Cybervision API token. Create one in Admin > API > Token
  api_token: xxx-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
  
  # ID of the preset from which devices will be synchronized with the Bastion.
  #
  # Devices that do not belong to this preset will not be onboarded or tagged on the Bastion.
  #
  # The ID can be found in the url path when opening the preset in cybervision UI.
  # 
  # If you leave it unset, you will be prompted with the available sets on your cybervision appliance.
  preset_id: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
  
  # timeout for requests issued to Cybervision (secs). 30 is default
  timeout: 30

  # CISCO Cybervision host address if the integration is executed from another machine.
  # Leave it empty by default.
  remote_host: ""
  
  # Port to use when remote_host is set, 443 by default.
  remote_port: 443
  
  # Optional. Path to a certificate authority (pem) to use to validate the cybervision server certificate.
  # Ignored if verify is False
  ca_cert_path: ""

bastion:

  # WALLIX Bastion host address (required)
  host: ""
  
  # username to use for identification on the Bastion. It must be a valid Bastion user with devices write permissions.
  username: "bastion_username"

  # user password, if api_key is not provided.
  password: "xxxxxxxx"
  
  # WALLIX Bastion API key, if password is not provided. Create one in Configuration > API keys
  api_key: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
  
  # if true, all devices found in the cybervision preset will be added to the Bastion devices.
  # Otherwise, those that are not found on the Bastion will be ignored.
  auto_onboard: true
  
  # timeout for requests issued to the Bastion (secs). 30 is default
  timeout: 30
  
  # Bastion API port to use. 443 by default.
  port: 443
  
  # Optional. Path to a certificate authority (pem) to use to validate the bastion server certificate.
  # Ignored if verify is False
  ca_cert_path: ""

# if false, TLS certificates of CISCO cybervision and WALLIX Bastion will not be verified.
verify_ssl: true

# if true, debug logs will be displayed
debug: false
"""


def _dumb_conf():
    return Config(
        cybervision=CybervisionConf(
            api_token="xxx-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            preset_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
        ),
        bastion=BastionConf(
            host="0.0.0.0",
            username="bastion_username",
            api_key="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            password="xxxxxxxx",
            auto_onboard=True,
        ),
        verify_ssl=True,
        debug=False,
    )


def _apply(data, instance: _ConfBase, path="") -> None:
    """validate data against instance which should be a dataclass field with dumb values.
    The values are overriden by the fields found in data"""

    if not isinstance(data, dict):
        raise RuntimeError(
            _conf_path_
            + ": expected field "
            + path
            + " to have the following content:\n"
            + yaml.safe_dump(
                asdict(instance),
            )
        )

    path = path + "." if path else ""

    for field, props in cast(Dict[str, Field], instance.__dataclass_fields__).items():
        dumb_val = getattr(instance, field)

        if field not in data or data[field] in (None, ""):
            if props.default is MISSING:
                # no default value
                if isinstance(dumb_val, _ConfBase):
                    dumb_val = asdict(dumb_val)
                raise RuntimeError(
                    _conf_path_
                    + ": expect field "
                    + path
                    + field
                    + " of the form: "
                    + yaml.safe_dump(dumb_val)
                )
            setattr(instance, field, props.default)
            continue

        val = data[field]

        if isinstance(dumb_val, _ConfBase):
            _apply(val, dumb_val, path=path + field)
            continue

        if not isinstance(val, props.type):
            raise RuntimeError(
                _conf_path_
                + ": expect field "
                + path
                + field
                + " to have type "
                + props.type.__name__
                + " but got "
                + type(val).__name__
            )

        if isinstance(val, str) and val == "":
            raise RuntimeError(
                _conf_path_ + ": field " + path + field + ": unexpected empty value"
            )

        setattr(instance, field, val)


def load_conf():
    try:
        perm = os.stat(_conf_path_).st_mode

        if oct(perm)[-2:] != "00":
            print(f"warning: {_conf_path_} is group/world readable. This is unsecure.")

        with open(_conf_path_, "r") as conffile:
            data = yaml.safe_load(conffile)

    except yaml.YAMLError as exc:
        raise RuntimeError(
            "invalid config file. Please check for syntax errors"
        ) from exc

    except FileNotFoundError as exc:
        raise RuntimeError(
            _conf_path_
            + " not found in the working directory. "
            + " Create a file named config.yaml or specify its path using the env var 'CONFIG_PATH', "
            + "and add the following content:\n"
            + DUMB_CONF
        ) from exc

    CONFIG.__initialized__ = True
    _apply(data, CONFIG)


CONFIG = _dumb_conf()
