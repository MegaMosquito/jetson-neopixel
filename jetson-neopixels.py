# This code displays rainbow patterns on NeoPixel strings on Jetson nanos.
# Based on https://circuitpython.readthedocs.io/projects/neopixel/en/latest/examples.html

import time
import board
import busio
import neopixel_spi as neopixel
 
# Change these to the appropriate values for your pixel strip
NUM_PIXELS = 16
PIXEL_ORDER = neopixel.RGB

# This assumes SPI0
spi = board.SPI()
pixels = neopixel.NeoPixel_SPI(spi, NUM_PIXELS, pixel_order=PIXEL_ORDER, auto_write=False)

# Returns a color number from a rainbow wheel
def wheel(pos):
  if pos < 0 or pos > 255:
    r = g = b = 0
  elif pos < 85:
    r = int(pos * 3)
    g = int(255 - pos * 3)
    b = 0
  elif pos < 170:
    pos -= 85
    r = int(255 - pos * 3)
    g = 0
    b = int(pos * 3)
  else:
    pos -= 170
    r = 0
    g = int(pos * 3)
    b = int(255 - pos * 3)
  return (r, g, b)

# Loop forever displaying the rotating rainbow
while True:
  for j in range(255):
    for i in range(NUM_PIXELS):
      pixel_index = (i * 256 // NUM_PIXELS) + j
      pixels[i] = wheel(pixel_index & 255)
    pixels.show()
    time.sleep(0.001)

