class Math:

    @staticmethod
    def add(x,y):
        return x + y
    
    @staticmethod
    def add5(num):
        return num + 5
    
    @staticmethod
    def PI():
        return 3.14
    
X = Math.add(5,3)
y= Math.add5(7)
#print(X , y)






class Pizza:

    def __init__(self, radius , ingredients):
        self.radius = radius
        self.ingredients = ingredients


    def __str__(self):                                             #dunder function
        return f'pizza ingredients are {self.ingredients}'
    
    def area(self):
        return Pizza.circle_area(self.radius)
    

    @staticmethod
    def circle_area(r):
        return r**2 *Math.PI()
    
p = Pizza(6 , ['tomatoes','mozzarella'])
print(p.area())
print(Pizza.circle_area(4))
    