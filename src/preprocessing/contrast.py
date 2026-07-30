
import cv2

class ContrastEnhancer:

    @staticmethod
    def clahe(
        gray,
        clip_limit=2.0,
        tile_grid=(8, 8),
    ):
        clahe = cv2.createCLAHE(
            clipLimit=clip_limit,
            tileGridSize=tile_grid,
        )
        return clahe.apply(gray)