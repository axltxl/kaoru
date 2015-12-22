# -*- coding: utf-8 -*-

"""
kaoru.commands.cancel
~~~~~~~~

/cancel command implementation

:copyright: (c) 2015 by Alejandro Ricoveri
:license: MIT, see LICENSE for more details.

"""

from .. import config
from .. import utils
from ..procutils import proc_exec_async
from . import bot_command

# /cancel command:
@bot_command
def _cmd_handler(bot, update):
    """Cancel any pending reboot/poweroffs"""

    proc_exec_async("sudo shutdown -c")
    config.set('queue_reboot', False)
    config.set('queue_poweroff', False)
    utils.echo_msg(bot, update, "Operations cancelled")

desc = 'Cancel any pending operation(s)'  # This command's description
cmd_handler = _cmd_handler  # command handler
cmd_str = 'cancel'  # command /string
