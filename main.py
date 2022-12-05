# Object-oriented programming (OOP) is a programming paradigm based on the concept of "objects", which are data structures that contain data, in the form of attributes, and code, in the form of functions known as methods. A distinguishing feature of objects is that an object's method can access and often modify the data attributes of the object with which they are associated (objects have a notion of "self"). In OO programming, computer programs are designed by making them out of objects that interact with one another.    

class Rectangle(): 
    def __init__(self, side_a, side_b):
        self.side_a = side_a
        self.side_b = side_b
        
    def area(self):
        return self.side_b * self.side_b


shape = Rectangle(10, 20)
print(shape.area())
