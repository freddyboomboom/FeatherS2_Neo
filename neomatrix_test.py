# Based on code from Andy Piper: https://github.com/andypiper/fivebyfive/blob/main/micropython/main.py
# This script is for CircuitPython, and requires you have the Adafruit neopixel library installed.
import board
from neopixel import NeoPixel
import random
import time

neopin = board.NEOPIXEL_MATRIX
pixels = 25
np = NeoPixel(neopin, pixels)

def rand_rgb():
    # Return a randomised RGB tuple, max values of 50 to limit brightness
    r = random.randint(0, 50)
    g = random.randint(0, 50)
    b = random.randint(0, 50)
    return r, g, b

def clear_all():
    # Reset all Neopixels to black / off
    # TODO: could have this use a custom colour
    np.fill((0, 0, 0))
    np.write()

def test_all_np():
    # Iterate through all Neopixels and blink
    # with random colours in sequence
    clear_all()
    for x in range(pixels):
        np[x] = rand_rgb()
        np.write()
        print("Pixel: " + str(x))
        time.sleep(0.4)
        np[x] = (0, 0, 0)
        np.write()
        time.sleep(0.2)
    print("NeoPixels Test completed.")

test_all_np()
