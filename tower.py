# Initial credit goes to Github's lowwalker.

# Tower SOS plugin
#
# gettext required for ubuntu

from sos.plugins import Plugin, RedHatPlugin, DebianPlugin, UbuntuPlugin
import os

class Tower(Plugin):
    '''Tower SOS plugin.'''
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
                "/var/log/supervisor/"
           ]

        # Tower Dirs
        self.add_copy_specs(dirs)

        # Commands
        for command in commands:
            self.add_cmd_output(command)

class RHELTower(Tower, RedHatPlugin):
    """Basic system information RHEL based distributions"""
    def setup(self):
        super(RHELTower, self).setup()
        self.add_copy_spec("/var/log/syslog")

class UbuntuTower(Tower, DebianPlugin, UbuntuPlugin):
    """Basic system information Ubuntu based distributions"""
    def setup(self):
        super(UbuntuTower, self).setup()
        dirs= [ "/var/log/syslog",
            "/var/log/udev",
            "/var/log/kern*",
            "/var/log/dist-upgrade",
            "/var/log/installer",
            "/var/log/unattended-upgrades",
            "/var/log/apport.log" ]

        self.add_copy_specs(dirs)
