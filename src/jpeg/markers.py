from dataclasses import dataclass
from typing import Final

@dataclass
class Marker:
    marker_code: int
    length: int


@dataclass
class APP_0_Marker(Marker):
    jfif_version_major: int
    jfif_version_minor: int
    pixel_unit_density: int
    x_density: int
    y_density: int
    x_thumbnail: int
    y_thumbnail: int
    thumbnail_RGB: list[int]
