
import math

class Circle():
    
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi*self.radius**2
    
    def perimeter(self):
        return 2*math.pi*self.radius

class Rectangle():
    
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def __eq__(self, other):
        if not isinstance(other, Rectangle):
            return False
        
        return (self.width == other.width) and (self.length == other.length)
    
    def area(self):
        return self.length*self.width
    
    def perimeter(self):
        return 2*(self.length+self.width)


class Square(Rectangle):
    
    def __init__(self, side):
        super().__init__(length = side, width = side)

    
