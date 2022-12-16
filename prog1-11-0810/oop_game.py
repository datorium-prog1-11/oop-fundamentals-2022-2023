import math
import random

class Circle:

    count = 0

    def __init__(self, radius):
        self.radius = radius
        self.__health = 100
        self.happines = 50
        self.isActive = True
        Circle.count += 1

    def status(self):
        return f"Health {self.__health} Happiness {self.happines}"       
      
    def area(self):
        return math.pi * (self.radius ** 2)

    def act(self, target):
        if not self.isActive:
            return

        actionList = ['attack', 'friend']
        action = random.choice(actionList)
        if action == 'attack':
            self.attack(target)
        elif action == 'friend':
            self.friend(target)

    def attack(self, target):
        if not self.isActive:
            return
        
        if self.area() > target.area():
            target.changeHealth(-20)
        else:
            self.changeHealth(-20)

    def friend(self, target):
        if not self.isActive:
            return

        target.happines += 10
        self.happines += 10

    def changeHealth(self, delta):
        self.__health += delta
        if self.__health <= 0:
            self.isActive = False
            print("I am out of game")            


class Square:

    count = 0

    def __init__(self, sideLength):
        self.sideLength = sideLength
        self.__health = 100
        self.happines = 50
        self.isActive = True
        Square.count += 1

    def status(self):
        return f"Health {self.__health} Happiness {self.happines}" 
    
    def area(self):
        return self.sideLength ** 2    
    
    def act(self, target):
        if not self.isActive:
            return

        actionList = ['attack', 'friend']
        action = random.choice(actionList)
        if action == 'attack':
            self.attack(target)
        elif action == 'friend':
            self.friend(target)

    def attack(self, target):
        if not self.isActive:
            return
        
        if self.area() > target.area():
            target.changeHealth(-20)
        else:
            self.changeHealth(-20)

    def friend(self, target):
        if not self.isActive:
            return

        target.happines += 10
        self.happines += 10

    def changeHealth(self, delta):
        self.__health += delta
        if self.__health <= 0:
            self.isActive = False
            print("I am out of game")

circles = []
squares = []

for i in range(100):
    diameter = random.randint(1, 201)
    circles.append(Circle(diameter/2))
    squares.append(Square(random.randint(1, 201)))

print(Circle.count)
print(Square.count)

for counter in range(10):
    for i in range(100):
        circles[i].act(squares[i])

for i in range(100):
    print(f"Circle: {circles[i].status()} Square: {squares[i].status()}")