import sys
import os
import json
import argparse
from .view import View


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

    # Parse arguments
    options = p.parse_args(sys.argv[1:])

    # If the user asked for the version,
    # print the version number and exit.
    if options.version:
        from . import _program, __version__
        print(_program, __version__)
        sys.exit(0)

    v = View(options)
    v.show()


if __name__ == '__main__':
    main()
