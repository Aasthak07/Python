#  LOOPS IN python
#  FOR LOOP
#  WHILE LOOP  
# 

count= 1
while count<=5:
    print("hello world",count)
    count+=1

print(count)  

# the difference between the iterator and iteration is that the iterator is an object that can be used to iterate over a sequence, while the iteration is the process of iterating over a sequence


# lets's practice 
#1 print the numbers from 1 to 100

i=1
while i<=100:
    print(i)
    i+=1
print("done")

#2 print the numbers from 100 to 1.
i=100
while i>=1: # or i>0 STOPPING CONDITION
    print(i)
    i-=1
print("done")

#3 print the elements of the following list using a loop:
list=[1,2,3,4,5,6,7,8,9,10]
index=0
while index<len(list):
    print(list[index])
    index+=1

 #4 search for a number x in this tuple using loop: 
 # if found print "found" else print "not found"
 
tuple = (1,4,9,16,25,36,49,64,81,100)
x=36
i=0
while i<len(tuple):
    if tuple[i]==x:
        print("found at index", i)
        break
    i+=1
else:
    print("not found")

 # 5 PRINT THE MULTIPLICATION OF TABLE NUMBER N
 
n = int(input("enter a number: "))
i=1
while i<=10:
    print(n*i)
    i+=1
print("done")     
  
# OR 
heroes= ["spiderman","batman","superman","ironman"]
i=0
while i<len(heroes):
    print(heroes[i])
    i+=1

   # Break and Continue Statement in Python
# Break Statement 

i=1
while i<=10:
    if i==5:
        break
    print(i)
    i+=1
print("done")    

  # Continue Statement
  # it skips the current iteration and moves to the next iteration
  # it is used to skip the current iteration of a loop and move to the next iteration
i=0
while i<10:
    i+=1
    if i==5:
        continue  #skips the current iteration when i is 5
    print(i)  


#Loops in Python
# A loop is a programming construct that allows you to repeat a block of code multiple times until 
# 
# for loop 
# The for loop in Python is used to iterate over a sequence (like a list, tuple, dictionary, set, or string) or other iterable objects.
# The for loop in Python is used to iterate over a sequence (like a list, tuple, dictionary, set, or string) or other iterable objects. 
# we can use else statement with for loop. The else block will be executed when the loop is finished normally, i.e., when the loop is not terminated by a break statement.
# 
  
list=[1,2,3,4,5]
for item in list:
    print(item) #a certain condition is met.

char="hello"
for c in char:
    print(c) 
else:
    print("done")

str= "apnaCollege"
for s in str:
    if s=="l":
        print("l is found")
        break
    print(s)
else:
    print("l is not found")


#question   Print the elements of the following list using a loop:  
# 
list=[1,4,9,16,25,36,49,64,81,100]
for item in list:
    print("item is:", item)    

tuple = (1,4,9,16,25,36,49,64,81,100)
x= int(input("enter a number to search: "))
for i in tuple:
    if i==x:
        print("found yes")
        break
else:
    print("not found")


# range() function in python
# The range() function in Python is used to generate a sequence of numbers. It can take one, two, or three arguments:
# range(stop): Generates numbers from 0 to stop-1.
# range(start, stop): Generates numbers from start to stop-1.
# range(start, stop, step): Generates numbers from start to stop-1, with a step size of step.
# The range() function is often used in for loops to generate a sequence of numbers.
# The range() function is often used in for loops to generate a sequence of numbers.
# The range() function is often used in for loops to generate a sequence of numbers.

#syntax of range()
#range(start, stop, step)

seq= range(5)
print(seq)  # it will print the range object
print(seq[0]) # it will print the first element of the range object
print(seq[1]) # it will print the second element of the range object
print(seq[2]) # it will print the third element of the range object
print(seq[3]) # it will print the fourth element of the range object
print(seq[4]) # it will print the fifth element of the range object

seq2= range(6)
for i in seq2:
    print(i)

for i in range(4): #range(stop)
    print(i)    

for i in range(1,11): # it will print the numbers from 1 to 10
    print(i)

for i in range(1,11,2): # it will print the numbers from 1 to 10 with a step of 2       (start, stop, step)
    print(i)    


for i in range(10,0,-1): # it will print the numbers from 10 to 1 with a step of -1
    print(i)

 #PRINT THE NUMBERS FROM 100 TO 1
for i in range(100,0,-1):
    print(i)   


# print the multiplication table of a given number n
n= int(input("enter a number: "))
for i in range(1,11):
    print("the multiplication of", n, "*", i, "is:", n*i) 


# pass statement in python
# The pass statement in Python is a null operation; it is used when a statement is required syntactically but you do not want any command or code to execute.
# The pass statement is often used as a placeholder for future code.       

for i in range(5):
    pass  # it does nothing

if True:
    pass  # it does nothing
print("it does nothing")


# wap to find the sum of first n natural numbers
n= int(input("enter a number: "))
sum=0
for i in range(1,n+1):
    sum+=i
print("the sum of first", n, "natural numbers is:", sum)

# write a program to print the factorial of a given number n
n= int(input("enter a number: "))
factorial=1
for i in range(1,n+1):
    factorial*=i
print("the factorial of", n, "is:", factorial)