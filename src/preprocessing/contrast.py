import cv2


class ContrastEnhancer:

    @staticmethod
    def clahe(gray):

        clahe = cv2.createCLAHE(
            clipLimit=2.0,
            tileGridSize=(8, 8)
        )

        return clahe.apply(gray)