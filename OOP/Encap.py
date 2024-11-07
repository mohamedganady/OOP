#when i want to implement Encapsulation we must do setter and getter function

class Student :
    def __init__(self,name,age,courses):
        self.__name = name
        self.__age = age
        self.__courses = courses   

    
    def get_name(self):                   #from getter and setter we apply Encapsulation to attributes name
        return self.__name
    
    def set_name(self,new_name):
        self.__name = new_name


    def get_age(self):                   #from getter and setter we apply Encapsulation to attributes name
        return self.__age
    
    def set_age(self,new_age):
        self.__age = new_age

        

    def describe(self):
        print(f"my name is {self.__name} and my age is {self.__age}") 


    def check_age(self , num):
        if self.__age>num:
            print("the student is old")
        else :
            print("the student is not old")


student1 = Student("ali",25,"html")




print(student1.get_name())
student1.set_name("ahmed")
print(student1.get_name())
student1.name="ibreamin"
print(student1.get_name())
student1.set_age(50)
student1.describe()