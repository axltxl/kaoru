# -*- coding: utf-8 -*-

"""
kaoru.procutils
~~~~~~~~

Utilities for executing external processes

:copyright: (c) 2015 by Alejandro Ricoveri
:license: MIT, see LICENSE for more details.

"""

import envoy

from . import log
from . import config


def _proc_exec(exec_func):
    """Run a process, asynchronously"""

    def _exec_func(cmd):
        log.msg_debug("exec: {}".format(cmd))
        if not config.get('dry_run'):
            return exec_func(cmd)
        return None
    return _exec_func

@_proc_exec
def proc_exec_async(cmd):
    """Run a process, asynchronously"""

    envoy.connect(cmd)
    return None

@_proc_exec
def proc_exec(cmd):
    """Run a process, synchronously"""

    return envoy.run(cmd)

def proc_select(exec_list):
    """Select the first executable found from a list

    Select the preferred executable for a command, if user_exec is None,
    this will check for every executable in exec_list in PATH.
    If none is found, it will return None

    :param exec_list: list of executable nominees
    """

    # if the user didn't select any particular
    # executable for a command, it'll be selected from
    # exec_list
    for prog in exec_list:
        r = envoy.run("which {}".format(prog))
        if r.status_code == 0:
            return r.std_out[:-1]
    return None
