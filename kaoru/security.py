# -*- coding: utf-8 -*-

"""
kaoru.security
~~~~~~~~

Security routines

:copyright: (c) 2015 by Alejandro Ricoveri
:license: MIT, see LICENSE for more details.

"""

from . import log
from . import config

class SecurityException(Exception):
    """Standard security exception"""
    pass

def check_masters(masters):
    if not len(masters):
        log.msg_warn("I have no master(s), I will only listen through console input (if set to true)")

def check_update(update):
    """Perform sanity checks on update"""

    # check whether the update comes from
    # one of my 'masters'
    if config.get('strict'):
        username = update.message.from_user.username
        command = update.message.text
        if not username in config.get('masters'):
            raise SecurityException("Unauthorized user '{}' attempted to run a command: {}".format(username, command))
