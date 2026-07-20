import cv2


class ContourExtractor:

    @staticmethod
    def largest(binary):

        contours, _ = cv2.findContours(
            binary,
            cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE,
        )

        if len(contours) == 0:
            return None

        return max(
            contours,
            key=cv2.contourArea,
        )