import cv2
import numpy as np

from src.preprocessing.contrast import ContrastEnhancer
from src.preprocessing.denoiser import Denoiser


class AdaptivePreprocessor:

    @staticmethod
    def run(image, report, recommendation):

        output = image.copy()

        steps = []

        # ---------- Contrast ----------

        if report.contrast < 40:

            output = ContrastEnhancer.clahe(output)

            steps.append("CLAHE")

        # ---------- Noise ----------

        if recommendation.method != "None":

            output = Denoiser.apply(
                output,
                recommendation.method,
            )

            steps.append(recommendation.method)

        # ---------- Blur ----------

        if report.blur < 150:

            output = cv2.bilateralFilter(
                output,
                d=7,
                sigmaColor=60,
                sigmaSpace=60,
            )

            steps.append("Bilateral")

        return output, steps