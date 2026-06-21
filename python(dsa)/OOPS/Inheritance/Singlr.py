class Rectangle:
    def __init__(self,l,b):
        self._l=l
        self._b=b
    def area(self):
        self._a=self._l*self._b
    def perimeter(self):
        self._p=2*(self._l+self._b)
class Cuboid(Rectangle):
    def __init__(self,l,b,h):
        super().__init__(l,b)
        self.__h=h
    def volume(self):
        self.__vol=self._a*(self.__h)
    def display(self):
        self.area()
        self.perimeter()
        self.volume()
        print("Rectangle")
        print("-----------------------")
        print("Area :",self._a)
        print("Perimeter :",self._p)
        print("-----------------------")
        print("Cuboid")
        print("Volume :",self.__vol)  
   
l=int(input("Enter length :"))
b=int(input("Enter Breadth :"))
h=int(input("Enter Height :"))        
c1=Cuboid(l,b,h)
c1.display()
                  
            
    
                        