from scipy import ndimage


class Image:

    RESOLUTION = (16, 16)
    ZOOM_ORDER = 5

    @classmethod
    def file_to_array(cls, file_or_path):
        image = ndimage.imread(file_or_path)
        zoom = cls.shape_to_zoom(image.shape)
        return ndimage.zoom(
            image,
            zoom,
            order=cls.ZOOM_ORDER,
        )

    @classmethod
    def shape_to_zoom(cls, shape):
        return tuple(
            num / denom
            for denom, num in zip(shape, cls.RESOLUTION)
        )
