# -*- coding: utf-8 -*-

"""
kaoru.commands.reboot
~~~~~~~~

/reboot command implementation

:copyright: (c) 2015 by Alejandro Ricoveri
:license: MIT, see LICENSE for more details.

"""

from .. import config
from .. import utils
from ..procutils import proc_exec_async
from . import bot_command

# /reboot command:
@bot_command
def _cmd_handler(bot, update):
    """reboot your machine(s)"""

    if not config.get('queue_poweroff') and not config.get('queue_reboot'):
        utils.echo_msg(
            bot, update,
            "I'm going to be rebooted in about {} minute(s)".format(
                config.get('reboot_delay')
            )
        )
        proc_exec_async("sudo shutdown -r +{}".format(
                config.get('reboot_delay')
            )
        )
        config.set('queue_reboot', True)
    else:
        utils.echo_msg(
            bot, update,
            "Your machines are already going to be shutdown/rebooted"
        )

desc = 'Reboot your host(s)'  # This command's description
cmd_handler = _cmd_handler  # command handler
cmd_str = 'reboot'  # command /string
