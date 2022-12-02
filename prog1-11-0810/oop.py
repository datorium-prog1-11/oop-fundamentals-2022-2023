import random

class Rectangle:
    surname = "Simpsons"
    count = 0

    def __init__(self, name, width = 10, height = 10, color = "Blue"):
        self.width = width
        self.height = height
        self.color = color
        self.name = name
        Rectangle.count += 1

    def introduce(self):
        print(f"Hi I am {self.color} rectangle {self.name}, my dimentions are {self.width}x{self.height}")

    def mans_laukums(self):
        print(f"Mans laukums ir {self.width * self.height}")

rect1 = Rectangle("Valters", height=200)
rect1.introduce()
rect1.mans_laukums()

rect2 = Rectangle("Anna", 40, 40, "Orange")
rect2.introduce()
rect2.mans_laukums()


print(f"Number of created instances: {Rectangle.count}")

# rectangles = []

#for i in range(100):
#    rectangles.append(Rectangle(f"Name{i+1}", random.randint(1, 500), random.randint(1, 500)))

#for rectangle in rectangles:
#    print(f"{rectangle.name} {rectangle.color} {rectangle.width} {rectangle.height}")