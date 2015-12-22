# -*- coding: utf-8 -*-

"""
kaoru.commands.unknown
~~~~~~~~

Default command handler

:copyright: (c) 2015 by Alejandro Ricoveri
:license: MIT, see LICENSE for more details.

"""

from .. import utils
from . import bot_command

@bot_command
def _cmd_handler(bot, update):
    """default command handler"""

    chatter_name = update.message.from_user.first_name
    utils.echo_msg(
        bot, update,
        "I am sorry {}. I'm afraid I cannot do that ...".format(chatter_name)
    )

cmd_handler = _cmd_handler  # command handler
