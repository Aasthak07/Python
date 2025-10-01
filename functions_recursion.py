# Functions in Python
# A function is a block of code that is used to perform a specific task. It can be called by name to perform that task.

def sum(x, y):
    sum=x+y
    print(sum)
    return sum

sum(5, 6)
sum(10, 20)
sum(100, 200)

def mul(a,b):
    return a*b

multiplication = mul(5,6)
print(multiplication)

def print_hello():
    print("Hello World")

print_hello()   
print_hello()
print_hello()

output = print_hello()
print(output)  # None

# average of three numbers
def avg(a, b, c):
    return (a+b+c)/3

print(avg(1,2,3))
print(avg(10,20,30))
print(avg(100,200,300))

print("apnacollege","aastha") #seprator
print("apnacollege","aastha", sep="*") #seprator
print("aastha")
print("aastha", end=" ")

# Defaults parameters

def div(a, b=2): # b is a default parameter always at the end
    return a/b

print(div(10))
print(div(10, 5))

# waf to print the length of a list.(list is the parameter)


cities=["delhi", "mumbai", "chennai", "kolkata"]
heroes=["ironman", "thor", "hulk", "captain america"]
def length(lst):
    return len(lst)

print(length([1,2,3,4,5]))
print(length(cities))
print(length(heroes))

# waf to print thr element of a list in a single line (list is the parameter)

print(cities[0], cities[1], cities[2], cities[3])

print(*cities) #unpacking operator

def print_list_length(lst):
    print(len(lst))

def print_list_elements(lst):
    for i in lst:
        print(i, end=" ")    

print_list_length(heroes)
print_list_elements(heroes)
print()

# waf to find the factorial of a number( n is the parameter)

def factorial(n):
    return 1 if (n==1 or n==0) else n*factorial(n-1)

print(factorial(5))

def cal_fact(n):
    fact=1
    for i in range(n):
        fact=fact*(i+1)
    return fact

print(cal_fact(3))

# waf to convert USD to INR (usd is the parameter)

def convert(usd):
    inr=usd*82
    # print(usd, "USD is", inr, "INR")
    return inr

print(convert(1))

# take a input from the user and find out even or odd (n is the parameter)
n=int(input("Enter a number: "))
def even_odd(n):
    if n%2==0:
        return "Even"
    else:
        return "Odd"

print(even_odd(n))

# Recursion
# A function that calls itself is known as a recursive function.    
# A recursive function is a function that calls itself directly or indirectly.

def show(n):
    print(n)

show(5)  

def show_rec(n):
    if(n==0):
        return
    print(n)
    show_rec(n-1)
show_rec(5)  

# solve factorial using recursion
def fact_rec(n):
    if n==0 or n==1:
        return 1
    return n*fact_rec(n-1)

print(fact_rec(5))

# write a recursive function to claculate the sum of first n natural numbers.

def sum_natural(n):
    if n==1:
        return 1
    return n+sum_natural(n-1)

print(sum_natural(5))


# write a recursive function to print all elements in a list.
#hint : use list & index as parameters

# def print_list(lst):
#     if len(lst)==0:
#         return
#     print(lst[0])
#     print_list(lst[1:])  

# print_list([1,2,3,4,5])

def print_list(lst, index=0):
    if index==len(lst):
        return
    print(lst[index])
    print_list(lst, index+1)

fruits=["apple", "banana", "cherry", "date"]
print_list(fruits)