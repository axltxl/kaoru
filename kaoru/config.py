# -*- coding: utf-8 -*-

"""
kaoru.config
~~~~~~~~

Configuration goes in here

:copyright: (c) 2015 by Alejandro Ricoveri
:license: MIT, see LICENSE for more details.

"""

import yaml
from schema import Schema, Optional, And

from . import log

# Default set of options
_options = {
    'token': None,
    'queue_reboot': False,
    'queue_poweroff': False,
    'discard_on_startup': True,
    'reboot_delay': 0,
    'poweroff_delay': 0,
    'screenlock_cmd': None,
    'dry_run': False,
    'strict': False,
    'masters': [],
    'show_hostname': False,
    'cli': False,
}
_schema = None


def init(*, config_file):
    """Configuration file

    Its role's very simple, to load
    a YAML file, validate it and from there
    set options to be used by this program

    :param config_file: path to configuration file
    """

    global _schema
    global _options

    # Validation schema for each option
    _schema = Schema({
        Optional('token'): str,
        Optional('strict'): bool,
        Optional('discard_on_startup'): bool,
        Optional('masters'): lambda x: isinstance(x,list) and all([isinstance(y,str) for y in x]),
        Optional('dry_run'): bool,
        Optional('show_hostname'): bool,
        Optional('reboot_delay'): int,
        Optional('screenlock_cmd'): str,
        Optional('poweroff_delay'): int,
        })

    # Load YAML file and validate it
    try:
        with open(config_file, "r") as file:
            data = _schema.validate(yaml.load(file))
            for key, value in data.items():
                # overwrite defaults with values taken
                # from the configuration file
                _list_merge(data, _options)
    except FileNotFoundError as fnfe:
        log.msg_warn(
            '{}: configuration file not found, '
            'proceeding with default values'.format(config_file)
        )


def _list_merge(src, dest):
    """
    Merge the contents coming from src into dest

    :param src: source dictionary
    :param dest: destination dictionary
    """
    for k in src:
        if type(src[k]) != dict:
            dest[k] = src[k]
        else:
            # ---
            # src could have a key whose value is a list
            # and does not yet exist on dest
            if k not in dest:
                dest[k] = {}
            _list_merge(src[k], dest[k])

def options():
    """Get the whole options set"""
    return _options

def get(key):
    if key in _options:
        return _options[key]
    return None

def set(key, value):
    global _options
    if key in _options:
        _options[key] = value

