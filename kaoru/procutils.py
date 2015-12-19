# -*- coding: utf-8 -*-

"""
kaoru.executor
~~~~~~~~

Utilities for executing external processes

:copyright: (c) 2015 by Alejandro Ricoveri
:license: MIT, see LICENSE for more details.

"""

import envoy

from . import log
from . import config

def proc_exec(cmd):
    """Run a process, asynchronously"""

    log.msg_debug("exec: {}".format(cmd))
    if not config.get('dry_run'):
        envoy.connect(cmd)
