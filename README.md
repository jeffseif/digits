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
    usage: main.py [-h] [--version] {train,classify} ...

    A digit classifier

    positional arguments:
      {train,classify}
        train           Train the digit classifier
        classify        Classify an image

    optional arguments:
      -h, --help        show this help message and exit
      --version         show program's version number and exit

    Version 1.0.0 | Jeffrey Seifried 2016

    > ./scripts/digits.sh train --verbose --validate
    INFO:digits:Building corpus ...
    INFO:digits:... done!
    INFO:digits:Featurizing corpus ...
    INFO:digits:... done!
    INFO:digits:Training classifier ...
    INFO:digits:... done!
    INFO:digits:Validating classifier ...
    INFO:digits:... done; F1 score: 96.39%
    INFO:digits:Serializing to model.pkl ...
    INFO:digits:... done!

    > ./scripts/digits.sh classify /path/to/eight.png
    INFO:digits:Deserializing from model.pkl ...
    INFO:digits:... done!
    INFO:digits:Featurizing /path/to/eight.png
    INFO:digits:... done!
    INFO:digits:Classifying ...
    INFO:digits:... done!
    Digit is 8
