# -*- coding: utf-8 -*-

"""
kaoru.commands.poweroff
~~~~~~~~

/poweroff command implementation

:copyright: (c) 2015 by Alejandro Ricoveri
:license: MIT, see LICENSE for more details.

"""

from .. import config
from .. import utils
from ..procutils import proc_exec_async
from . import bot_command

# /poweroff command:
@bot_command
def _cmd_handler(bot, update):
    """turn off your machine(s)"""

    if not config.get('queue_poweroff') and not config.get('queue_reboot'):
        utils.echo_msg(
            bot, update,
            "Your machines are to be shutdown in about {} minute(s)".format(
                config.get('poweroff_delay')
            )
        )
        proc_exec_async("sudo shutdown -P +{}".format(
                config.get('poweroff_delay')
            )
        )
        config.set('queue_poweroff', True)
    else:
        utils.echo_msg(
            bot, update,
            "Your machines are already going to be shutdown/rebooted"
        )


desc = 'Shut down your host(s)'  # This command's description
cmd_handler = _cmd_handler  # command handler
cmd_str = 'poweroff'  # command /string
