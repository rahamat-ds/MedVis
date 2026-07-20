import cv2
import numpy as np
from skimage.measure import shannon_entropy
from skimage.restoration import estimate_sigma
from src.utils.image_utils import to_grayscale


def brightness(image):
    gray = to_grayscale(image)
    return float(np.mean(gray) / 255.0)


def contrast(image):
    gray = to_grayscale(image)
    return float(np.std(gray))


def entropy(image):
    gray = to_grayscale(image)
    return float(shannon_entropy(gray))


def noise(image):
    gray = to_grayscale(image)
    sigma = estimate_sigma(
        gray,
        channel_axis=None,
    )
    if isinstance(sigma, (list, tuple, np.ndarray)):
        sigma = float(np.mean(sigma))
    return float(sigma / 255.0) 


def blur(image):
    gray = to_grayscale(image)
    return float(
        cv2.Laplacian(gray, cv2.CV_64F).var()
    )


def edge_density(image):
    gray = to_grayscale(image)
    edges = cv2.Canny(gray, 100, 200)

    return float(
        np.count_nonzero(edges) / edges.size
    )


def bit_depth(image):
    return image.dtype.itemsize * 8


def channels(image):
    if len(image.shape) == 2:
        return 1

    return image.shape[2]