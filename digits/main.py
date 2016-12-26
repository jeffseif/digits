from digits import __author__
from digits import __description__
from digits import __version__
from digits import __year__
from digits import DEFAULT_MODEL_FILENAME
from digits.logger import set_logging_verbosity
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
    subparsers = parser.add_subparsers()

    # Parent
    parent = argparse.ArgumentParser(add_help=False)
    parent.add_argument(
        '-v',
        '--verbose',
        action='count',
        default=0,
        help='Increase output verbosity',
    )
    parent.add_argument(
        '--model-filename',
        default=DEFAULT_MODEL_FILENAME,
        help='Where to serialize to',
    )
    parents = (parent,)

    # Train
    train_parser = subparsers.add_parser(
        'train',
        parents=parents,
        help='Train the digit classifier',
    )
    train_parser.add_argument(
        '--validate',
        action='store_true',
        default=False,
        help='Show F1 score',
    )
    train_parser.set_defaults(func=train)

    # Classify
    classify_parser = subparsers.add_parser(
        'classify', 
        parents=parents,
        help='Classify an image',
    )
    classify_parser.add_argument(
        'path_to_image',
        default=DEFAULT_MODEL_FILENAME,
        help='The image to classify',
    )
    classify_parser.set_defaults(func=classify)

    args = parser.parse_args()
    set_logging_verbosity(args.verbose)
    if hasattr(args, 'func'):
        args.func(args)


def train(args):
    Model() \
        .train(args.validate) \
        .save(args.model_filename)


def train_model_for_setup_dot_py():
    Model() \
        .train() \
        .save()


def classify(args):
    digit = Model() \
        .load(args.model_filename) \
        .classify_image(args.path_to_image)
    print('Digit is {}'.format(digit))


if __name__ == '__main__':
    import sys
    sys.exit(main())
