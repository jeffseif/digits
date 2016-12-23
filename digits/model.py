import numpy as np
import pickle

from sklearn import svm

from digits.corpus import Corpus


class Model:

    PARAMS = {
        'degree': 5,
        'kernel':'poly',
    }
    
    def __init__(self, args):
        self.model_filename = args.model_filename
        self.show_score = args.show_score

    def train(self):
        self.load_corpus()
        self.fit()
        if self.show_score:
            self.score()
        self.save()

    def __call__(self, x):
        return self.clf.predict(x)

    def load_corpus(self):
        print('Loading corpus ...')
        train = {}
        test = {}
        for digit in range(10):
            train[digit] = list(Corpus(digit, True))
            test[digit] = list(Corpus(digit, False))
        print('... done!')

        print('Flattening features ...')
        self.train = self.flatten(train)
        self.test = self.flatten(test)
        print('... done!')

    @staticmethod
    def flatten(data):
        features = []
        labels = []
        for label, it in data.items():
            images = list(it)
            length = len(images)
            features.append(np.array(images).reshape((length, -1)))
            labels.extend([label] * length)
        return np.concatenate(features, axis=0), np.array(labels)

    def fit(self):
        print('Training ...')
        self.clf = svm.SVC(**self.PARAMS)
        self.clf.fit(*self.train)
        print('... done!')

    def score(self):
        print('Scoring ...')
        score = self.clf.score(*self.test)
        print('... done; F1 score: {:.2%}'.format(score))

    def save(self):
        print('Serializing to {} ...'.format(self.model_filename))
        with open(self.model_filename, 'wb') as f:
            pickle.dump(self.clf, f)
        print('... done!')

    def load(self):
        print('Deserializing from {} ...'.format(self.model_filename))
        with open(self.model_filename, 'rb') as f:
            self.clf = pickle.load(f)
        print('... done!')
