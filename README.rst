kaoru
=========
.. image:: https://badge.fury.io/py/kaoru.svg
   :target: http://badge.fury.io/py/kaoru

[WIP] A Telegram Bot to serve you
-------------------------------------------------------------

**kaoru** is a minimalist python command line tool for easily list
and capture your Softlayer virtual servers into corresponding images with no
effort whatsoever.


-  `Quick start <#quick-start>`_
-  `Requirements <#requirements>`_
-  `Installation <#installation>`_
-  `Basic usage <#basic-usage>`_
-  `Options <#options>`_
-  `Configuration file <#configuration-file>`_
-  `Contributing <#contributing>`_
-  `Donating <#donating>`_
-  `Copyright and licensing <#copyright-and-licensing>`_


Quick start
===========

::

    # First of all, you need to install
    pip3 install kaoru


Requirements
============

-  `python <http://python.org>`_ >= 3.3
-  `clint <https://github.com/kennethreitz/clint>`_
-  `docopt <http://docopt.org>`_
-  `pyyaml <http://pyyaml.org>`_
-  `schema <https://github.com/keleshev/schema>`_


Installation
============

Installation of kaoru can be made directly from source, via `pip <https://github.com/pypa/pip>`_ or
`easy_install <http://pythonhosted.org/setuptools/easy_install.html>`_, whichever you prefer.

Option # 1: pip
---------------
::

    $ pip install kaoru

Option # 2: from source
-----------------------
::

    $ git clone git@github.com:axltxl/kaoru.git
    $ cd kaoru
    $ python3 setup.py install

Option # 3: easy_install
------------------------
::

    $ easy_install kaoru

From this point you can edit your `configuration file <#configuration-file>`_
::

  $ vi /path/to/your/kaoru.conf

Basic Usage
===========
Normal execution
::

    $ kaoru --capture /path/to/my/custom/kaoru.yaml

Dry run
::

    $ kaoru -d


Configuration file
==================

kaoru lists and tells Softlayer to capture images based
on criteria information extracted from a 'criteria file' which is
no more than a dead-simple YAML file with a handful key-value pairs,
like so:

::

    ---
    # Example criteria YAML file
    domain: mydomain.com
    tags: [mydomain, production]
    hourly: false
    monthly: true
    cpus: 2


Options
=======
::

    kaoru [options] (--list | --capture) <config_file>


-  ``--version`` show version number and exit
-  ``-h | --help`` show a help message and exit
-  ``-d | --dry-run`` don't actually do anything
-  ``-q | --quiet`` quiet output
-  ``--ll | --log-level=[num]`` set logging output level
-  ``-l LOG_FILE | --log-file LOG_FILE set log file``


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

Code contributions
------------------

Code contributions (patches, new features) are the most obvious way to help with the project’s development.
Since this is so common we ask you to follow our workflow to most efficiently work with us.
For code contributions, we follow the "fork-and-pull" Git workflow.


1. Fork, then clone your repo on GitHub
::

  git clone git@github.com:your-username/kaoru.git
  git add origin upstream https://github.com/axltxl/kaoru.git

If you already forked the repo, then be sure to merge
the most recent changes from "upstream" before making a pull request.
::

  git pull upstream

2. Create a new feature branch in your local repo
::

  git checkout -b my_feature_branch

3. Make your changes, then make sure the tests passes
::

  pyvenv kaoru-pyve && source kaoru-pyve/bin/activate
  python3 setup.py test

4. Commit your changes once done
::

  git commit -a -m "My commit message"
  git push origin my_feature_branch

5. Submit a `pull request <https://github.com/axltxl/kaoru/compare/>`_ with your feature branch containing your changes.


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
