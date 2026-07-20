from src.preprocessing.preprocessor import Preprocessor
from src.preprocessing.contrast import ContrastEnhancer


class PreprocessingPipeline:

    @staticmethod
    def run(image, recommendation):

        working = image.copy()

        # grayscale handled internally
        working = ContrastEnhancer.clahe(working)

        working = Preprocessor.run(
            working,
            recommendation.method,
        )

        return working