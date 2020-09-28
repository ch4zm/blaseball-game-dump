import sys
import os
import json
import argparse
from .view import View
from .util import CaptureStdout

def main(sysargs = sys.argv[1:]):

    p = argparse.ArgumentParser()

    p.add_argument('-v',
                   '--version',
                   required=False,
                   default=False,
                   action='store_true',
                   help='Print program name and version number and exit')

    p.add_argument('game_id',
                   help='Specify the game ID of the game to summarize (repeat flag to specify multiple game IDs)')

    # -----

    # Print help, if no arguments provided
    if len(sysargs)==0:
        p.print_help()
        exit(0)
    elif '-v' in sysargs or '--version' in sysargs:
        # If the user asked for the version,
        # print the version number and exit.
        # (Note: this is done separate from
        # argparse, because otherwise the user
        # has to ALSO provide a game ID to get
        # the --version flag to work. ugh.)
        from . import _program, __version__
        print(_program, __version__)
        sys.exit(0)

    # Parse arguments
    options = p.parse_args(sysargs)

    v = View(options)
    v.show()


def game_dump(sysargs):
    with CaptureStdout() as so:
        main(sysargs)
    return str(so)


if __name__ == '__main__':
    main()
