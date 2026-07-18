from dataclasses import dataclass

from src.inspection.inspector import InspectionResult


@dataclass
class Recommendation:

    method: str
    reason: str


class DecisionEngine:

    @staticmethod
    def recommend(result: InspectionResult):

        if result.noise > 0.05:

            return Recommendation(
                "Non Local Means",
                "High estimated noise"
            )

        if result.noise > 0.02:

            return Recommendation(
                "Bilateral Filter",
                "Moderate noise while preserving edges"
            )

        if result.blur < 80:

            return Recommendation(
                "Gaussian Filter",
                "Low Laplacian variance indicates blur"
            )

        return Recommendation(
            "None",
            "Image quality acceptable"
        )