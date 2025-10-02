#OOPS in python
# Object-Oriented Programming (OOP) is a programming paradigm that provides a way to create and manipulate objects, which are instances of classes.
# In Python, OOP is implemented using classes, methods, attributes, and inheritance.
# A class is a blueprint for creating objects, which are instances of that class.
# A class is a template(blueprint) for creating objects, which are instances of that class.

class StudentBasic:
    name = "aastha"
    age = 20

s1= StudentBasic()
print(s1)
print(s1.name)
print(s1.age)

class Car:
    color = "red"
    model = "bmw"

c1=Car()
print(c1.color)
print(c1.model)

#constructor//__init__ function
# 

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age    

s1=Student("aastha",20)
print(s1.name, s1.age) 

s2=Student("karan",20)
print(s2.name, s2.age)

# class & Instance Attributes

class Student2:
    college = "apna college"
    

    def __init__(self, name, age):
        self.name = name
        self.age = age

s1=Student2("ma",20)
print(s1.name, s1.age)


# Methods in Python
# A method is a function that is associated with a class and is used to perform actions on objects of that class.

class Student3:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

    def get_marks(self):
        return self.marks    

s1=Student3("aastha",20, 97)
s1.display()
print(s1.get_marks())

#1 create student class that takes name and marks of 3 subject as arguments in consructor. Then create a method to print the average.

class Student4:
    @staticmethod #decorator
    def hello():
        print("hello")
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        return sum(self.marks)/len(self.marks)
    
s1=Student4("aastha", [10,20,30])
print(s1.get_avg()) 

s1.name ="ironman"
s1.get_avg()


# Static methods in Python
# A static method is a method that is associated with a class and is not associated with any particular object of that class.
class Student5:
    @staticmethod      
    def hello():
        print("hello")

# Abstraction method in python
# Abstraction is a process of hiding the implementation details and showing only the necessary information to the user.
# 
class Machine:
    def __init__(self):
        self.acc = False
        self.brake = False
        self.clutch = False

    def start(self):
        self.clutch = True
        self.acc = True
        print("car started...")

car1= Machine()
car1.start()  


#Encapsulation method in python
# Encapsulation is a process of hiding the implementation details and showing only the necessary information to the user.

# Create account class with 2 attributes - balance and account no. 
# create method for debit, credit & printing the balance


class Account:
    def __init__(self, balance, account_no):
        self.balance = balance
        self.account_no = account_no

    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount, "has been debited from your account")
        print("Your current balance is Rs.", self.balance)

    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount, "has been credited to your account")
        print("Your current balance is Rs.", self.balance)

    def get_balance(self):
        return self.balance

    def get_account_no(self):
        return self.account_no

acc1 = Account(10000, "1234")
acc1.debit(500)
acc1.credit(9000)
print(acc1.get_balance())
print(acc1.get_account_no())
