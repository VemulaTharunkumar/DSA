import math

class Circle:
    def __init__(self, r):
        self._r = r

    def area(self):
        self._a = math.pi * (self._r ** 2)


class Sphere(Circle):
    def __init__(self, r):
        super().__init__(r)

    def volume(self):
        self._v = (4/3) * math.pi * (self._r ** 3)

    def display(self):
        self.area()
        self.volume()
        print("Radius:", self._r)
        print("Area of Circle:", self._a)
        print("Volume of Sphere:", self._v)


class Cylinder(Circle):
    def __init__(self, r, h):
        super().__init__(r)
        self._h = h

    def volume(self):
        self._v = math.pi * (self._r ** 2) * self._h

    def display(self):
        self.area()
        self.volume()
        print("Radius:", self._r)
        print("Height:", self._h)
        print("Area of Circle:", self._a)
        print("Volume of Cylinder:", self._v)


r = int(input("Enter Radius: "))

s = Sphere(r)
s.display()

h = int(input("\nEnter Height: "))

c = Cylinder(r, h)
c.display()