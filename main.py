import cv2
from src.core.imageloader import ImageLoader
from src.inspection.inspector import Inspector
from src.inspection.decision_engine import DecisionEngine
from pathlib import Path
from src.preprocessing.denoiser import Denoiser
from src.preprocessing.body_musk import BodyMask
from src.utils.visualization import side_by_side
from src.preprocessing.preprocessor import Preprocessor
from src.segmentation.thresholding import Thresholding
from src.morphology.morphology import Morphology
from src.extraction.contours import ContourExtractor
from src.utils.visualization import draw_contour
from src.utils.io import ImageWriter

def main():

    image = ImageLoader.load(
        "datasets/raw/CHNCXR_0001_0.png"
    )

    body_mask = BodyMask.extract(image)
    masked_image = BodyMask.apply(image, body_mask)
    report = Inspector.inspect(masked_image)
    recommendation = DecisionEngine.recommend(report)
    processed = Denoiser.apply(image, recommendation.method)
    processed = Preprocessor.run(
        image=masked_image,
        method=recommendation.method,
        contrast=report.contrast,
        blur=report.blur,
    )

    otsu = Thresholding.otsu(processed)
    adaptive = Thresholding.adaptive(processed)
    clean = Morphology.clean(otsu)
    largest = ContourExtractor.largest(clean)
    overlay = draw_contour(image,largest)
    comparison = side_by_side(masked_image,processed)

    Path("outputs/processed").mkdir(
        parents=True,
        exist_ok=True,
    )

    Path("outputs/comparison").mkdir(
        parents=True,
        exist_ok=True,
    )

    cv2.imwrite("outputs/processed/result.png",processed)
    cv2.imwrite("outputs/comparison/comparison.png",comparison)

    ImageWriter.save("01_original", image)
    ImageWriter.save("01_body_mask", body_mask)
    ImageWriter.save("01_masked_body", masked_image)
    ImageWriter.save("02_denoised", processed)
    ImageWriter.save("03_otsu", otsu)
    ImageWriter.save("04_adaptive", adaptive)
    ImageWriter.save("05_clean", clean)
    ImageWriter.save("06_overlay",overlay)

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
    # print(f"Edge Density : {report.edge_density:.3f}")
    print(f"Edge Density : {report.edge_density:.6f}")


    print()

    print("Recommendation")

    print(f"Method : {recommendation.method}")
    print(f"Reason : {recommendation.reason}")

    print()

    print("Adaptive Decisions")
    if report.contrast < 40:
        print("✓ CLAHE enhancement applied")

    if report.blur < 150:
        print("✓ Bilateral smoothing applied")

    print(f"✓ {recommendation.method}")
    print()
    print("=" * 60)

    print()
    print("Output")
    print("Processed image saved to:")
    print("outputs/processed/result.png")

    print()

    print("Comparison saved to:")
    print("outputs/comparison/comparison.png")

if __name__ == "__main__":
    main()

    