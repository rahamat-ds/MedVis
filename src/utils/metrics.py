import cv2
import numpy as np
from skimage.measure import shannon_entropy
from skimage.restoration import estimate_sigma


def brightness(image):
    return float(np.mean(image) / 255.0)


def contrast(image):
    return float(np.std(image))


def entropy(image):
    return float(shannon_entropy(image))


def noise(image):
    sigma = estimate_sigma(
        image,
        channel_axis=None,
    )

    if isinstance(sigma, (list, tuple, np.ndarray)):
        sigma = float(np.mean(sigma))

    return float(sigma)


def blur(image):
    return float(
        cv2.Laplacian(image, cv2.CV_64F).var()
    )


def edge_density(image):
    edges = cv2.Canny(image, 100, 200)

    return float(
        np.count_nonzero(edges) / edges.size
    )


def bit_depth(image):
    return image.dtype.itemsize * 8


def channels(image):
    if len(image.shape) == 2:
        return 1

    return image.shape[2]