import numpy as np
import pickle

from sklearn import svm

from digits.corpus import Corpus
from digits.image import Image


class Model:

    PARAMS = {
        'degree': 5,
        'kernel':'poly',
    }
    
    def train(self, show_score):
        self.index_corpus()
        self.fit_model()
        if show_score:
            self.score_classifier()
        return self

    def index_corpus(self):
        print('Indexing corpus ...')
        train = {}
        test = {}
        for digit in range(10):
            train[digit] = Corpus(digit, True)
            test[digit] = Corpus(digit, False)
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
            images = list(map(Image.file_to_array, it))
            length = len(images)
            features.append(np.array(images).reshape((length, -1)))
            labels.extend([label] * length)
        return np.concatenate(features, axis=0), np.array(labels)

    def fit_model(self):
        print('Training ...')
        self.clf = svm.SVC(**self.PARAMS)
        self.clf.fit(*self.train)
        print('... done!')

    def score_classifier(self):
        print('Scoring ...')
        score = self.clf.score(*self.test)
        print('... done; F1 score: {:.2%}'.format(score))

    def save(self, model_filename):
        print('Serializing to {} ...'.format(model_filename))
        with open(model_filename, 'wb') as f:
            pickle.dump(self.clf, f)
        print('... done!')
        return self

    def load(self, model_filename):
        print('Deserializing from {} ...'.format(model_filename))
        with open(model_filename, 'rb') as f:
            self.clf = pickle.load(f)
        print('... done!')
        return self

    def classify_image(self, path_to_image):
        array = Image.file_to_array(path_to_image)
        features, _ = self.flatten({None: [array]})
        prediction = self.clf.predict(features)
        return prediction[0]