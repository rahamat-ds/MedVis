from src.core.imageloader import ImageLoader
from src.inspection.inspector import Inspector
from src.inspection.decisionEngine import DecisionEngine


def main():

    image = ImageLoader.load(
        "examples/sample.png"
    )

    report = Inspector.inspect(image)

    recommendation = DecisionEngine.recommend(
        report
    )

    print("=" * 60)
    print("MedVis v0.1")
    print("=" * 60)

    print()

    print("Image Information")

    print(f"Dimensions   : {report.width} x {report.height}")
    print(f"Channels     : {report.channels}")
    print(f"Bit Depth    : {report.bit_depth}")

    print()

    print("Quality Metrics")

    print(f"Brightness   : {report.brightness:.3f}")
    print(f"Contrast     : {report.contrast:.3f}")
    print(f"Entropy      : {report.entropy:.3f}")
    print(f"Noise        : {report.noise:.3f}")
    print(f"Blur Score   : {report.blur:.3f}")
    print(f"Edge Density : {report.edge_density:.3f}")

    print()

    print("Recommendation")

    print(f"Method : {recommendation.method}")
    print(f"Reason : {recommendation.reason}")

    print()

    print("=" * 60)


if __name__ == "__main__":
    main()