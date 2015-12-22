# -*- coding: utf-8 -*-

"""
kaoru.commands.hello
~~~~~~~~

/hello command implementation

:copyright: (c) 2015 by Alejandro Ricoveri
:license: MIT, see LICENSE for more details.

"""

from telegram import Update
from .. import utils
from . import bot_command

_greetings = [
    # English
    'Affirmative Dave, I read you',
    'Hello world!',

    # Spanish
    'Hola',

    # Arabic
    'أهلاً و سهلاً',

    # Mandarin
    '你好',

    # Corsican
    'Salute',

    # French
    'Salut', 'Bonjour!, est-ce que vous allez bien?',

    # Danish
    'Hej',

    # German
    'Hallo',
    'Guten tag!',

    # Italian
    'Ciao',

    # Japanese
    '今日は',

    # Klingon
    'nuqneH',

    # Farsi
    'سلام',

    # Turkish
    'Merhaba',
]

# /hello command
@bot_command
def _cmd_handler(bot, update):
    """a rather simple ping command"""

    if isinstance(update, Update):
        utils.echo_msg( bot, update, utils.select_rand_str(_greetings))
    else:
        utils.echo_msg(bot, update, utils.select_rand_str(_greetings))

desc = 'See if I "live"'  # This command's description
cmd_handler = _cmd_handler  # command handler
cmd_str = 'hello'  # command /string
