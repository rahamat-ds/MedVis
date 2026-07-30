from src.preprocessing.adaptive import AdaptivePreprocessor


class PreprocessingPipeline:

    @staticmethod
    def run(image, report, recommendation):

        processed, history = AdaptivePreprocessor.run(
            image,
            report,
            recommendation,
        )

        return processed, history