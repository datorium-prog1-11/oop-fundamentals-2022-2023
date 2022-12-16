import math

class Circle:
    def __init__(self, diameter):
        self.diameter = diameter
        self.health = 100
        self.happiness = 50
        self.active = True

    def area(self):
        return math.pi * (self.diameter / 2) ** 2
    
    def changeHealth(self, delta):
        self.health += delta
        if self.health <= 0:
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

    def status(self):
        print(f"Health:{self.health} Happiness:{self.happiness}")


class Square:
    def __init__(self, side):
        self.side = side
        self.health = 100
        self.happiness = 50

    def area(self):
        return self.side ** 2

    def changeHealth(self, delta):
        self.health += delta
        if self.health <= 0:
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

    def status(self):
        print(f"Health:{self.health} Happiness:{self.happiness}")


aplis = Circle(5)
kvadrats = Square(5)

print(aplis.area())
print(kvadrats.area())

aplis.status()
kvadrats.status()

aplis.attack(kvadrats)
aplis.attack(kvadrats)
aplis.attack(kvadrats)
aplis.attack(kvadrats)
aplis.attack(kvadrats)

aplis.status()
kvadrats.status()