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
    license = \
    """
*Copyright (c) Alejandro Ricoveri*

``` The MIT License (MIT)
Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.```
    """.strip()


    about_str = \
    """
*{name} - v{version}*
{url}
{license}
    """.format(
    name=pkg_name,
    url=pkg_url,
    version=pkg_version,
    license=license
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
