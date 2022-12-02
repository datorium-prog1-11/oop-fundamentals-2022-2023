import random
import math

class STEM:
    def rectangle_area(width = 1, height = 1):
        if width >= 0 and height >=0:
            print(f"The area {width}x{height} is {width * height}")
        else:
            print(f"Can not calculate negative area of {width}x{height}")

    def degrees_to_radians(degrees):
        radians = degrees * (math.pi / 180)
        print(f"{degrees} degrees are {radians} radians")


for i in range(20):
    w = random.randint(-20, 20)
    h = random.randint(-20, 20)
    STEM.rectangle_area(w, h)

STEM.degrees_to_radians(60)
