import math
import random

class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.health = 100
        self.happines = 50
    
    def area(self):
        return math.pi * (self.radius ** 2)

    def act(self, target):
        actionList = ['attack', 'friend']
        action = random.choice(actionList)
        if action == 'attack':
            self.attack(target)
        elif action == 'friend':
            self.friend(target)

    def attack(self, target):
        if self.area() > target.area():
            target.changeHealth(-20)
        else:
            self.changeHealth(-20)

    def friend(self, target):
        target.happines += 10
        self.happines += 10

    def changeHealth(self, delta):
        self.health += delta
        if self.health <= 0:
            print("I am out of game")            


class Square:
    def __init__(self, sideLength):
        self.sideLength = sideLength
        self.health = 100
        self.happines = 50

    def area(self):
        return self.sideLength ** 2

    def attack(self, target):
        if self.area() > target.area():
            target.health -= 20
        else:
            self.health -= 20

    def friend(self, target):
        target.happines += 10
        self.happines += 10

    def changeHealth(self, delta):
        self.health += delta
        if self.health <= 0:
            print("I am out of game")            

c1 = Circle(2.5)
s1 = Square(5)
print(f"{c1.health} {c1.happines}")
print(f"{s1.health} {s1.happines}")
c1.act(s1)
print(f"{c1.health} {c1.happines}")
print(f"{s1.health} {s1.happines}")