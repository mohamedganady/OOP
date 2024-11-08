#Enforce a Contract: They ensure that all subclasses provide implementations for the specified methods, which is useful for consistency.

from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


    @abstractmethod
    def perimeter(self):
        pass



class Square(Shape):
    def __init__(self, side):    #side called attributes
        self.__side=side


    def area(self):
        return self.__side * self.__side
    
    def perimeter(self):
        return self.__side *4
    

class Rectangle(Shape):
    def __init__(self,length,width):
        self.__length=length
        self.__width = width  

    def area(self):
        return self.__width * self.__length
    
    def perimeter(self):
        return (self.__length + self.__width ) * 2




square = Square(10)
rect = Rectangle(2 , 5)
print(square.area())
print(rect.area())