#Jeremy Durdel
#Chapter 7 and 8 CPX 1
#07/02/2025

from adafruit_circuitplayground import cp
import time
import random

pattern = []

with open("pattern.txt") as file:
    line = file.readline()
    pattern = [int(pin.strip()) for pin in line.strip()
    .split(',') if pin.strip().isdigit()]

def pixel_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    return (red, green, blue)

def off_pixels():
    for i in range(10):
        cp.pixels[i] = (0, 0, 0)

while True:
    for pixel in pattern:
        if 0 <= pixel < 10:
            cp.pixels.fill((0, 0, 0))
            cp.pixels[pixel] = pixel_color()
            time.sleep(0.5)

