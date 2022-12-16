class rect:
    def __init__(self):
        self._health = 100
        self.energy = 100

    @property
    def health(self):
        print('getter method')
        return self._health
    
    @health.setter
    def health(self, newHealth):
        print('setter method')
        self._health = newHealth


r1 = rect()
r1.health = 20

print(r1.health)


class A:
    def __init__(self):
        self.__var = 123
    
    def printVar(self):
        print(self.__var)

x = A()
x.__var