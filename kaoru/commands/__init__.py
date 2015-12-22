# -*- coding: utf-8 -*-

"""
kaoru.commands
~~~~~~~~

The very basics

:copyright: (c) 2015 by Alejandro Ricoveri
:license: MIT, see LICENSE for more details.

"""

from telegram import Update
from .. import db
from .. import log
from .. import security

def bot_command(command_func):
    """
    A decorator whose purpose is to stack middleware
    routines on top of its target function
    """

    # the actual wrapper function
    def _wrapper(bot, update):
        ###################################
        # all middleware can be run in here
        ###################################
        if isinstance(update, Update):
            username = update.message.from_user.username
            userid = update.message.from_user.id
            command = update.message.text
            log.msg_debug("[{}:{}] Received command: '{}'".format(
                    username, userid, command
                )
            )

            #########################
            # perform security checks
            #########################
            try:
                security.check_update(update)
            except security.SecurityException as sec_except:
                log.msg_err(sec_except)
                return

            ###################################################
            # Grab the update and append it to database to keep
            # constant track of what this bot is getting
            ###################################################
            db.insert_update(update)
        else:
            # I have received a string command
            log.msg_debug("Received command: '{}'".format(update))

        # Finally, execute the intended command
        command_func(bot, update)

    # give the thing back!
    return _wrapper
