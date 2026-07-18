from pathlib import Path

import cv2
import numpy as np


class ImageLoader:
    """
    Responsible only for loading an image from disk.
    """

    @staticmethod
    def load(path: str) -> np.ndarray:
        image_path = Path(path)

        if not image_path.exists():
            raise FileNotFoundError(f"Image not found: {path}")

        image = cv2.imread(str(image_path), cv2.IMREAD_UNCHANGED)

        if image is None:
            raise ValueError(f"Unable to load image: {path}")

        return image