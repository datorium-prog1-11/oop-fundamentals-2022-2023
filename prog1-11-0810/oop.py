import random

class Rectangle:
    def __init__(self, name, width = 10, height = 10, color = "Blue"):
        self.width = width
        self.height = height
        self.color = color
        self.name = name

rect1 = Rectangle("Valters", height=200)
print(f"Hi I am {rect1.color} rectangle {rect1.name}, my width is {rect1.width} and height is {rect1.height}")

rect2 = Rectangle("Anna", 40, 40, "Orange")
print(f"Hi I am {rect2.color} rectangle {rect2.name}, my width is {rect2.width} and height is {rect2.height}")

rectangles = []

for i in range(100):
    rectangles.append(Rectangle(f"Name{i+1}", random.randint(1, 500), random.randint(1, 500)))

for rectangle in rectangles:
    print(f"{rectangle.name} {rectangle.color} {rectangle.width} {rectangle.height}")