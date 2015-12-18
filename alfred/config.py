# -*- coding: utf-8 -*-

"""
alfred.config
~~~~~~~~

Configuration goes in here

:copyright: (c) 2015 by Alejandro Ricoveri
:license: MIT, see LICENSE for more details.

"""

import yaml
from schema import Schema, Optional

from . import log

# Default set of options
_options = {
    'token': None,
    'queue_reboot': False,
    'queue_poweroff': False,
    'time_reboot': 1,
    'time_poweroff': 1,
    'dry_run': False
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
        Optional('dry_run'): bool,
        Optional('time_reboot'): int,
        Optional('time_poweroff'): int,
        })

    # Load YAML file and validate it
    try:
        with open(config_file, "r") as file:
            data = _schema.validate(yaml.load(file))
            for key, value in data.items():
                # overwrite defaults with values taken
                # from the configuration file
                if key in _options:
                    _options[key] = value
    except FileNotFoundError as fnfe:
        log.msg_warn(
            '{}: configuration file not found, '
            'proceeding with default values'.format(config_file)
        )

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

