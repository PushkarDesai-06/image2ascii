from compressor import getPixels
from rich import print
import random

pixels, img = getPixels("./photos/image2.jpg")

a, b, c = img.getbands()
h, w = img.size

print(f"{h} {w}")


def getRandomChar():
    arr = ["/", "-", "@", "-", "H", "$", "#"]
    return arr[random.randint(0, len(arr) - 1)]


for i in range(h):
    for j in range(w):
        r, g, b = pixels[j, i]
        brightness = (0.299 * r) + (0.587 * g) + (0.114 * b)
        brightness = min(255, brightness)
        ramp = (
            '$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/|()1{}[]?-_+~<>i!lI;:,"'
            + "^"
            + "'. "
        )

        char = ramp[int((brightness / 255) * (len(ramp) - 1))]

        # print(f"[rgb({r},{g},{b})]{char}{char}", end="")
        print(f"[bold black on rgb({r},{g},{b})]||", end="")
        # print(f"{char}{char}", end="")
        # print(f"[rgb({r};{g};{b})]█", end="")
    print("")
