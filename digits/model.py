import numpy as np
import pickle

from sklearn import svm

from digits import DEFAULT_MODEL_FILENAME
from digits.corpus import Corpus
from digits.image import Image
from digits.logger import Logger


def get_parent_directory():
    import os
    this_directory = os.path.dirname(os.path.realpath(__file__))
    return '{}/../'.format(this_directory)


class Model(Logger):

    PARAMS = {
        'degree': 5,
        'kernel': 'poly',
    }

    def train(self, validate=False):
        self.build_corpus()
        self.fit_model()
        if validate:
            self.validate_classifier()
        return self

    def build_corpus(self):
        self.info('Building corpus ...')
        train_paths = {}
        test_paths = {}
        for digit in range(10):
            train_paths[digit] = Corpus(digit, True)
            test_paths[digit] = Corpus(digit, False)
        self.info('... done!')

        self.info('Featurizing corpus ...')
        self.train = self.featurize_paths(train_paths)
        self.test = self.featurize_paths(test_paths)
        self.info('... done!')

    @staticmethod
    def featurize_paths(label_to_paths):
        features = []
        labels = []
        for label, path_iter in label_to_paths.items():
            images = list(map(Image.file_to_features, path_iter))
            features.extend(images)
            labels.extend([label] * len(images))
        return np.concatenate(features, axis=0), np.array(labels)

    def fit_model(self):
        self.info('Training classifier ...')
        self.clf = svm.SVC(**self.PARAMS)
        self.clf.fit(*self.train)
        self.info('... done!')

    def validate_classifier(self):
        self.info('Validating classifier ...')
        score = self.clf.score(*self.test)
        self.info('... done; F1 score: {:.2%}'.format(score))

    def save(self, model_filename=get_parent_directory() + DEFAULT_MODEL_FILENAME):
        self.info('Serializing to {} ...'.format(model_filename))
        with open(model_filename, 'wb') as f:
            pickle.dump(self.clf, f)
        self.info('... done!')
        return self

    def load(self, model_filename=get_parent_directory() + DEFAULT_MODEL_FILENAME):
        self.info('Deserializing from {} ...'.format(model_filename))
        with open(model_filename, 'rb') as f:
            self.clf = pickle.load(f)
        self.info('... done!')
        return self

    def classify_image(self, path_to_image):
        self.info('Featurizing {} ...'.format(path_to_image))
        features = Image.file_to_features(path_to_image)
        self.info('... done!')
        return self.classify(features)

    def classify_blob(self, blob):
        self.info('Featurizing blob ...')
        features = Image.array_to_features(blob)
        self.info('... done!')
        return self.classify(features)

    def classify(self, features):
        self.info('Classifying ...')
        prediction = self.clf.predict(features)
        self.info('... done!')
        return prediction[0]
