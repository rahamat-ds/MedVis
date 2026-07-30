import cv2
import numpy as np
from src.preprocessing.denoiser import Denoiser
from src.preprocessing.contrast import ContrastEnhancer


class Preprocessor:

    @staticmethod
    def run(
        image: np.ndarray,
        method: str,
        contrast: float = None,
        blur: float = None,
    ) -> np.ndarray:
        """
        Adaptive preprocessing pipeline.
        Steps:
        1. Convert to grayscale (inside Denoiser)
        2. Improve contrast if needed
        3. Denoise according to Decision Engine
        4. Slight smoothing if image is blurry
        """
        # Denoiser already converts to grayscale
        processed = Denoiser.apply(image, method)

        # Low contrast
        if contrast is not None and contrast < 40:
            processed = ContrastEnhancer.clahe(processed)

        # Blurry image
        if blur is not None and blur < 150:
            processed = cv2.bilateralFilter(
                processed,
                d=5,
                sigmaColor=50,
                sigmaSpace=50,
            )
        return processed