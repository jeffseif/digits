#! /usr/bin/env python3
from digits import __author__
from digits import __description__
from digits import __version__
from digits import __year__
from digits import DEFAULT_MODEL_FILENAME
from digits.model import Model


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
    parser.add_argument(
        '--model-filename',
        default=DEFAULT_MODEL_FILENAME,
        help='Path to classifier serialization',
    )
    parser.add_argument(
        '--show-score',
        action='store_true',
        default=False,
        help='Show classifier F1 score',
    )
    parser.add_argument(
        'mode',
        choices=(
            'load',
            'train',
        ),
    )
    args = parser.parse_args()

    if args.mode == 'train':
        Model(args).train()
    elif args.mode == 'load':
        Model(args).load()


if __name__ == '__main__':
    import sys
    sys.exit(main())
