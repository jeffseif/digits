from scipy import ndimage

from digits.logger import Logger


class Image(Logger):

    RESOLUTION = (16, 16)
    ZOOM_ORDER = 5

    @classmethod
    def file_to_features(cls, file_or_path):
        array = ndimage.imread(file_or_path)
        return cls.array_to_features(array)

    @classmethod
    def array_to_features(cls, array):
        zoomed = ndimage.zoom(
            array,
            cls.get_array_zoom(array),
            order=cls.ZOOM_ORDER,
        )
        return cls.zoomed_to_features(zoomed)

    @classmethod
    def get_array_zoom(cls, array):
        return tuple(
            num / denom
            for denom, num in zip(array.shape, cls.RESOLUTION)
        )

    @classmethod
    def zoomed_to_features(cls, zoomed):
        return zoomed.reshape((1, -1))
