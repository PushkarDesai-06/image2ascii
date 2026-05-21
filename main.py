import os
from compressor import getPixels
from utils import getCharByBrightness
from rich import print


def printImage(imagePath):
    path = os.path.realpath(imagePath)
    currPath = os.path.abspath("./")

    if not path.startswith(currPath):
        print("Not a valid path!")
        return
    pixels, img = getPixels(imagePath)
    h, w = img.size

    for i in range(h):
        for j in range(w):
            r, g, b = pixels[j, i]
            char = getCharByBrightness(r, g, b)

            print(f"[rgb({r},{g},{b})]{char}{char}", end="")
            # print(f"[bold black on rgb({r},{g},{b})]||", end="")
            # print(f"{char}{char}", end="")
            # print(f"[rgb({r};{g};{b})]█", end="")
        print("")


printImage("./photos/image4.jpg")
