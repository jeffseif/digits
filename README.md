# digits

A digit classifier

Printed digits for the numbers `0` through `9` are extracted from [The Chars74K dataset](http://www.ee.surrey.ac.uk/CVSSP/demos/chars74k/) and a [scikit learn SVM classifier](http://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html) is trained upon them.

## Package

### Installation

```bash
pip install -e git+https://github.com/jeffseif/digits.git#egg=digits
```

### Development

```bash
git clone git@github.com:jeffseif/digits.git
cd digits
make test
```

### Example invocation

```bash
./cli --help
usage: main.py [-h] [--version] {train,classify} ...

A digit classifier

positional arguments:
  {train,classify}
    train           Train the digit classifier
    classify        Classify an image

optional arguments:
  -h, --help        show this help message and exit
  --version         show program's version number and exit

Version 1.0.0 | Jeffrey Seifried 2017

./cli train --verbose --validate
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

./cli classify /path/to/eight.png
INFO:digits:Deserializing from model.pkl ...
INFO:digits:... done!
INFO:digits:Featurizing /path/to/eight.png
INFO:digits:... done!
INFO:digits:Classifying ...
INFO:digits:... done!
Digit is 8
```
