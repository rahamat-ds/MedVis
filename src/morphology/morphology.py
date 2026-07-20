import cv2


class Morphology:

    @staticmethod
    def clean(binary):

        kernel = cv2.getStructuringElement(
            cv2.MORPH_ELLIPSE,
            (5, 5),
        )

        opened = cv2.morphologyEx(
            binary,
            cv2.MORPH_OPEN,
            kernel,
        )

        closed = cv2.morphologyEx(
            opened,
            cv2.MORPH_CLOSE,
            kernel,
        )

        return closed