# CISCO Cybervision integration for WALLIX Bastion

Enhance your IT & OT infrastructure management with the CISCO Cybervision connector for WALLIX Bastion.

This connector enables:

- automatic onboarding of devices discovered by Cybervision on a Bastion appliance
- one-time and periodic synchronization of devices metadata between Cybervision and Bastion

## Installation

Upload the archive to your Cybervision appliance, then unzip it using `tar -xf <archive_file>`.

You will find three shell scripts inside, which must be run as root:

- `install.sh`: perform a guided installation of the connector as a cron task
- `run.sh`: force a manual execution of the connector (after a successfull installation)

The install will ask for the frequency to set on the cron task, an existing user to execute the program and a path to store the files.
As Cybervision system files are read-only, you cannot create a new user. You can choose to run it as root or cv-admin. cv-admin is recommended.
Likewise, the files can only be stored under the `/data` directory, e.G in /data/home/cv-bastion or /data/tmp/cv-bastion.

You may also choose to install the integration on a separate machine. In this case it is recommended to create a dedicated user without login ability, i.e configuring /bin/false as login shell.
Mind that to run crob jobs, the user needs a home directory.

To update the connector, simply run the `install.sh` script from the new version with the same inputs to override the previous installation.

The logs of the connector when run using cron will be found within syslog. (on Cyber Vision they are located at /data/log/syslog)

You can update the `config.yaml` file at anytime. Make sure the file ownership remains to the user that runs the connector.

## What it does

Each run of the connector executes the following operations:

1. Find all devices on the Bastion
2. For each device on Cybervision: check if it has a property `bastion.id` or an IP address which matches one in the Bastion devices.
   If a match is found, the following custom properties are added or updated on the Cybervision device:
   - bastion.id (if unset)
   - all Bastion services, in the form `bastion.service.<svc>: <port>`, ex: `bastion.service.ssh: 22`
   - bastion.lastSync
3. Find all devices in the selected Cybervision preset
4. For each device in the preset: if it does not exist on the Bastion and bastion.auto_onboard is true, add the device on the Bastion

   The connector identifies all tagged services which are relevant for the Bastion (SSH, RDP and TELNET) and the associated port.

   If none of these services is found and no public IP is mentioned on the device, it is skipped.

   The device is created with the following properties:

   - name: Cybervision label
   - services: the services mentioned above if detected by Cybervision
   - IP: the first public IP found for one of these services
   - Tags:
     - all tags found on Cybervision, written in the form `cybervision.<tag category>.<tag name>: 1`. Tags from the "Network analysis" category are ignored.
     - the following device properties: "serial-number", "model-ref", "vendor-name", "fw-version", written in the form `cybervision.serial_number: xxxx`

   The connector also add the tags `cybervision.id` and `cybervision.lastSync`.

   Likewise, a user property names `bastion.id`and `bastion.lastSync` is added to the Cybervision device.

5. If the device already exists, its tags are updated (using the Cybervision tags and properties mentioned above)

## Ignore a specific device

A Cybervision device belonging to the selected preset can be skipped from onboarding and tags synchronization by applying the property "bastion.ignore" with value "yes" or "true".

## Uninstall

To uninstall the integration, simply delete the installation directory and run `crontab -r -u "user"` with the username used to run the integration to delete the user crontab. If the user crontab may contain other cron tasks, use `crontab -e -u "user" instead to edit it and remove the corresponding line.
