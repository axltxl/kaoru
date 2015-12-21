# -*- coding: utf-8 -*-

"""
kaoru.utils
~~~~~~~~

Utilities

:copyright: (c) 2015 by Alejandro Ricoveri
:license: MIT, see LICENSE for more details.

"""

import socket
from telegram import Update
from . import log
from . import config

def echo_msg(bot, update, msg):
    if isinstance(update, Update):
        # some basic info about the user
        userid = update.message.from_user.id
        username = update.message.from_user.username

        # log the thing
        log.msg("echo message [{}@{}]: {}".format(username, userid, msg))

        # reformat message so it includes this machine's host name
        show_hostname = config.get('show_hostname')
        dry_run = config.get('dry_run')
        if show_hostname or dry_run:
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
        bot.sendMessage(
            chat_id=update.message.chat_id,
            text=msg
        )
    else:
        log.msg("{} > {}".format(bot.username, msg))
