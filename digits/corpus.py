import random

from scipy import ndimage


class Corpus:

    FRACTION_IN_TRAINING_SET = 0.5
    PATH_FORMAT = 'corpus/English/Fnt/Sample{digit:03d}/img{digit:03d}-{index:05d}.png'
    IMAGES_PER_DIGIT = 1016
    RESOLUTION = (16, 16)
    ZOOM_ORDER = 5

    def __init__(self, digit, is_training_set):
        self.digit = digit
        self.is_training_set = is_training_set
    
    def __iter__(self):
        for index in range(self.IMAGES_PER_DIGIT):
            path = self.PATH_FORMAT.format(
                digit=self.digit+1,
                index=index+1,
            )
            if self.is_thing_training_set(path) is self.is_training_set:
                yield self.path_to_array(path)

    def is_thing_training_set(self, thing):
        random.seed(thing)
        return random.random() < self.FRACTION_IN_TRAINING_SET

    def path_to_array(self, path):
        image = ndimage.imread(path)
        zoom = self.shape_to_zoom(image.shape)
        return ndimage.zoom(
            image,
            zoom,
            order=self.ZOOM_ORDER,
        )

    def shape_to_zoom(self, shape):
        return tuple(
            num / denom
            for denom, num in zip(shape, self.RESOLUTION)
        )
