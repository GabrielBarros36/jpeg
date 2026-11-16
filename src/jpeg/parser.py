from typing import Final
from jpeg.markers import APP_0_Marker

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

def has_SOI(byte_arr: bytes) -> bool:
    return byte_arr[0:2] == SOI

def parse_APP_0(byte_arr: bytes) -> int:
    for i in range(len(byte_arr) - 1):
        if byte_arr[i] == 0xff:
            if byte_arr[i+1] == 0xe0:
                return i
    return -1



def make_jpeg_bytes(width=24, height=16, mode="L"):
    buf = io.BytesIO()
    Image.new(mode, (width, height), color=128).save(buf, format="JPEG")
    return buf.getvalue()
