from dataclasses import dataclass

from src.utils import metrics


@dataclass
class InspectionResult:

    width: int
    height: int

    channels: int
    bit_depth: int

    brightness: float
    contrast: float
    entropy: float

    noise: float
    blur: float

    edge_density: float


class Inspector:

    @staticmethod
    def inspect(image):

        height, width = image.shape[:2]

        return InspectionResult(

            width=width,
            height=height,

            channels=metrics.channels(image),
            bit_depth=metrics.bit_depth(image),

            brightness=metrics.brightness(image),
            contrast=metrics.contrast(image),
            entropy=metrics.entropy(image),

            noise=metrics.noise(image),
            blur=metrics.blur(image),

            edge_density=metrics.edge_density(image),
        )