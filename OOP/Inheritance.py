class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display(self):
        return f"name is {self.name} and age is {self.age}"
    


class Man(Person):
    gender = 'Male'

    def __init__(self,name,age,voice):
        super().__init__(name,age)
        self.voice = voice

    def display(self):
        string = super().display()
        return string + f"name is {self.voice}"
    

man = Man("ali", 30 , "hard")
print(man.display())