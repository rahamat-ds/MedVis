import cv2
import numpy as np
from src.utils.image_utils import to_grayscale


class Denoiser:

    @staticmethod
    def apply(image: np.ndarray, method: str) -> np.ndarray:
        """
        Apply the selected denoising algorithm.
        """
        gray = to_grayscale(image)

        if method == "None":
            return gray.copy()

        if method == "Gaussian Filter":
            return cv2.GaussianBlur(
                gray,
                (5, 5),
                0,
            )

        if method == "Median Filter":
            return cv2.medianBlur(
                gray,
                5,
            )

        if method == "Bilateral Filter":
            return cv2.bilateralFilter(
                gray,
                d=9,
                sigmaColor=75,
                sigmaSpace=75,
            )

        if method == "Non Local Means":

            return cv2.fastNlMeansDenoising(
                gray,
                None,
                h=10,
                templateWindowSize=7,
                searchWindowSize=21,
            )

        raise ValueError(f"Unknown method: {method}")