# abstract method
# abc = abstract base class -> blue print class
from abc import ABC, abstractclassmethod


class Shape(ABC):         # abstract base class (Shape())
    @abstractclassmethod
    def draw(self):
        pass

class Rectangle(Shape):
    def draw(self):
        print("In Rectangle.draw")

class Circle(Shape):
    def draw(self):
        print('In Circle.draw')

# objs = Shape()        # error

objr = Rectangle()
objc = Circle()

objr.draw()
objc.draw()