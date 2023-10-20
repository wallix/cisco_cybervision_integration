import logging

import os

assert len(os.environ["PYTHONPATH"].split(":")) == 1, "unexpected PYTHONPATH"

import sys

sys.path.extend(
    [
        os.environ["PYTHONPATH"].rstrip("/") + "/" + dir
        for dir in (
            "site-packages",
            "lib",
            "generated",
            "generated/bastion",
            "generated/cybervision",
        )
    ]
)

import urllib3
from urllib3 import exceptions
from lib import sync

from lib import cybervision, bastion

from lib.conf import CONFIG, DUMB_CONF, load_conf

from lib.util import Exit


def main(check_only=False):
    load_conf()

    if not CONFIG.verify_ssl:
        urllib3.disable_warnings(category=exceptions.InsecureRequestWarning)

    loglevel = logging.DEBUG if CONFIG.debug else logging.INFO
    logging.basicConfig(level=loglevel)

    with cybervision.Cybervision() as cisco_client:
        with bastion.Bastion() as bastion_client:
            synchronizer = sync.Synchronizer(bastion_client, cisco_client)
            if check_only:
                synchronizer.check_preset()
            else:
                synchronizer.sync()


_HELP_ = """
This package provides an integration for CISCO Cybervision with WALLIX Bastion.

Please read the README.md for more details.

Options:

  -h  --help      Show this help
  --show-conf     Show the template of the config.yaml file
  --check-preset  If the preset found in the configuration is unset or invalid, prompt available presets
"""


if __name__ == "__main__":
    for arg in sys.argv[1:]:
        if arg in ("-h", "--help"):
            print(_HELP_)
            sys.exit(0)
        elif arg == "--show-conf":
            print(DUMB_CONF)
            sys.exit(0)
        elif arg == "--check-preset":
            try:
                main(check_only=True)
                print("Valid preset ID.")
            except Exit:
                sys.exit(2)
            sys.exit(0)
        else:
            print("unknown argument: " + arg)
            print(_HELP_)
            sys.exit(1)
    try:
        main()
    except Exit:
        logging.info("exiting")
        sys.exit(1)
