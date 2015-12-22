# -*- coding: utf-8 -*-

"""
kaoru.commands.screenshot
~~~~~~~~

/screenshot command implementation

:copyright: (c) 2015 by Alejandro Ricoveri
:license: MIT, see LICENSE for more details.

"""
import os
import uuid
import re
from telegram import Update, ChatAction

from .. import utils
from .. import config
from .. import log
from . import bot_command
from ..procutils import proc_exec, proc_select

# a fun list of replies to the user
_replies = [
    'Here you go, Sir.',
    'Le voilà, Monsieur.',
    'As you wish.',
    'Sus deseos son órdenes para mi, mi Señor.'
]

# /screenshot command:
@bot_command
def _cmd_handler(bot, update):
    """
    it basically takes a screen shot
    """

    # check for executables set for commands
    screenshot_exec = proc_select(['import', 'scrot'])

    # file name is set without extension at first, depending on the
    # program being selected for the job, an extension will be chosen
    screenshot_file = "/tmp/{}".format(uuid.uuid4().hex)

    # screen shot quality (for jpeg)
    screenshot_jpeg_quality = 60

    # for the moment, there is only support
    # for scrot as the screenshooter

    # imagemagick
    if re.match('.*import$', screenshot_exec):
        screenshot_file += '.jpg'
        screenshot_exec = "{} -window root -quality {} {}".format(
            screenshot_exec,
            screenshot_jpeg_quality,
            screenshot_file
        )
    # scrot
    elif re.match('.*scrot$', screenshot_exec):
        screenshot_file += '.jpg'
        screenshot_exec = "{} -q {} {}".format(
            screenshot_exec,
            screenshot_jpeg_quality,
            screenshot_file
        )
    else:
        log.msg_err("No screenshot backend has been found!")

    # execute the thing
    if screenshot_exec is not None:
        bot.sendChatAction(
            chat_id=update.message.chat_id,
            action=ChatAction.UPLOAD_PHOTO
        )
        proc_exec(screenshot_exec)

    # check is the file is available
    if os.path.isfile(screenshot_file):
        if isinstance(update, Update):
            with open(screenshot_file, 'rb') as photo:
                log.msg_debug("{}: {} byte(s)".format(
                    screenshot_file,
                    os.path.getsize(screenshot_file)
                ))
                log.msg_debug("{}: sending picture".format(screenshot_file))
                # send the actual pic
                bot.sendPhoto(
                    photo=photo,
                    chat_id=update.message.chat_id,
                    caption=utils.select_rand_str(_replies)
                )
                log.msg_debug("{}: picture sent".format(screenshot_file))
    else:
        utils.echo_msg(
            bot, update,
            "I am sorry, I have been unable "
            "to generate that screenshot you wished."
        )

desc = 'Get a screen shot from your host(s)'  # This command's description
cmd_handler = _cmd_handler  # command handler
cmd_str = 'screenshot'  # command /string
