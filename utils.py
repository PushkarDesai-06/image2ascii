import random


def getRandomChar():
    arr = ["/", "-", "@", "-", "H", "$", "#"]
    return arr[random.randint(0, len(arr) - 1)]


def getCharByBrightness(r, g, b):
    brightness = (0.299 * r) + (0.587 * g) + (0.114 * b)
    brightness = min(255, brightness)
    ramp = (
        '$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/|()1{}[]?-_+~<>i!lI;:,"' + "^" + "'. "
    )

    return ramp[int((brightness / 255) * (len(ramp) - 1))]
