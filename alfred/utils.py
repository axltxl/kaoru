# -*- coding: utf-8 -*-

"""
alfred.utils
~~~~~~~~

Utilities

:copyright: (c) 2015 by Alejandro Ricoveri
:license: MIT, see LICENSE for more details.

"""

import socket
from . import log
from . import config

def echo_msg(bot, update, msg):
    # some basic info about the user
    userid = update.message.from_user.id
    username = update.message.from_user.username

    # log the thing
    log.msg("echo message [{}@{}]: {}".format(username, userid, msg))

    # reformat message so it includes this machine's host name
    hostname = socket.gethostname()
    if not config.get('dry_run'):
        tag = "[{}]".format(hostname)
    else:
        tag = "[{}:dry-run]".format(hostname)
    msg = "{} {}".format(tag, msg)

    # send the actual message
    bot.sendMessage(
        chat_id=update.message.chat_id,
        text=msg
    )
