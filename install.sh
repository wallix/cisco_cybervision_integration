#!/bin/bash
set -e 
set -o pipefail

while :
do
    case "$1" in
      -h | --help)
          echo "This script installs the WALLIX Bastion integration on a CISCO Cyber Vision appliance."
          echo "Please read the associated README for additionnal information."
          exit 0
          ;;
      *)  # No more options
          break
          ;;
    esac
done

# Check if the script is being run as root
if [ "$EUID" -ne 0 ]; then
  echo "This script must be run as root."
  exit 1
fi

cat << EOF
This script installs the WALLIX Bastion integration for CISCO Cyber Vision.

It can be installed on a Cyber Vision appliance or another debian-based system.

The following information will be requested:
- (optional) A cron job frequency to execute the program periodically
- a user that can run cron jobs. On Cyber Vision, you should use cv-admin
- a path to store the integration directory. On Cyber Vision, it must be under /data

An editor will then open to fill up the integration configuration file.

Press enter to continue...
EOF

read

# Set the path to the Python package
package_path=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )


# Check if the package directory exists
if [ ! -d "$package_path" ]; then
  echo "Error: The current package directory was not found."
  exit 1
fi

read -p "Enter the frequency for the cron job (e.g., '0 7 * * 1-5' for every weekday at 7:00 AM) or press enter to skip cron configuration: " cron_frequency

read -p "Enter the name of an existing system user that should run the connector (ex: cv-admin): " -i "cv-admin" username


if ! id "$username" >/dev/null 2>&1; then
  echo "unknown user: $username"
  exit 1
fi

read -p "Enter the path where the connector files directory (cv-bastion) will be stored (ex: /data/home or /data/tmp): " target_path

target_path=$target_path/cv-bastion

mkdir -p $target_path

cp -r "$package_path/." "$target_path"

chown $username $target_path
chown -R $username $target_path/src
chmod -R 500 $target_path

if [[ ! -e "$target_path/config.yaml" ]]; then
    read -p "no config.yaml found. A vi editor will open to configure it. Press any key to continue" -n 1
    PYTHONPATH=$target_path/src python3 $target_path/src --show-conf > "$target_path/config.yaml"

    vi "$target_path/config.yaml" < "$(tty)" > "$(tty)"
fi

retcode=0
PYTHONPATH=$target_path/src CONFIG_FILE=$target_path/config.yaml python3 $target_path/src --check-preset || {
  retcode=$?
}

if [ $retcode -eq 2 ]; then
  read -p "Enter the id of the preset that should be used, then press enter: " preset_id

  sed -i "s/preset_id:.*/preset_id: $preset_id/" "$target_path/config.yaml"

  PYTHONPATH=$target_path/src CONFIG_FILE=$target_path/config.yaml python3 $target_path/src --check-preset

  echo "Preset successfully validated."
elif [ $retcode -ne 0 ]; then
  exit 1
fi

chown $username "$target_path/config.yaml"
chmod 400 "$target_path/config.yaml"

# Add the cron job for the dedicated user

if [[ -n $cron_frequency ]]; then
  echo "$cron_frequency PYTHONPATH=$target_path/src CONFIG_FILE=$target_path/config.yaml python3 $target_path/src" >> $target_path/crontab
  crontab -u "$username" $target_path/crontab  # Install the modified crontab

  # Clean up the temporary crontab file
  rm $target_path/crontab
fi

echo "Integration configured successfully. You can delete the extracted files at $package_path"

read -p "Delete the extracted files at $package_path? (y/n) " choice

case "$choice" in 
  y|Y|yes ) rm -rf $package_path;;
  n|N|no ) echo "ignored";;
  * ) echo "invalid response. ignored";;
esac

read -p "Would you like to run the integration now? (y/n) " choice

case "$choice" in 
  y|Y|yes ) sudo -u $username PYTHONPATH=$target_path/src CONFIG_FILE=$target_path/config.yaml  python3 $target_path/src;;
  n|N|no ) echo "skipped";;
  * ) echo "invalid response. skipped";;
esac