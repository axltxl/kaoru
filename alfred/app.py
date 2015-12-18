# -*- coding: utf-8 -*-

"""
alfred.app
~~~~~~~~

Main module

:copyright: (c) 2015 by Alejandro Ricoveri
:license: MIT, see LICENSE for more details.

"""

import sys
import traceback
import os
import signal
import time
from telegram import Updater
from docopt import docopt

from . import __version__ as version
from . import PKG_URL as pkg_url
from . import __name__ as pkg_name
from . import log
from . import command
from . import config


def init(argv):
    """Usage: alfred [--log-level LVL] [--log-file FILE] [--dry-run]

    --log-level LVL  Verbosity level on output [default: 1]
    --log-file FILE  Log file [default: alfred.log]
    --dry-run        Dry run mode (don't do anything)
    """
    # get token so this bot can use Telegram Bot API
    # TODO: what if this environment variable is not set?
    # TODO: what if a config file could actually handle this?
    config.token = os.getenv('TG_TOKEN')

    args = docopt(init.__doc__, argv=argv[1:], version=version)

    # This baby will handle UNIX signals
    signal.signal(signal.SIGINT, _handle_signal)
    signal.signal(signal.SIGTERM, _handle_signal)

    # initialize log
    if not args['--log-file']:
        args['--log-file'] = log.LOG_FILE_DEFAULT
    log.init(log_file=args['--log-file'],
             threshold_lvl=int(args['--log-level']))

    # show splash
    _splash()

    return args

def handle_except(e):
    """
    Handle (log) any exception

    :param e: exception to be handled
    """
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    log.msg_err("Unhandled {e} at {file}:{line}: '{msg}'" .format(
        e=exc_type.__name__, file=fname,
        line=exc_tb.tb_lineno, msg=e))
    log.msg_err(traceback.format_exc())
    log.msg_err("An error has occurred!. "
                "For more details, review the logs.")
    return 1

##################
# The main "thing"
##################
def start(
        dry_run=False,
        queue_reboot=False,
        queue_poweroff=False,
        time_poweroff=1,
        time_reboot=1
        ):


    # TODO: we'll see about this
    # TODO: config should come from a file
    # Main settings for this module
    config.queue_reboot   = queue_reboot
    config.queue_poweroff = queue_poweroff
    config.time_reboot = time_reboot
    config.time_poweroff = time_poweroff
    config.dry_run = dry_run


    # ... and as well a few other things that are necessary
    updater = Updater(token=config.token)
    dispatcher = updater.dispatcher

    # Register callbacks for each supported command in this bot
    command.register_commands(updater, dispatcher)

    # Start listening for actual requests
    updater.start_polling()

def _handle_signal(signum, frame):
    """
    UNIX signal handler
    """
    # Raise a SystemExit exception
    sys.exit(1)

def shutdown():
    """
    Cleanup
    """
    log.msg("Exiting ...")

def _splash():
    """Print the splash"""
    splash_title = "{pkg} [{version}] - {url}".format(
        pkg=pkg_name, version=version, url=pkg_url)
    log.to_stdout(splash_title, colorf=log.yellow, bold=True)
    log.to_stdout('-' * len(splash_title), colorf=log.yellow, bold=True)

