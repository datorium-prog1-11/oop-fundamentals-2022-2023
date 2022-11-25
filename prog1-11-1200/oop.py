import random

class Rectangle:
    def __init__(self, name, width=10, height=10, color="Blue"):
        self.width = width
        self.height = height
        self.color = color
        self.name = name

rect1 = Rectangle("Oskars", 100, 200, "Purple")
print(f"{rect1.name} {rect1.color} {rect1.width} x {rect1.height}")

rect2 = Rectangle("Alan")
print(f"{rect2.name} {rect2.color} {rect2.width} x {rect2.height}")

rectangles = []
colors = ['Red', 'Green', 'Blue', 'Purple', 'Orange', 'Yellow', 'White', 'Black']

for i in range(100):
    rectangles.append(Rectangle(f"Name{i+1}", random.randint(1, 500), random.randint(1, 500), random.choice(colors)))

for rectangle in rectangles:
    print(f"{rectangle.name} {rectangle.color} {rectangle.width} x {rectangle.height}")