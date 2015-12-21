# -*- coding: utf-8 -*-

"""
kaoru.__main__
~~~~~~~~

Main entry point

:copyright: (c) 2015 by Alejandro Ricoveri
:license: MIT, see LICENSE for more details.

"""

import sys

from docopt import DocoptExit

from kaoru.app import handle_except, init, shutdown, start

def main(argv=None):
    """
    This is the main thread of execution

    :param argv: list of command line arguments
    """
    # Exit code
    exit_code = 0

    # First, we change main() to take an optional 'argv'
    # argument, which allows us to call it from the interactive
    # Python prompt
    if argv is None:
        argv = sys.argv

    try:
        # Bootstrap
        options = init(argv)

        # start the thing!
        start()

    except DocoptExit as dexcept:
        # Deal with wrong arguments
        print(dexcept)
        exit_code = 1
    except Exception as e:
        # ... and if everything else fails
        handle_except(e)
        exit_code = 1
    finally:
        # All cleanup actions are taken from here
        shutdown()
    return exit_code


# Now the sys.exit() calls are annoying: when main() calls
# sys.exit(), your interactive Python interpreter will exit!.
# The remedy is to let main()'s return value specify the
# exit status.
if __name__ == '__main__':
    sys.exit(main())
