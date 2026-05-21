from PIL import Image


def getPixels(path: str):
    img = Image.open(path)
    compressed = img.resize((60, 60))
    pixels = compressed.load()

    return pixels, compressed
