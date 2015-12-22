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

def proc_select(exec_list, *, user_exec=None, command):
    """Select the first executable found from a list

    Select the preferred executable for a command, if user_exec is None,
    this will check for every executable in exec_list in PATH.
    If none is found, it will return None

    :param exec_list: list of executable nominees
    :param user_exec: user selection for the executable used for a command
    :param command: command associated with selected executable

    """

    # selected executable
    selected_exec = None

    # user_exec is first class citizen
    if user_exec is not None:
        selected_exec = user_exec

    # if the user didn't select any particular
    # executable for a command, it'll be selected from
    # exec_list
    if selected_exec is None:
        for prog in exec_list:
            r = envoy.run("which {}".format(prog))
            if r.status_code == 0:
                selected_exec = r.std_out[:-1]
                break

    log.msg_debug("[{}] executable for this command is: {}".format(command, selected_exec))
    return selected_exec
