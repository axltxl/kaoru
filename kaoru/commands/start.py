# -*- coding: utf-8 -*-

"""
kaoru.commands.start
~~~~~~~~

/start command implementation

:copyright: (c) 2015 by Alejandro Ricoveri
:license: MIT, see LICENSE for more details.

"""

from telegram import Update, ParseMode, Emoji
from . import bot_command
from .. import utils

# /start command
@bot_command
def _cmd_handler(bot, update):
    # set the user name
    username = 'user'
    if isinstance(update, Update):
        username = update.message.from_user.first_name

    # the actual message to semt
    start_msg = \
    """
_Hello world!_  ... Oh!, I meant Hello {user} .... {flushed_face}
I can't promise I won't break, but I'll put my best to assist you!
Anyways, *let's do this!, shall we?*, start by asking me for /help
    """.format(user=username, flushed_face=Emoji.FLUSHED_FACE).strip()

    # and send the thing
    utils.echo_msg(
        bot, update, start_msg, parse_mode=ParseMode.MARKDOWN
    )

cmd_list = None  #
desc = 'Start me up'  # This command's description
cmd_handler = _cmd_handler  # command handler
cmd_str = 'start'  # command /string
