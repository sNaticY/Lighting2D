# Importing Image module from PIL package
import math

from PIL import Image
import PIL
import random

H = 200
W = 200

def main():
    # creating a image object (main image)
    img = PIL.Image.new(mode="RGB", size=(W, H))

    for i in range(img.size[0]):
        for j in range(img.size[1]):
            c = int(sample(float(i) / W, float(j) / H) * 255)
            img.putpixel((i, j), (c, c, c))

    # This method will show image in any image viewer
    img.show()
    img.save("images/01.jpg", "JPEG")


N = 64
TWO_PI = 6.28318530718


def sample(x, y) -> float:
    sum_number = 0.0
    for i in range(N):
        a = TWO_PI * (i + random.random() / 1.0) / N
        sum_number += trace(x, y, math.cos(a), math.sin(a))

    return sum_number / N


def circle_sdf(x: float, y: float, cx: float, cy: float, r: float) -> float:
    ux: float = x - cx
    uy: float = y - cy
    return math.sqrt(ux * ux + uy * uy) - r


MAX_STEP = 10
MAX_DISTANCE = 2.0
EPSILON = float(1e-6)


def trace(ox: float, oy: float, dx: float, dy: float) -> float:
    t = 0.0
    i = 0.0
    while i < MAX_STEP and t < MAX_DISTANCE:
        sd = circle_sdf(ox + dx * t, oy + dy * t, 0.5, 0.5, 0.1)
        if sd < EPSILON:
            return 2.0
        t += sd
        ++i
    return 0.0


if __name__ == '__main__':
    main()


print('demo/__init__.py executed')
