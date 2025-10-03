#polymorphism in python
# Polymorphism is a concept in object-oriented programming (OOP) that allows objects of different classes to be treated as objects of a common superclass.
# It enables a single interface to represent different underlying forms (data types).
# Polymorphism is a fundamental concept in object-oriented programming and is used to implement inheritance, method overriding, and dynamic dispatch.
# 2 more decorators @getter and @setter

#operator overloading
# operators & Dunder functions
# Dunder functions are special methods in Python that have double underscores at the beginning and end of their names.
# These methods are also known as magic methods or special methods.

print(5 + 6)  #11 addition
print(type(5))  #int
print("5" + "6")  # concatenation
print(type("5"))  #str   
print([5,4,3] + [6,1,32,5])  # list concatenation
print(type([5,4,3]))  #list
print((5,4,3) + (6,1,32,5))  # tuple concatenation
print(type((5,4,3)))  #tuple

class Complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
    def shownumber(self):
        print(self.real,"i +" , self.imaginary,"j") 

    def add(self, num2):
        newReal = self.real + num2.real
        newImaginary = self.imaginary + num2.imaginary
        return Complex(newReal, newImaginary) 
    def __sub__(self, num2):   # operator overloading for - operator
        newReal = self.real - num2.real
        newImaginary = self.imaginary - num2.imaginary
        return Complex(newReal, newImaginary)
num1 = Complex(5,3) 
num1.shownumber()

num2 = Complex(2,2)
num2.shownumber()

num3= num1.add(num2)
# num3= num1 + num2  # this will give error as + operator is not defined for Complex class
num3.shownumber()

num4= num1 - num2  # this will work as - operator is overloaded for Complex class
num4.shownumber()

# practice question
# define  a circle class to create a circle with radius using the constructor. Define an area() method of the class which calculates the area of the circle. define a perimeter() method of the class which allows you to calculate the perimeter of the circle. Use the value of pi as 3.14

class Circle:
    pi = 3.14
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return Circle.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * Circle.pi * self.radius

c1 = Circle(21) 
print(c1.area())
print(c1.perimeter()) 

# Define a Employee class with attributes role, department & salary. This class also has showDetails() method.
     #Create an Engineer class that inherits properties from employee and also has attribute : name & age.

class Employee:
    def __init__(self, role, department, salary):
        self.role = role
        self.department = department
        self.salary = salary

    def showDetails(self):
        print("Role:", self.role)
        print("Department:", self.department)
        print("Salary:", self.salary)

class Engineer(Employee): 
    def __init__(self, name, age, role, department, salary):
        super().__init__(role, department, salary)  # calling parent class constructor  
        self.name = name
        self.age = age
        super().__init__(role, department, salary)


e1 = Employee("Manager", "Sales", 75000)
print(e1.showDetails())

eng1 = Engineer("Alice", 30, "Software Engineer", "Development", 90000)
print(eng1.showDetails())

# Create a class called order which stores item & its price.
#   use Dunder function __gt__() to convey that:
#    order1 > order2 if order1's price is greater than order2's price

class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self, ord2):
        return self.price > ord2.price
    

ord1 = Order("laptop", 50000)
ord2 = Order("phone", 30000)
print(ord1 > ord2)  # True
print(ord2 > ord1)  # False    




