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
    subparsers = parser.add_subparsers(help='Additional help')

    # Train
    train_parser = subparsers.add_parser(
        'train',
        help='Train the digit classifier',
    )
    train_parser.add_argument(
        '--model-filename',
        default=DEFAULT_MODEL_FILENAME,
        help='Where to serialize to',
    )
    train_parser.add_argument(
        '--show-score',
        action='store_true',
        default=False,
        help='Show F1 score',
    )
    train_parser.set_defaults(func=train)

    # Classify
    classify_parser = subparsers.add_parser(
        'classify', 
        help='Train the digit classifier',
    )
    classify_parser.add_argument(
        'path_to_image',
        default=DEFAULT_MODEL_FILENAME,
        help='The image to classify',
    )
    classify_parser.add_argument(
        '--model-filename',
        default=DEFAULT_MODEL_FILENAME,
        help='Where to deserialize from',
    )
    classify_parser.set_defaults(func=classify)

    args = parser.parse_args()
    args.func(args)


def train(args):
    Model() \
        .train(args.show_score) \
        .save(args.model_filename)


def classify(args):
    digit = Model() \
        .load(args.model_filename) \
        .classify_image(args.path_to_image)
    print('Digit is {}'.format(digit))


if __name__ == '__main__':
    import sys
    sys.exit(main())
