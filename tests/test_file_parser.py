from jpeg.parser import has_SOI, SOI, parse_APP_0, APP_0
import io

from PIL import Image


def test_has_SOI():
    data = make_jpeg_bytes()
    assert data[0:2] == SOI
    assert has_SOI(data[0:2])


def test_parse_APP_0():
    data = make_jpeg_bytes()

    result = parse_APP_0(data)
    assert result.length > 0


def make_jpeg_bytes(width=24, height=16, mode="L"):
    buf = io.BytesIO()
    Image.new(mode, (width, height), color=128).save(buf, format="JPEG")
    return buf.getvalue()
