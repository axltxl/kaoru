kaoru
=====

.. image:: https://badge.fury.io/py/kaoru.svg
    :target: http://badge.fury.io/py/kaoru

[WIP] A Telegram Bot as your personal IoT assistant
---------------------------------------------------

**kaoru** can be defined as a Telegram Bot whose roles are much alike
to those related to IoT personal assistant.

OK, I think I get the idea, but what is it good for?
----------------------------------------------------

**kaoru**'s purpose in life is to make your life a little bit easier by
allowing you remote control of certain things on your host(s), the rationale
behind this is that there could be moments in which you would need to perform
administrative tasks on either your office or home laptop, things that you
maybe forgot to do, or things you could only do by getting in front of them.
An IoT-like approach would be ideal on this scenario, namely, talk to your
machines and tell them to do stuff for you while you're walking streets,
or having a dinner with your friend, or when you're just too sleepy/lazy
to get up from your couch/bed.

For the moment, **kaoru** is capable of:

-  Rebooting your host(s)
-  Shutting down your host(s)
-  Locking the screen on your host(s)
-  Send screen shots from your host(s)

Things I feel tempted to implement:

-  Suspend to RAM/disk.
-  Tell your host(s) to send you a file in their file system.
-  Perform a ``tail`` on a file and send messages as new content is appended to that file.

Wait, what?, bots are sort-of public domain, you know?
------------------------------------------------------

While that's true, the fact is that having your host running **kaoru**
means that you have control over *her*, including (but not limited) to
control which people she's going to listen to, as explained in `Security <#security>`_.

OK, I get it, how do I use this?, I just wanna get hands-on this "thing" ...
----------------------------------------------------------------------------

Well, the most essential thing you will need is to tell `@BotFather <http://telegram.me/botfather>`_ to
make a new bot for you, as specified in `Telegram Bots Documentation <https://core.telegram.org/bots>`_

On the other hand, you gotta install **kaoru**, of course.

.. code-block:: bash

    # First of all, you need to install
    pip3 install kaoru

A Telegram Bot is a just a dummy client with no cell phone attached to it,
you need something to control this bot so it can become active, and that's when
**kaoru** comes into play.

Make sure you have properly set up your brand new Telegram Bot, `@BotFather <http://telegram.me/botfather>`_
should have given you an **API access token** (a bunch of characters and numbers),
**kaoru** needs this token in order for her to do her magic.

Moreover, you can edit your `configuration file <#configuration-file>`_ from this point

.. code-block:: bash

    $ vi /path/to/your/kaoru.conf

**NOTE**: A configuration file is *not mandatory* for **kaoru** to run, she can do
it using her defaults, however, you will need at least to set the API token
through the environment variable ``TG_TOKEN``

**Now you are done setting up kaoru, now is time to run it!**

.. code-block:: bash

    $ kaoru --config /path/to/you/kaoru.conf

    kaoru [version] - https://github.com/axltxl/kaoru
    -------------------------------------------------
    --- Reading configuration file at: asd.conf
    (!) Strict mode has been enforced!
    (!) You will need to register my commands with my @BotFather
    (!) Ask him to /setcommands and after you
    (!) have mentioned me, you can paste the following:
    ---
    hello - See if I "live"
    screenlock - Lock the screen(s) on your host(s)
    screenshot - Get a screen shot from your host(s)
    reboot - Reboot your host(s)
    poweroff - Shut down your host(s)
    cancel - Cancel any pending operation(s)
    dryrun - Toggle "dry run" mode
    ---
    --- Waiting for updates ...

**NOTE**: bear in mind that **you have to register kaoru's commands for your bot**
with the `@BotFather <http://telegram.me/botfather>`_, **kaoru** will tell you how.

**So, I have everything set up. What commands are available on this bot?**

Good question indeed!, the following is the current set of commands
supported by **kaoru**, more are planned to come:


-  ``/hello`` A simple ping just to see if your bot is *alive*
-  ``/screenlock`` Lock screens on your host(s)
-  ``/screenshot`` Get a screen shot from your host(s)
-  ``/poweroff`` Tell your host(s) to shut down
-  ``/reboot`` Tell your host(s) to reboot
-  ``/cancel`` Cancel any pending operations
-  ``/dryrun`` don't do a thing, but pretend


Are there any sort of requirements for kaoru in order to work properly?
-----------------------------------------------------------------------

Yes indeed. For the moment, **kaoru** is only working under certain
conditions. Hosts running **kaoru** must:


-  Be Linux-based at least (though conceptually speaking, ``*nix`` should be supported)
-  Have ``sudo``. Since commands like ``shutdown`` need to be run as ``root``.
-  Have either `scrot <http://freecode.com/projects/scrot>`_ or `imagemagick <http://imagemagick.org>`_ installed (if you want ``/screenshot`` command to work)
-  Run kaoru on behalf on an user whose ``sudo`` privileges cover at least the execution of ``shutdown`` with no password requirement.

Configuration file
==================

**kaoru** lists all sorts of configuration directives inside a YAML
configuration file. These directives range from essentials like
a Telegram Bot API token to those related with blablabla. Please refer
to the `example configuration file <https://github.com/axltxl/kaoru/blob/develop/example.conf>`_
for more details on how to configure **kaoru**.

.. code-block:: yaml

    ---
    ############################
    # Example configuration file
    ############################

    # Telegram Bot API access token
    token: 1XXXXXXXXXXXX:XXXXXXXXXXXXXXXXXXXXXXX

    # shutdown the host 2 minutes after a /poweroff command has been received
    poweroff_delay: 2

    # command to execute when a /screenlock command has been received
    screenlock_cmd: xscreensaver


**NOTE**: Configuration files can be read by **kaoru** using the ``--config``
argument, by default, **kaoru** will look up for a configuration file on
``~/.config/kaoru/kaoru.conf``


Security
========

By default, **kaoru** runs openly, namely, it will listen to *any incoming
updates from any user* wanting to communicate with her, while this would allow you
to quickly see her working, **it is inherently and by all means INSECURE!!!!**

Once you feel happy with your configuration, it is strongly advised
that you **enforce strict mode** on your configuration file, like so:

.. code-block:: yaml

    ---
    # .. other options are behind

    # enforce strict mode
    strict: true

    # The following are the users who can talk
    # to kaoru. Requests coming from users outside
    # this list are simply IGNORED.
    masters:
        - <your Telegram user name>
        - betty # your friend betty can also talk to kaoru


Once you're done, you can proceed to re-execute **kaoru**.
With ``strict`` directive set to ``true``, **kaoru** will only
listen and react to commands and messages coming from users set in ``masters``.


Options
=======
.. code-block:: bash

    kaoru [options]


-  ``--version`` show version number and exit
-  ``-i | --interactive`` enter CLI mode
-  ``-c FILE | --config FILE`` configuration file to use
-  ``-h | --help`` show a help message and exit
-  ``-d | --dry-run`` don't actually do anything
-  ``L NUM | --log-level NUM`` set logging output level
-  ``-l FILE | --log-file LOG_FILE`` set log file


Contributing
============

There are many ways in which you can contribute to kaoru.
Code patches are just one thing amongst others that you can submit to help the project.
We also welcome feedback, bug reports, feature requests, documentation improvements,
advertisement and testing.

Feedback contributions
----------------------

This is by far the easiest way to contribute something.
If you’re using kaoru for your own benefit, don’t hesitate sharing.
Feel free to `submit issues and enhancement requests. <https://github.com/axltxl/kaoru/issues>`_

Copyright and Licensing
=======================

Copyright (c) Alejandro Ricoveri

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be included
in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
