class Student :
    def __init__(self,name,age,courses):
        self.name = name
        self.age = age
        self.courses = courses   

    def describe(self):
        print(f"my name is {self.name} and my age is {self.age}") 


    def check_age(self , num):
        if self.age>num:
            print("the student is old")
        else :
            print("the student is not old")


student1 = Student("ali",25,"html")
student2 = Student("ahmed",35,"html")
student3 = Student("noha",21,"css")
#print(id(student1), id(student2))

print(f"my name is {student1.name} and my age is {student1.age}")   

student1.describe()
student1.check_age(40)
       