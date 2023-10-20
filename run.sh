#!/bin/bash
set -e 
set -o pipefail

if [ "$EUID" -ne 0 ]; then
  echo "This script must be run as root."
  exit 1
fi

username=cv-bastion
target_path=/opt/cv-bastion

sudo -u $username PYTHONPATH=$target_path/src CONFIG_FILE=$target_path/config.yaml  python3 $target_path/src