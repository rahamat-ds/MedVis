import cv2
import numpy as np


def side_by_side(original, processed):

    if len(original.shape) == 2:
        original = cv2.cvtColor(
            original,
            cv2.COLOR_GRAY2BGR,
        )

    if len(processed.shape) == 2:
        processed = cv2.cvtColor(
            processed,
            cv2.COLOR_GRAY2BGR,
        )

    return np.hstack(
        (
            original,
            processed,
        )
    )


def draw_contour(image, contour):

    output = image.copy()

    if len(output.shape) == 2:
        output = cv2.cvtColor(
            output,
            cv2.COLOR_GRAY2BGR,
        )

    if contour is not None:

        cv2.drawContours(
            output,
            [contour],
            -1,
            (0, 255, 0),
            2,
        )

    return output