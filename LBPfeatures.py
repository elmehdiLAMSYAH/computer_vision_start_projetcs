from skimage import feature
import numpy as np


class LBP:
    def __init__(self, point_number, radius):
        """ the class constructor """
        self.point_number = point_number
        self.radius = radius

    def describe(self, image, eps=1e-7):
        """ function tasks:
            compute LBP features
            retur a histogram of lbp
        """
        lbp = feature.local_binary_pattern(image,
                                           self.point_number,
                                           self.radius,
                                           method="uniform")
        histograme, _ = np.histogram(lbp.ravel(),
                                     bins=np.arange(0, self.point_number + 3),
                                     range=(0, self.point_number + 2))

        histograme = histograme.astype("float")
        histograme /= (histograme.sum() + eps)
        return histograme