# Copyright (c) 2014 Ansible, Inc.
# All Rights Reserved.

from sos.plugins import Plugin, RedHatPlugin, UbuntuPlugin

class tower(Plugin, RedHatPlugin, UbuntuPlugin):
    '''Tower SOS plugin'''
    plugin_name = "tower"

    def setup(self):

        commands = [
                     "ansible --version",      # ansible core version
                     "awx-manage --version",   # tower version
                     "supervisorctl status",   # tower process status
                     "tree -d /var/lib/awx",   # show me the dirs
                     "ls -ll /var/lib/awx",    # check permissions
                     "ls -ll /etc/awx"
                   ]

        dirs = [
                "/etc/awx/",
                "/var/log/supervisor/",
                "/var/log/syslog",
                "/var/log/udev",
                "/var/log/kern*",
                "/var/log/dist-upgrade",
                "/var/log/installer",
                "/var/log/unattended-upgrades",
                "/var/log/apport.log"
           ]

        for path in dirs:
            self.add_copy_spec(path)

        for command in commands:
            self.collect_ext_output(command)
