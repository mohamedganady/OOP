from datetime import date

class Student :
    def __init__(self,name,age,courses=None):
        self.name = name
        self.age = age
        self.courses = courses   
        

    def describe(self):
        print(f"my name is {self.name} and my age is {self.age}") 


    
    @classmethod
    def initFromBirthYear(cls,name,birthYear):
        return cls(name , date.today().year - birthYear)


student1 = Student("ali",25,"html")
student2 = Student.initFromBirthYear( "ahmed" , 1980)

student2.describe()

