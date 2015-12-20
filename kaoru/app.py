# -*- coding: utf-8 -*-

"""
kaoru.app
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
from . import security
from . import cli

# telegram objects to be used
_tg_dispatcher = None
_tg_updater = None

##################################################
# Configuration file defaults
# default config directory should be XDG-compliant
##################################################
_config_dir_default = "{}/.config/{}".format(os.getenv('HOME'), pkg_name)
_config_file_default = "{}.conf".format(pkg_name)

def _config_init(config_file):
    """Initialise the configuration file"""

    # Create configuration directory if it does not exist
    if not os.path.exists(_config_dir_default):
        log.msg_warn(
            "Configuration directory '{}' does not exist, creating it ..."
            .format(_config_dir_default)
        )
        # create the actual default configuration directory
        os.makedirs(_config_dir_default)

    if config_file is None:
        config_file = "{}/{}".format(_config_dir_default, _config_file_default)
    log.msg("Reading configuration file at: {}".format(config_file))
    config.init(config_file=config_file)

    #########################################################
    # Telegram Bot API token:
    # It can be obtained by either via the configuration file
    # or the environment variable TG_TOKEN
    #########################################################
    if config.get('token') is None:
        token = os.getenv('TG_TOKEN')
        if token is None:
            raise SystemError('A Telegram Bot API token is mandatory for this thing to work!')
        else:
            log.msg_debug('got Telegram Bot API token from environment variable')
        config.set('token', token)
    else:
        log.msg_debug('got Telegram Bot API token from configuration file')

    # print final configuration
    log.msg_debug("Configuration settings are the following:")
    log.msg_debug("-----------------------------------------")
    cfg_opts = config.options().copy()
    # mangle token before showing it off
    token = cfg_opts['token']
    mangled_token = '*' * (len(token)//2)
    mangled_token = "{}{}".format(mangled_token, token[len(token)//2+1:])
    cfg_opts['token'] = mangled_token
    log.msg_debug(cfg_opts)
    log.msg_debug("-----------------------------------------")

def _log_init(log_file, log_lvl):
    """Initialise log file"""

    if not log_file:
        log_file = "{}/{}".format(_config_dir_default, log.LOG_FILE_DEFAULT)
    log.init(log_file=log_file, threshold_lvl=int(log_lvl))

def init(argv):
    """Usage: kaoru [--log-level LVL] [--log-file FILE] [--dry-run] [--config FILE]

    --log-level LVL  Verbosity level on output [default: 1]
    --log-file FILE  Log file
    --config FILE    Configuration file to use
    --dry-run        Dry run mode (don't do anything)
    """

    args = docopt(init.__doc__, argv=argv[1:], version=version)

    # This baby will handle UNIX signals
    signal.signal(signal.SIGINT, _handle_signal)
    signal.signal(signal.SIGTERM, _handle_signal)

    # initialize log
    _log_init(args['--log-file'], args['--log-level'])

    # show splash
    _splash()

    # initialise configuration file
    _config_init(args['--config'])

    # check for strict mode
    if config.get('strict'):
        log.msg_warn("Strict mode has been enforced")
        security.check_masters(config.get('masters'))

    # give back the list of arguments captured by docopt
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

def _handle_error(bot, update, error):
    raise error

##################
# The main "thing"
##################
def start(dry_run=False):

    # whether to set dry run mode
    config.set('dry_run', dry_run)


    # ... and as well a few other things that are necessary
    global _tg_updater, _tg_dispatcher

    #########################
    # create Telegram updater
    #########################
    _tg_updater = Updater(token=config.get('token'))

    # ... and get its dispatcher, which it's manipulated
    # on further code
    _tg_dispatcher = _tg_updater.dispatcher

    ###############
    # error handler
    # TODO: causing errors
    ###############
    # log.msg_debug('Registering error handler')
    # _tg_dispatcher.addErrorHandler(_handle_error)

    # Register callbacks for each supported command in this bot
    command.register_commands(_tg_updater, _tg_dispatcher)

    ####################################
    # Start listening for actual updates
    ####################################
    update_queue = _tg_updater.start_polling(
        poll_interval=0.5,
        timeout=5,
        network_delay=10
    )

    # Mark the beginning of everything
    log.msg("Waiting for updates ...")

    # Start CLI-Loop
    if config.get('cli'):
        cli.prompt_loop(_tg_dispatcher, update_queue)
    else:
        while True:
            time.sleep(1)


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

    # Make sure the updater has stopped
    if _tg_updater is not None:
        log.msg_debug('Stopping updater ..')
        _tg_updater.stop()

    log.msg("Exiting ...")

def _splash():
    """Print the splash"""
    splash_title = "{pkg} [{version}] - {url}".format(
        pkg=pkg_name, version=version, url=pkg_url)
    log.to_stdout(splash_title, colorf=log.yellow, bold=True)
    log.to_stdout('-' * len(splash_title), colorf=log.yellow, bold=True)

