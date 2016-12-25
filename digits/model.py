import numpy as np
import pickle

from sklearn import svm

from digits.corpus import Corpus
from digits.image import Image
from digits.logger import Logger


class Model(Logger):

    PARAMS = {
        'degree': 5,
        'kernel':'poly',
    }
    
    def train(self, validate):
        self.index_corpus()
        self.fit_model()
        if validate:
            self.validate_classifier()
        return self

    def index_corpus(self):
        self.info('Indexing corpus ...')
        train = {}
        test = {}
        for digit in range(10):
            train[digit] = Corpus(digit, True)
            test[digit] = Corpus(digit, False)
        self.info('... done!')

        self.info('Flattening features ...')
        self.train = self.flatten(train)
        self.test = self.flatten(test)
        self.info('... done!')

    @staticmethod
    def flatten(data):
        features = []
        labels = []
        for label, it in data.items():
            images = list(map(Image.file_to_array, it))
            length = len(images)
            features.append(np.array(images).reshape((length, -1)))
            labels.extend([label] * length)
        return np.concatenate(features, axis=0), np.array(labels)

    def fit_model(self):
        self.info('Training ...')
        self.clf = svm.SVC(**self.PARAMS)
        self.clf.fit(*self.train)
        self.info('... done!')

    def validate_classifier(self):
        self.info('Validating ...')
        score = self.clf.score(*self.test)
        self.info('... done; F1 score: {:.2%}'.format(score))

    def save(self, model_filename):
        self.info('Serializing to {} ...'.format(model_filename))
        with open(model_filename, 'wb') as f:
            pickle.dump(self.clf, f)
        self.info('... done!')
        return self

    def load(self, model_filename):
        self.info('Deserializing from {} ...'.format(model_filename))
        with open(model_filename, 'rb') as f:
            self.clf = pickle.load(f)
        self.info('... done!')
        return self

    def classify_image(self, path_to_image):
        image_map = {None: [path_to_image]}
        features, _ = self.flatten(image_map)
        prediction = self.clf.predict(features)
        return prediction[0]
