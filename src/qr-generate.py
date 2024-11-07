#!/usr/bin/python3

import pyqrcode
import png
from pyqrcode import QRCode

# String which represents the QR code
s = "something is not hidden, but is easily overlooked because it blends in with its surrounding"

# Generate QR code
url = pyqrcode.create(s)

# Create and save the png file naming "myqr.png"
url.png('myqr.png', scale = 6)

