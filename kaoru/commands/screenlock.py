# -*- coding: utf-8 -*-

"""
kaoru.commands.screenlock
~~~~~~~~

/screenlock implementation

:copyright: (c) 2015 by Alejandro Ricoveri
:license: MIT, see LICENSE for more details.

"""

from telegram import Update
from .. import utils
from .. import config
from .. import log
from . import bot_command
from ..procutils import proc_exec_async

# /screenlock command:
@bot_command
def _cmd_handler(bot, update):
    """
    it basically runs a screen locker
    """

    # check for executables set for commands
    screenlock_exec = config.get('screenlock_cmd')
    if screenlock_exec is None:
        screenlock_exec = proc_select([
            'xlock', 'xscreensaver', 'i3lock'
            ],
        )
    # only execute the thing if existent
    if screenlock_exec is None:
        err_msg = "A suitable 'screenlock_cmd' has bot been found."
        utils.echo_msg(err_msg)
        log.msg_err(err_msg)
        return

    proc_exec_async(screenlock_exec)
    utils.echo_msg(bot, update, "Your screen(s) are now LOCKED")

desc = 'See if I "live"'  # This command's description
cmd_handler = _cmd_handler  # command handler
cmd_str = 'screenlock'  # command /string
