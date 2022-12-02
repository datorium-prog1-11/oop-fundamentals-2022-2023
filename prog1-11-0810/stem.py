import random

class Translator:
    pass

class Biology:
    pass

class STEM:
    def rectangle_area(width, height):
        return width * height

    def degrees_to_radians(degrees):
        pi = 3.14159
        radians = degrees*(pi/180)
        return radians

    def circle_area(radius):
        pi = 3.142857
        return (radius**2)*pi

    def jebkada_funkcija(arguments1, arguments2):
        #te notiek aprēķini
        return 0        

print(STEM.rectangle_area(20, 40))
print(STEM.degrees_to_radians(160))
print(STEM.circle_area(0.5))

print(random.randint(1, 101))