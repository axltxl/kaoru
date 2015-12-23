# -*- coding: utf-8 -*-

"""
kaoru.commands.about
~~~~~~~~

/about command implementation

:copyright: (c) 2015 by Alejandro Ricoveri
:license: MIT, see LICENSE for more details.

"""

from telegram import ParseMode
from .. import __version__ as pkg_version
from .. import PKG_URL as pkg_url
from .. import __name__ as pkg_name
from .. import __author__ as pkg_author
from .. import __copyright__ as pkg_copyright
from .. import config
from .. import utils
from . import bot_command

# /about command
@bot_command
def _cmd_handler(bot, update):
    """command handler"""

    # the about string
    about_str = \
    """
*{name} - v{version}*
{url}
    """.format(
    name=pkg_name,
    url=pkg_url,
    version=pkg_version,
    ).strip()

    # send the actual message
    utils.echo_msg(bot, update,
        about_str,
        parse_mode=ParseMode.MARKDOWN,
        disable_web_page_preview=True
    )

desc = 'Information for nerds'  # This command's description
cmd_handler = _cmd_handler  # command handler
cmd_str = 'about'  # command /string
