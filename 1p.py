print("hello world")
name="aastha"
age=20
price=45.67
a= None
old= False

print("my name is", name)
print(age)
print(price)

print(type(name))
print(type(age))
print(type(price))
print(type(a))  #<class 'NoneType'>
print(type(old)) # <class 'bool'>

# this is the output:
# <class 'str'>
# <class 'int'>
# <class 'float'>

a=10
b=20
c=a+b
print(c);

# this is single line comment
'''
this is multi line comment
'''

# arithemetic operators
# +, -, *, /, %, //, **

x=10
y=3 
print(x+y)  # addition
print(x-y)  # subtraction
print(x*y)  # multiplication
print(x/y)  # division
print(x%y)  # modulus  remainder 
print(x//y) # floor division
print(x**y) # exponentiation x^y

# relational operators / COMPARISON OPERATORS
# >, <, >=, <=, ==, !=

x=10    
y=20
print(x>y)   # greater than  # False
print(x<y)   # less than   #True 
print(x>=y)  # greater than equal to # False
print(x<=y)  # less than equal to    # True
print(x==y)  # equal to # False
print(x!=y)  # not equal to # True

#ASSIGNMENT OPERATORS
# =, +=, -=, *=, /=, %=, //=, **=
x=10    
y=20
x+=y  # x=x+y
print(x)  #30
x-=y  # x=x-y   
print(x)  #10
x*=y  # x=x*y   
print(x)  #200
x/=y  # x=x/y   
print(x)  #10.0
x%=y  # x=x%y   
print(x)  #10.0
x//=y  # x=x//y   
print(x)  #0.0
x**=y  # x=x**y   
print(x)  #10000.0

# logical operators
# and, or, not

x=False  
y=True
print(x and y)  # False
print(x or y)  # True
print(not x)   # True
print("hello")
print(not False)  
print(not True) 

# Tyepcasting/ Type conversion
# implicit typecasting and explicit typecasting is converting one data type to another data type forcefully
# implicit typecasting
x=10        
y=20.5
z=x+y  # int + float = float
print(z)  #30.5
# explicit typecasting
x=10        
y=20.5
z=int(x)+y  # int + float = float
print(z)  #30.5

# input function
# name=input("Enter your name: ")
# print("Hello", name)
# val=input("Enter a number: ")
# print("You entered", val) # this will be string
# print(type(val))  # <class 'str'>
# val=int(input("Enter something: "))

# add two numbers using input function
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
print("Sum is", a+b)

# WAP to find area of circle
r=float(input("Enter radius of circle: "))
area=3.14*r*r        
print("Area of circle is", area)