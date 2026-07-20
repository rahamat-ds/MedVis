import cv2
import numpy as np
from src.utils.image_utils import to_grayscale


class Thresholding:

    @staticmethod
    def otsu(image: np.ndarray):
        gray = to_grayscale(image)
        _, binary = cv2.threshold(
            gray,
            0,
            255,
            cv2.THRESH_BINARY + cv2.THRESH_OTSU,
        )

        return binary

    @staticmethod
    def adaptive(image: np.ndarray):
        gray = to_grayscale(image)
        return cv2.adaptiveThreshold(
            gray,
            255,
            cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
            cv2.THRESH_BINARY,
            31,
            2,
        )