# del keyword
# used to delete a variable or an object properties or object itself

class StudentBasic:
    def __init__(self, name):
        self.name = name
        
s1 = StudentBasic("aastha")
print(s1.name)
del s1
# print(s1.name)

# print(s1) NameError: name 's1' is not defined

# private(like) attributes & methods

class Account:
    def __init__(self, account_no, account_password):
        self.account_no = account_no
        self.__account_password = account_password # double space for private attribute__

    def reset_password(self):
        print(self.__account_password)
            

acc1=Account(1234, "abcd")
print(acc1.account_no)
# print(acc1.__account_password)   #AttributeError: 'Account' object has no attribute '__account_password  
print(acc1.reset_password())  


class Person:
    __name = "anonymous"

    def __hello(self, name):
        print("hello person")  #AttributeError: 'Person' object has no attribute '__name'

    def welcome(self):
        self.__hello(self.__name)  


p1 = Person()
print(p1.welcome())


# INHERITANCE in python
# Inheritance is a concept in object-oriented programming (OOP) that allows a class to inherit properties and methods from another class.
# The class that inherits from another class is called a subclass, and the class that is inherited from is called a superclass.

class Car:
    color = "red"
    @staticmethod
    def start():
        print("car started...")

    @staticmethod
    def stop():
        print("car stopped...")

class ToyoraCar(Car):  
    def __init__(self, name):
        self.name = name

car1 = ToyoraCar("fortuner") 
car2 = ToyoraCar("thar")
print(car1.name)
print(car2.start()) 
print(car1.color)  

#MULTILEVEL INHERITANCE

class Cars:
    color = "red"
    @staticmethod
    def start():
        print("car started...")

    @staticmethod
    def stop():
        print("car stopped...")

class Hyundai(Cars):
    def __init__(self, brand):
        self.brand = brand

class Fortuner(Hyundai):
    def __init__(self, type):
        self.type = type 

car1 = Fortuner("diesel") 
car1.start()


# MULTIPLE INHERITANCE

class A:
    varA = "welcome to class A"

class B:
    varB = "welcome to class B"

class C(A, B):
    varC = "welcome to class C" 

c1 = C()
print(c1.varA)
print(c1.varB)
print(c1.varC)       
       

# SUPER METHOD
# The super() function returns an object that represents the parent class.

class Mars:
    def __init__(self, type):
        self.type = type
    @staticmethod
    def start():
        print("mars started...") 

    @staticmethod
    def stop():
        print("mars stopped...")

class Toyota(Mars):
    def __init__(self, name, type):
        self.name = name
        super().__init__(type)
        super().start()
        
        

mars1 = Toyota("fortuner", "diesel")
print(mars1.type) 


class Person1:
    name="anonymous"
    # def changeName(self, name):
        # self.name = name
        # Person1.name = name
        # self.__class__.name = name  # same as above line
    @classmethod
    def changeName(cls, name):
        cls.name = name
p1 = Person1()
p1.changeName("Shreya") 
print(p1.name)
print(Person1.name)

# INSTANCE METHOD
# A method that is associated with an instance of a class. It can access and modify the instance's attributes and other methods.
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} is barking"

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

dog1 = Dog("Buddy", 3)
print(dog1.bark())
print(dog1.get_age())
dog1.set_age(4)
print(dog1.get_age())

# @property decorator

class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math
        # self.percentage = str((phy + chem + math) / 3) + "%"

    # def clacPercentage(self):
    #     self.percentage = str((self.phy + self.chem + self.math) /3) + "%" 
    @property
    def percentage(self):
        return str((self.phy + self.chem + self.math) /3) + "%"  

stu1 = Student(90, 80, 70)
print(stu1.percentage)  # 80.0% 

stu1.phy = 100
print(stu1.phy)  # 80.0%

print(stu1.percentage)  # 80.0%  # still 80.0% not updated




       


        