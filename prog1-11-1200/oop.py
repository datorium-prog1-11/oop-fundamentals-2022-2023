import random

class Rectangle:
    count = 0
    def __init__(self, name, width=10, height=10, color="Blue"):
        self.width = width
        self.height = height
        self.color = color
        self.name = name
        Rectangle.count += 1

    def inform_count():
        print(f"Instances created: {Rectangle.count}")

    def introduce(self):
        print(f"{self.name} {self.color} {self.width} x {self.height}")

    def calculate_area(self):
        print(f"The area is {self.width * self.height}")

# UZDEVUMS: izveido instances metodi kas aprēķina
# un izvada kosolē taisntūra laukumu

rect1 = Rectangle("Oskars", 100, 200, "Purple")
rect1.introduce()
rect1.calculate_area()

rect2 = Rectangle("Alan")
rect2.introduce()
rect2.calculate_area()

kvadrats = Rectangle("Kvadrats", 20, 20, "Red")
kvadrats.introduce()
kvadrats.calculate_area()

Rectangle.inform_count()


#rectangles = []
#colors = ['Red', 'Green', 'Blue', 'Purple', 'Orange', 'Yellow', 'White', 'Black']

#for i in range(100):
#    rectangles.append(Rectangle(f"Name{i+1}", random.randint(1, 500), random.randint(1, 500), random.choice(colors)))

#for rectangle in rectangles:
#    print(f"{rectangle.name} {rectangle.color} {rectangle.width} x {rectangle.height}")