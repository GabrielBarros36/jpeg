from typing import Final
from jpeg.markers import SOI_marker, APP_0_Marker

def has_SOI(byte_arr: bytes) -> bool:
    return byte_arr[0:2] == SOI_marker.code

def parse_APP_0(byte_arr: bytes) -> APP_0_Marker:
    for i in range(len(byte_arr) - 1):
        if byte_arr[i:i+2] == APP_0_Marker.code:
            return APP_0_Marker(
                [],
                length = int.from_bytes(byte_arr[i+2:i+4]),
                jfif_version_major = byte_arr[i+7],
                jfif_version_minor = byte_arr[i+8],
                pixel_unit_density = byte_arr[i+9],
                x_density = int.from_bytes(byte_arr[i+10:i+12]),
                y_density = int.from_bytes(byte_arr[i+12:i+14]),
            )
    return App_0_Marker()



def make_jpeg_bytes(width=24, height=16, mode="L"):
    buf = io.BytesIO()
    Image.new(mode, (width, height), color=128).save(buf, format="JPEG")
    return buf.getvalue()
