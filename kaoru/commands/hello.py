# -*- coding: utf-8 -*-

"""
kaoru.commands.hello
~~~~~~~~

/hello command implementation

:copyright: (c) 2015 by Alejandro Ricoveri
:license: MIT, see LICENSE for more details.

"""

from telegram import Update
from .. import utils
from . import bot_command

# /hello command
@bot_command
def _cmd_handler(bot, update):
    """a rather simple ping command"""

    if isinstance(update, Update):
        chatter_name = update.message.from_user.first_name
        utils.echo_msg(
            bot, update,
            "Affirmative, {}. I read you. ".format(chatter_name)
        )
    else:
        utils.echo_msg(bot, update, "Affirmative. I read you. ")

desc = 'See if I "live"'  # This command's description
cmd_handler = _cmd_handler  # command handler
cmd_str = 'hello'  # command /string
