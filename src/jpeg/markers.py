from dataclasses import dataclass
from typing import Final

# Markers
# fmt: off
SOI:   Final[bytes] = bytes([0xFF, 0xD8]) # stands alone
APP_0: Final[bytes] = bytes([0xFF, 0xE0])
COM:   Final[bytes] = bytes([0xFF, 0xFE])
DQT:   Final[bytes] = bytes([0xFF, 0xDB])
SOF_0: Final[bytes] = bytes([0xFF, 0xC0])
DHT:   Final[bytes] = bytes([0xFF, 0xC4])
SOS:   Final[bytes] = bytes([0xFF, 0xDA])
EOI:   Final[bytes] = bytes([0xFF, 0xD9]) # stands alone
# fmt: on

@dataclass
class SOI_marker:
    code: bytes = SOI

@dataclass
class APP_0_Marker:
    thumbnail_RGB: list[int]

    length: int = 0
    jfif_version_major: int = 0
    jfif_version_minor: int = 0
    pixel_unit_density: int = 0
    x_density: int = 0
    y_density: int = 0
    x_thumbnail: int = 0
    y_thumbnail: int = 0
    code: bytes = APP_0
