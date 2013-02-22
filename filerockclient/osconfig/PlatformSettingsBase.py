# -*- coding: ascii -*-
#  ______ _ _      _____            _       _____ _ _            _
# |  ____(_) |    |  __ \          | |     / ____| (_)          | |
# | |__   _| | ___| |__) |___   ___| | __ | |    | |_  ___ _ __ | |_
# |  __| | | |/ _ \  _  // _ \ / __| |/ / | |    | | |/ _ \ '_ \| __|
# | |    | | |  __/ | \ \ (_) | (__|   <  | |____| | |  __/ | | | |_
# |_|    |_|_|\___|_|  \_\___/ \___|_|\_\  \_____|_|_|\___|_| |_|\__|
#
# Copyright (C) 2012 Heyware s.r.l.
#
# This file is part of FileRock Client.
#
# FileRock Client is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# FileRock Client is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with FileRock Client. If not, see <http://www.gnu.org/licenses/>.
#

"""
This is the PlatformSettingsBase module.




----

This module is part of the FileRock Client.

Copyright (C) 2012 - Heyware s.r.l.

FileRock Client is licensed under GPLv3 License.

"""

import logging, os

class PlatformSpecificSettingsBase(object):

     # List of arguments that shall never go into autostart command string
    BLACKLISTED_ARGUMENTS = [
        u"--restart-count",
        u"-d"
    ]

    def __init__(self, *args, **kdws):
        self.cmdline_args = kdws['cmdline_args']
        self.logger = logging.getLogger("FR.%s" % self.__class__.__name__)

    def set_autostart(self, enable):
        """ Enable/disable client start on system startup """
        assert False, u"Unimplemented method set_autostart() called"

    def is_systray_icon_whitelisted(self):
        """ Check if tray icon will be visible (Ubuntu with Unity only) """
        assert False, u"Unimplemented method is_systray_icon_whitelisted() called"


    def whitelist_tray_icon(self):
        """ Sets client tray icon visible (Ubuntu with Unity only) """
        assert False, u"Unimplemented method whitelist_tray_icon() called"

    def _get_command_string(self):
        """
        Returns a string representing command line to start
        FileRock client, possibly stripping some unwanted args

        Might be overridden by PlatformSettings* classes
        """

        # Get filtered cmd line args
        arguments = self._filter_cmd_line_args(self.cmdline_args)

        # Ugly trick to patch relative path related issues
        # Abs-pathize everything that looks like a valid path
        arguments = map(
            lambda arg : os.path.abspath(arg) if not arg.startswith("-") and os.path.exists(arg) else arg,
            arguments
        )

        return " ".join(arguments).strip()


    def _filter_cmd_line_args(self, arguments):
        """
        Return a filtered list of cmd line args, which will
        be added to the launch agent plist file

        Might be overridden by PlatformSettings* classes
        """

        # Just strips everything that starts with a "-"
        # TODO: implement a smarter cmdline argument filtering strategy
        return filter(lambda arg: not arg.startswith("-"), arguments)

