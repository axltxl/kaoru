# -*- coding: utf-8 -*-

"""
kaoru.commands.dryrun
~~~~~~~~

/dryrun command implementation

:copyright: (c) 2015 by Alejandro Ricoveri
:license: MIT, see LICENSE for more details.

"""

from .. import config
from .. import utils
from . import bot_command

# /dryrun command
@bot_command
def _cmd_handler(bot, update):
    """toggle dry run mode"""
    config.set('dry_run', not config.get('dry_run'))
    if config.get('dry_run'):
        status = "ON"
    else:
        status = "OFF"
    utils.echo_msg(bot, update, "Dry run mode is {}".format(status))

desc = 'Toggle "dry run" mode'  # This command's description
cmd_handler = _cmd_handler  # command handler
cmd_str = 'dryrun'  # command /string
