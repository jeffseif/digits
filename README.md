# digits

A digit classifier

## Package

### Installation

    > pip install -e git+https://github.com/jeffseif/digits.git#egg=digits

### Development

    > git clone git@github.com:jeffseif/digits.git
    > cd digits
    > make test

### Example invocation

    > ./scripts/digits.sh --help
    usage: main.py [-h] [--version] [-v] {train,classify} ...

    A digit classifier

    positional arguments:
      {train,classify}  Additional help
        train           Train the digit classifier
        classify        Train the digit classifier

    optional arguments:
      -h, --help        show this help message and exit
      --version         show program's version number and exit
      -v, --verbose     Increase output verbosity

    Version 1.0.0 | Jeffrey Seifried 2016

    > ./scripts/digits.sh train
    Loading corpus ...
    ... done!
    Flattening features ...
    ... done!
    Training ...
    ... done!
    Scoring ...
    ... done; F1 score: 96.39%
    Serializing to model.pkl ...
    ... done!

    > ./scripts/digits.sh classify /path/to/eight.png
    Deserializing from model.pkl ...
    ... done!
    Digit is 8
