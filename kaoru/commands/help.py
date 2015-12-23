# -*- coding: utf-8 -*-

"""
kaoru.commands.help
~~~~~~~~

/help command implementation

:copyright: (c) 2015 by Alejandro Ricoveri
:license: MIT, see LICENSE for more details.

"""

from telegram import ParseMode
from .. import __version__ as pkg_version
from .. import PKG_URL as pkg_url
from .. import __name__ as pkg_name
from .. import __author__ as pkg_author
from .. import __copyright__ as pkg_copyright
from .. import config
from .. import utils
from . import bot_command


# /help command
@bot_command
def _cmd_handler(bot, update):
    # First of all, grab the current list of commands
    # and format them to Markdown
    commands = ""
    for command, desc, handler in cmd_list:
        commands += "/{} - {}\n".format(command, desc)

    # ... and construct the final markdown string for help
    help_str = \
    """
*The following is the list of available commands I have:*
---
{}
    """.format(commands).strip()

    # send the thing
    utils.echo_msg(bot, update, help_str, parse_mode=ParseMode.MARKDOWN)

cmd_list = None  #
desc = 'Get list of available commands'  # This command's description
cmd_handler = _cmd_handler  # command handler
cmd_str = 'help'  # command /string
