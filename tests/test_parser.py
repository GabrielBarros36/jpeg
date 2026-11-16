import io

from PIL import Image

from jpeg.markers import SOI_marker,APP_0_Marker
from jpeg.parser import has_SOI, parse_APP_0


def test_has_SOI():
    data = make_jpeg_bytes()
    assert data[0:2] == SOI_marker.code
    assert has_SOI(data[0:2])


def test_parse_APP_0():
    data = make_jpeg_bytes()

    result = parse_APP_0(data)
    assert result.length > 0


def test_parse_APP_0_all_fields():
    data = make_jpeg_bytes()
    result = parse_APP_0(data)
    assert result.length == 0x10
    assert result.jfif_version_major == 1
    assert result.jfif_version_minor == 1
    assert result.pixel_unit_density == 0
    assert result.x_density == 1
    assert result.y_density == 1
    assert result.x_thumbnail == 0
    assert result.y_thumbnail == 0
    assert len(result.thumbnail_RGB) == 0

def make_jpeg_bytes(width=24, height=16, mode="L"):
    buf = io.BytesIO()
    Image.new(mode, (width, height), color=128).save(buf, format="JPEG")
    return buf.getvalue()
