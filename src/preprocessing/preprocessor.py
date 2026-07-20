import cv2
import numpy as np

from src.preprocessing.denoiser import Denoiser


class Preprocessor:

    @staticmethod
    def run(image: np.ndarray, method: str) -> np.ndarray:
        """
        Complete preprocessing pipeline.
        """

        denoised = Denoiser.apply(image, method)

        return denoised