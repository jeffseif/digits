import random

from digits.logger import Logger


class Corpus(Logger):

    FRACTION_IN_TRAINING_SET = 0.5
    PATH_FORMAT = 'corpus/English/Fnt/Sample{digit:03d}/img{digit:03d}-{index:05d}.png'
    IMAGES_PER_DIGIT = 1016

    def __init__(self, digit, is_training_set):
        self.digit = digit
        self.is_training_set = is_training_set

    def __iter__(self):
        for index in range(self.IMAGES_PER_DIGIT):
            path = self.PATH_FORMAT.format(
                digit=self.digit + 1,
                index=index + 1,
            )
            if self.is_thing_training_set(path) is self.is_training_set:
                self.debug(path)
                yield path

    @classmethod
    def is_thing_training_set(cls, thing):
        random.seed(thing)
        return random.random() < cls.FRACTION_IN_TRAINING_SET
