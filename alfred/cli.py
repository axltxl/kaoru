# -*- coding: utf-8 -*-

"""
alfred.cli
~~~~~~~~

Command line interface

:copyright: (c) 2015 by Alejandro Ricoveri
:license: MIT, see LICENSE for more details.

"""

from clint.textui import puts
from clint.textui.colored import red, cyan
from clint.textui.prompt import query

from . import command
from . import config

def _prompt_str(botname):
    """Print prompt string"""

    return str(cyan('{}>'.format(botname), bold=True))

def _cli_help(commands):
    puts(cyan("Available commands are:"))
    for cmd, desc, handler in commands:
        puts(cyan("* {} - {}".format(cmd, desc)))

def prompt_loop(dispatcher, update_queue):
    """Command line interface for the user"""

    puts(red("Entering CLI"))
    puts(red('Type "help" to get a list of available commands'))

    while True:
        # prompt the user for input
        cmd = query(_prompt_str(dispatcher.bot.username))

        # and then see what command came out of it
        if cmd == 'help':
            _cli_help(command.get_list())
            continue
        if cmd == 'quit':
            # Gracefully stop the event handler
            break

        # else, put the text into the update queue
        elif len(cmd ) > 0:
            update_queue.put(cmd )  # Put command into queue

