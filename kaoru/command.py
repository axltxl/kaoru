# -*- coding: utf-8 -*-

"""
kaoru.commands
~~~~~~~~

Command handlers

:copyright: (c) 2015 by Alejandro Ricoveri
:license: MIT, see LICENSE for more details.

"""

from . import log
from .commands import (
    about,
    start,
    hello,
    help,
    screenlock,
    screenshot,
    dryrun,
    cancel,
    poweroff,
    suspend,
    hibernate,
    reboot,
    unknown,
)

# list of available commands
_commands = [
    (about.cmd_str, about.desc, about.cmd_handler),
    (start.cmd_str, start.desc, start.cmd_handler),
    (hello.cmd_str, hello.desc, hello.cmd_handler),
    (help.cmd_str, help.desc, help.cmd_handler),
    (screenlock.cmd_str, screenlock.desc, screenlock.cmd_handler),
    (screenshot.cmd_str, screenshot.desc, screenshot.cmd_handler),
    (dryrun.cmd_str, dryrun.desc, dryrun.cmd_handler),
    (cancel.cmd_str, cancel.desc, cancel.cmd_handler),
    (reboot.cmd_str, reboot.desc, reboot.cmd_handler),
    (poweroff.cmd_str, poweroff.desc, poweroff.cmd_handler),
    (suspend.cmd_str, suspend.desc, suspend.cmd_handler),
    (hibernate.cmd_str, hibernate.desc, hibernate.cmd_handler),
]

# set cmd list to be used by /help command
help.cmd_list = _commands

def _print_cmd_desc(commands):
    """Print command descriptions"""
    log.msg_warn("You will need to register my commands with my @BotFather")
    log.msg_warn("Ask him to /setcommands and after you")
    log.msg_warn("have mentioned me, you can paste the following:")
    log.msg("")
    for command, desc, handler in commands:
        print("{} - {}".format(command, desc))
    log.msg("")

def get_list():
    """List of available commands"""

    return _commands

def register_commands(updater, dispatcher):
    """register each and every command this bot is going to process"""

    # register every command there is
    for command, desc, handler in _commands:
        dispatcher.addTelegramCommandHandler(command, handler)
        dispatcher.addStringCommandHandler(command, handler)
        log.msg_debug("/{}: command registered".format(command))

    # and the default one as well ...
    log.msg_debug('Registering default handlers')
    dispatcher.addUnknownTelegramCommandHandler(unknown.cmd_handler)

    # print command descriptions
    _print_cmd_desc(_commands)

