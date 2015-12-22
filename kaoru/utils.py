# -*- coding: utf-8 -*-

"""
kaoru.utils
~~~~~~~~

Utilities

:copyright: (c) 2015 by Alejandro Ricoveri
:license: MIT, see LICENSE for more details.

"""

import socket
import random
import time

from telegram import Update, ChatAction
from . import log
from . import config

def random_seed():
    """Seed the randomizer"""
    random.seed(int(time.time()))

def echo_msg(bot, update, msg, **kwargs):
    if isinstance(update, Update):
        # some basic info about the user
        userid = update.message.from_user.id
        username = update.message.from_user.username
        chat_id = update.message.chat_id

        # log the thing
        log.msg("echo message [{}@{}]: {}".format(username, userid, msg))

        # reformat message so it includes this machine's host name
        show_hostname = config.get('show_hostname')
        dry_run = config.get('dry_run')
        parse_mode = kwargs.get('parse_mode')
        if (show_hostname or dry_run) and parse_mode is None:
            tag = ""
            if show_hostname:
                tag = socket.gethostname()
            if dry_run:
                if len(tag):
                    tag += ":dr"
                else:
                    tag = "dr"
            tag = "[{}]".format(tag)
            msg = "{} {}".format(tag, msg)

        # send the actual message
        bot.sendChatAction(chat_id=chat_id, action=ChatAction.TYPING)
        bot.sendMessage(
            chat_id=chat_id,
            text=msg,
            **kwargs
        )
    else:
        log.msg("{} > {}".format(bot.username, msg))

def select_rand_str(candidates):
    """select a random string from a list

    :candidates: list of string candidates
    :returns: str

    """
    return candidates[random.randrange(0, len(candidates))]
