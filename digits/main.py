#! /usr/bin/env python3
import numpy
import scipy
import sklearn

from digits import __author__
from digits import __description__
from digits import __version__
from digits import __year__


def main():
    import argparse

    __version__author__year__ = '{} | {} {}'.format(
        __version__,
        __author__,
        __year__,
    )

    parser = argparse.ArgumentParser(
        description=__description__,
        epilog='Version {}'.format(__version__author__year__),
    )
    parser.add_argument(
        '--version',
        action='version',
        version='%(prog)s {}'.format(__version__author__year__),
    )
    parser.add_argument(
        '-v',
        '--verbose',
        action='count',
        default=0,
        help='Increase output verbosity',
    )
    args = parser.parse_args()


if __name__ == '__main__':
    import sys
    sys.exit(main())
