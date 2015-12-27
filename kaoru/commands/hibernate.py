# -*- coding: utf-8 -*-

"""
kaoru.commands.hibernate
~~~~~~~~

/hibernate command implementation

:copyright: (c) 2015 by Alejandro Ricoveri
:license: MIT, see LICENSE for more details.

"""

import re

from .. import config
from .. import utils
from ..procutils import proc_exec_async, proc_select
from . import bot_command

# /hibernate command:
@bot_command
def _cmd_handler(bot, update):
    """hibernate your machine(s)"""

    hibernate_exec = proc_select(['pm-hibernate'])
    utils.echo_msg(
        bot, update,
        'Your host(s) are going to be put into HIBERNATION'
    )
    if re.match('.*pm-hibernate$', hibernate_exec):
        # pm-hibernate needs to be run as root
        hibernate_exec = 'sudo {}'.format(hibernate_exec)
        proc_exec_async(hibernate_exec)
    else:
        log.msg_err(
            "pm-hibernate has not been found, "
            "make sure you have installed pm-utils on your system."
        )


desc = 'Suspend your host(s) to disk'  # This command's description
cmd_handler = _cmd_handler  # command handler
cmd_str = 'hibernate'  # command /string
