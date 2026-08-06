import cv2
import numpy as np


class BodyMask:
    """
    Extract the patient's body from the background.

    This mask is later used to:
    - ignore black borders
    - improve thresholding
    - restrict segmentation to meaningful pixels
    """

    @staticmethod
    def extract(image: np.ndarray) -> np.ndarray:

        # Convert to grayscale if needed
        if len(image.shape) == 3:
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        else:
            gray = image.copy()

        # Slight blur removes tiny artefacts
        blurred = cv2.GaussianBlur(
            gray,
            (5, 5),
            0,
        )

        # Binary mask
        _, mask = cv2.threshold(
            blurred,
            5,
            255,
            cv2.THRESH_BINARY,
        )

        # Fill small holes
        kernel = np.ones((7, 7), np.uint8)

        mask = cv2.morphologyEx(
            mask,
            cv2.MORPH_CLOSE,
            kernel,
            iterations=2,
        )

        # Remove tiny noise
        mask = cv2.morphologyEx(
            mask,
            cv2.MORPH_OPEN,
            kernel,
            iterations=1,
        )

        # Keep only the largest connected object
        contours, _ = cv2.findContours(
            mask,
            cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE,
        )

        if len(contours) == 0:
            return mask

        largest = max(contours, key=cv2.contourArea)

        clean_mask = np.zeros_like(mask)

        cv2.drawContours(
            clean_mask,
            [largest],
            -1,
            255,
            thickness=-1,
        )

        return clean_mask

    @staticmethod
    def apply(image: np.ndarray, mask: np.ndarray):

        """
        Remove everything outside the body.
        """

        return cv2.bitwise_and(
            image,
            image,
            mask=mask,
        )