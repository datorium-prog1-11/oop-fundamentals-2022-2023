import math
import random

class Circle:
    def __init__(self, diameter):
        self.diameter = diameter
        self.__health = 100
        self.happiness = 50
        self.active = True

    def area(self):
        return math.pi * (self.diameter / 2) ** 2
    
    def changeHealth(self, delta):
        self.__health += delta
        if self.__health <= 0:
            print("I am out of the game...")
            self.active = False

    def attack(self, target):
        if self.active:        
            if self.area() > target.area():
                target.changeHealth(-30)
            else:
                self.changeHealth(-30)
        else:
            print("Can not attack, I am out of game")

    def friend(self, target):
        target.happiness += 10
        self.happiness += 10

    def interact(self, target):
        actions = ['attack', 'friend']
        action = random.choice(actions)
        if action == 'attack':
            self.attack(target)
        elif action == 'friend':
            self.friend(target)

    def status(self):
        return f"Health:{self.__health} Happiness:{self.happiness}"


class Square:
    def __init__(self, side):
        self.side = side
        self.__health = 100
        self.happiness = 50
        self.active = True

    def area(self):
        return self.side ** 2

    def changeHealth(self, delta):
        self.__health += delta
        if self.__health <= 0:
            print("I am out of the game...")
            self.active = False

    def attack(self, target):
        if self.active:        
            if self.area() > target.area():
                target.changeHealth(-30)
            else:
                self.changeHealth(-30)
        else:
            print("Can not attack, I am out of game")

    def friend(self, target):
        target.happiness += 10
        self.happiness += 10

    def interact(self, target):
        actions = ['attack', 'friend']
        action = random.choice(actions)
        if action == 'attack':
            self.attack(target)
        elif action == 'friend':
            self.friend(target)

    def status(self):
        return f"Health:{self.__health} Happiness:{self.happiness}"


circles = []
squares = []

for i in range(100):
    circles.append(Circle(random.randint(1, 200)))
    squares.append(Square(random.randint(1, 200)))

print(f"Circles: {len(circles)}, Squares: {len(squares)}")

for sim in range(10):
    for i in range(100):
        circles[i].interact(squares[i])

for i in range(100):
    print(f"Circle {circles[i].status()} | Square {squares[i].status()}")