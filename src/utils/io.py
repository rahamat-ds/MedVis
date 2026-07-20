from pathlib import Path

import cv2


class ImageWriter:

    @staticmethod
    def save(name, image):

        Path("outputs").mkdir(
            exist_ok=True,
        )

        cv2.imwrite(
            f"outputs/{name}.png",
            image,
        )