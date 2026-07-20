import cv2
import numpy as np
from pathlib import Path


class ImageLoader:

    @staticmethod
    def load(path: str):

        path = Path(path)

        image = cv2.imread(str(path), cv2.IMREAD_UNCHANGED)

        if image is None:
            raise ValueError(f"Cannot load {path}")

        return image

# class ImageLoader:
#     """
#     Responsible only for loading an image from disk.
#     """

#     @staticmethod
#     def load(path: str) -> np.ndarray:
#         image_path = Path(path)

#         if not image_path.exists():
#             raise FileNotFoundError(f"Image not found: {path}")

#         image = cv2.imread(str(image_path), cv2.IMREAD_UNCHANGED)

#         if image is None:
#             raise ValueError(f"Unable to load image: {path}")

#         return image