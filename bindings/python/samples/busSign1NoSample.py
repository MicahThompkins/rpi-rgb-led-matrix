#!/usr/bin/env python
import time
import sys

from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics
from PIL import Image

# if len(sys.argv) < 2:
#     sys.exit("Require an image argument")
# else:
#     image_file = sys.argv[1]
#
# image = Image.open(image_file)

# Configuration for the matrix
options = RGBMatrixOptions()
options.rows = 16
options.chain_length = 1
options.parallel = 1
options.hardware_mapping = 'classic-pi1'  # If you have an Adafruit HAT: 'adafruit-hat'

matrix = RGBMatrix(options = options)

# Make image fit our screen.
# image.thumbnail((matrix.width, matrix.height), Image.ANTIALIAS)
#
# matrix.SetImage(image.convert('RGB'))
offscreen_canvas = matrix.CreateFrameCanvas()
font = graphics.Font()
font.LoadFont("../../../fonts/7x13.bdf")
textColor = graphics.Color(255, 0, 0)
pos = offscreen_canvas.width
my_text = "#9 North in 5 minutes"
graphics.DrawText(offscreen_canvas, font, pos, 10, textColor, my_text)

try:
    print("Press CTRL-C to stop.")
    while True:
        time.sleep(100)
except KeyboardInterrupt:
    sys.exit(0)
