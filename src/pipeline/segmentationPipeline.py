from src.segmentation.thresholding import Thresholding
from src.morphology.morphology import Morphology
from src.extraction.contours import ContourExtractor


class SegmentationPipeline:

    @staticmethod
    def run(image):

        otsu = Thresholding.otsu(image)

        adaptive = Thresholding.adaptive(image)

        cleaned = Morphology.clean(adaptive)

        contour = ContourExtractor.largest(cleaned)

        return {
            "otsu": otsu,
            "adaptive": adaptive,
            "clean": cleaned,
            "contour": contour,
        }