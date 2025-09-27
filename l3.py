# LIST IN PYTHON
# LIST IS A COLLECTION OF HOMOGENEOUS ELEMENTS
# LIST IS MUTABLE
# LIST IS ORDERED
# LIST IS INDEXED
# LIST IS DEFINED IN SQUARE BRACKET []
# LIST CAN HAVE DUPLICATE ELEMENTS
# LIST CAN HAVE HETEROGENEOUS ELEMENTS
# LIST CAN BE MODIFIED
# LIST CAN BE SLICED
# LIST CAN BE NESTED
# LIST CAN BE ITERATED
# LIST CAN BE CONCATENATED
# LIST CAN BE REPEATED
# LIST CAN BE CHECKED FOR MEMBERSHIP

MARKS=[10,20,30,40,50]
print(MARKS)
print(type(MARKS))  #<class 'list'>
print(id(MARKS))    #140703823682560
print(len(MARKS))   #5
print(MARKS[0])     #10
print(MARKS[-1])    #50

#list can have duplicate element and different type of elements
DATA=[10,20,30,40,50,10,20,30,40,50]
print(DATA) # [10, 20, 30, 40, 50, 10, 20, 30, 40, 50]
MIXED=[10,20.5,'Hello',True,10,20.5,'Hello',True]
print(MIXED) # [10, 20.5, 'Hello', True, 10, 20.5, 'Hello', True]
NESTED=[10,20,[30,40,50],60,70]
print(NESTED) # [10, 20, [30, 40, 50], 60, 70]

#list can be modified
MARKS[0]=100
print(MARKS) # [100, 20, 30, 40, 50]    

#list can be sliced
print(MARKS[0:3]) # [100, 20, 30]
print(MARKS[:3])  # [100, 20, 30]
print(MARKS[2:])  # [30, 40, 50]    
print(MARKS[:])   # [100, 20, 30, 40, 50]

#list methods
#1. append() - to add an element at the end of the list
MARKS.append(60)
print(MARKS) # [100, 20, 30, 40, 50, 60]

#2. insert() - to add an element at a specific index
MARKS.insert(2,70)
print(MARKS) # [100, 20, 70, 30, 40, 50, 60]

#3. remove() - to remove an element from the list
MARKS.remove(70)
print(MARKS) # [100, 20, 30, 40, 50, 60]

#4. pop() - to remove an element from the end of the list
MARKS.pop()
print(MARKS) # [100, 20, 30, 40, 50]

#5. count() - to count the number of occurrences of an element in the list
MARKS.count(20) # 1
print(MARKS.count(20)) # 1

#6. index() - to find the index of an element in the list
print(MARKS.index(30)) # 2


list1 = [2,1,3]
print(list1.sort()) # None      # sort method returns None
print(list1) # [1, 2, 3]


#TUPLE IN PYTHON
# TUPLE IS A COLLECTION OF HOMOGENEOUS ELEMENTS
# TUPLE IS IMMUTABLE
# TUPLE IS ORDERED
# TUPLE IS INDEXED
# TUPLE IS DEFINED IN ROUND BRACKET ()
# TUPLE CAN HAVE DUPLICATE ELEMENTS
# TUPLE CAN HAVE HETEROGENEOUS ELEMENTS
# TUPLE CAN BE MODIFIED (ONLY BY REASSIGNMENT)
# TUPLE CAN BE SLICED
# TUPLE CAN BE NESTED
# TUPLE CAN BE ITERATED
# TUPLE CAN BE CONCATENATED
# TUPLE CAN BE REPEATED
# TUPLE CAN BE CHECKED FOR MEMBERSHIP

tup=(2, 1, 3, 4, 5, 6)
tup1=()
print(tup) # (2, 1, 3, 4, 5, 6)
print(type(tup)) # <class 'tuple'>
print(id(tup)) # 140703823682560
print(len(tup)) # 6
print(tup[0]) # 2   
print(tup[-1]) # 6
print(tup1) # ()
print(type(tup1)) # <class 'tuple'>

tup3=(2,) # single element tuple
print(tup3) # 2
print(type(tup3)) # <class 'int'>
tup4=(2,) # single element tuple
print(tup4) # (2,)
print(type(tup4)) # <class 'tuple'>


# tuple questions
# WAP TO TAKE 3 MOVIE NAMES AS INPUT FROM THE USER AND STORE THEM IN A LIST.
# CONVERT THE LIST INTO A TUPLE AND PRINT THE TUPLE.

list2= []
movie1= str(input("Enter a string as FIRST movie name: ")) 
movie2= str(input("Enter a string as  SECOND movie name: "))
movie3= str(input("enter a string as third movie name:"))
list2.append(movie1)
list2.append(movie2)
list2.append(movie3)
print(list2) # ['Inception', 'Avatar', 'Titanic']
tuple1= tuple(list2)
print(tuple1) # ('Inception', 'Avatar', 'Titanic')

#wap to check if a list contains a palindrome element or not

list3= ['hello', 'madam', 'world', 'python', 'level']
flag= False
for item in list3:
    if item==item[::-1]:
        flag=True
        break
if flag:
    print("List contains a palindrome element")
else:
    print("List does not contain a palindrome element")


    list4= [1, 2,3,2,1]
    list5=[1,2,3,4,5]
    copy_list4= list4.copy()
    copy_list4.reverse()
    if copy_list4==list4:
        print("list4 is a palindrome")
    else:
        print("list4 is not a palindrome")


    # wap to count the number of students with the A grade in the following tuple. and store them in alist & sort them from A to D
    
    tuple= {'John': 'A', 'Jane': 'B', 'Jim': 'A', 'Jake': 'C', 'Jill': 'A'}
    grade_list= []
    for key, value in tuple.items():
        if value=='A':
            grade_list.append(key)
    print(grade_list)
    grade_list.sort()
    print(grade_list) # ['Jake', 'Jane', 'Jill', 'Jim', 'John']
    print(len(grade_list)) # 3
    
    