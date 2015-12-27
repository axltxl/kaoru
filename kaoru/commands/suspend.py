# -*- coding: utf-8 -*-

"""
kaoru.commands.suspend
~~~~~~~~

/suspend command implementation

:copyright: (c) 2015 by Alejandro Ricoveri
:license: MIT, see LICENSE for more details.

"""

import re

from .. import config
from .. import utils
from ..procutils import proc_exec_async, proc_select
from . import bot_command

# /suspend command:
@bot_command
def _cmd_handler(bot, update):
    """suspend your machine(s)"""

    suspend_exec = proc_select(['pm-suspend'])
    utils.echo_msg(bot, update, 'Your host(s) are going to be SUSPENDED')
    if re.match('.*pm-suspend$', suspend_exec):
        # pm-suspend needs to be run as root
        suspend_exec = 'sudo {}'.format(suspend_exec)
        proc_exec_async(suspend_exec)
    else:
        log.msg_err(
            "pm-suspend has not been found, "
            "make sure you have installed pm-utils on your system."
        )


desc = 'Suspend your host(s) to RAM'  # This command's description
cmd_handler = _cmd_handler  # command handler
cmd_str = 'suspend'  # command /string
