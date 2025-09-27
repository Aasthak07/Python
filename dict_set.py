# DICTIONARY IN PYTHON
# DICTIONARY IS A COLLECTION OF KEY-VALUE PAIRS
# DICTIONARY IS MUTABLE
# DICTIONARY IS ORDERED
# DICTIONARY IS INDEXED
# DICTIONARY IS DEFINED IN CURLY BRACKET {}
# DICTIONARY CAN HAVE DUPLICATE KEYS
# DICTIONARY CAN HAVE DUPLICATE VALUES
# DICTIONARY CAN HAVE HETEROGENEOUS KEYS AND VALUES
# DICTIONARY CAN BE MODIFIED
# DICTIONARY CAN BE SLICED
# DICTIONARY CAN BE NESTED
# DICTIONARY CAN BE ITERATED
# DICTIONARY CAN BE CONCATENATED
# DICTIONARY CAN BE REPEATED
# DICTIONARY CAN BE CHECKED FOR MEMBERSHIP


info={
    "name":"aastha",
    "age":20,
    "city":"delhi" ,
    "country":"india",
}
print(type(info)) # <class 'dict'>
print(info) # {'name': 'aastha', 'age': 20, 'city': 'delhi', 'country': 'india'}

print(info["name"]) # aastha
print(info["age"]) # 20
print(info["city"]) # delhi
print(info["country"]) # india

info["name"]= "hasrsh"
info["surname"]= "sharma"
print(info) # {'name': 'hasrsh', 'age': 20, '
print(info["name"]) # hasrsh

null_dict={}
null_dict["hey"]="hello"
print(null_dict) # {'hey': 'hello'}
print(type(null_dict)) # <class 'dict'>

#Nested Dictionary

student={
    "name":"aastha",
    "age":20,
    "marks":{
        "maths":90,
        "science":95,
        "english":85
    }
}
print(student)
print(student["marks"]["science"]) # 95


# dictionary methods
print(len(student)) # 3
print(student.keys()) # dict_keys(['name', 'age', 'marks'])
print(list(student.keys())) # ['name', 'age', 'marks']
print(student.values()) # dict_values(['aastha', 20, {'maths':
print(list(student.values()))# ['aastha', 20, {'maths': 90, 'science': 95, 'english': 85}]
print(student.items()) # dict_items([('name', 'aastha'), ('age', 20), ('marks', {'maths': 90, 'science': 95, 'english': 85})])
print(list(student.items())) # [('name', 'aastha'), ('age', 20), ('marks', {'maths': 90, 'science': 95, 'english': 85})]

print(student.get("name")) # aastha
print(student.get("city")) # None
print(student["name"]) # aastha


# SET IN PYTHON

# SET IS A COLLECTION OF UNIQUE ELEMENTS
# SET IS MUTABLE but elements of set are immutable
# SET IS ORDERED    # SET IS UNORDERED
# SET IS INDEXED  # SET IS UNINDEXED
# SET IS DEFINED IN CURLY BRACKET {}
# SET CAN HAVE DUPLICATE ELEMENTS
# SET CAN HAVE HETEROGENEOUS ELEMENTS
# SET CAN BE MODIFIED
# SET CAN BE SLICED
# SET CAN BE NESTED
# SET CAN BE ITERATED

#list and dict cannot be stored in set because they are mutable and unhashable
# TUPLE CAN BE STORED IN SET BECAUSE THEY ARE IMMUTABLE AND HASH

collection={1,2,3,4,5,5,5,5,6,7,8,9,9,9,"hello","hello","hello",(1,2),(1,2)}
print(collection)
print(type(collection)) # <class 'set'>
print(len(collection)) # 11
# print(collection[0]) # TypeError: 'set' object is not subscriptable
null_collection=set() # empty set; synatx to create empty set
print(type(null_collection)) # <class 'set'>

# set methods
# print(dir(collection))
collection1= set()
collection1.add(10)
collection1.add(20)
collection1.add(30)
collection1.add(40)
collection1.add(10) # duplicate element will not be added
collection1.add("hello")
collection1.add("world")
collection1.add((1,2,3,4,5)) # tuple can be added
# collection1.add([1,2,3,4,5]) # list cannot be added
# collection1.add({1: "hello", 2: "world"}) # dictionary cannot be added
print(len(collection1)) # 5
print(collection1) # {40, 10, 20, 30}
# collection1.clear() # clears the set
print(collection1) # set()
print(collection1.pop())
print(collection1.pop())


# SET IS IMMUTABLE CAN BE HASH VALUE (FIXED)

set1={1,2,3,4,5}
set2={4,5,6,7,8}
print(set1.union(set2)) # {1, 2, 3, 4, 5, 6, 7, 8}
print(set1.intersection(set2)) # {4, 5}


#lets practice
# store the following word meaning in a dictionary and print them

dict2={
    "table":"a piece of furniture with a flat top and one or more legs",
    "cat":"a small domesticated carnivorous mammal with soft fur, a short snout, and retractile claws",
    "python":"a large heavy-bodied nonvenomous constrictor snake occurring throughout the Old World tropics",
    "price": 1000,
    "is_good": True,
}
print(dict2)
print(dict2["table"])
print(dict2["cat"])
print(dict2["python"])
print(dict2["price"])
print(dict2["is_good"])

#     OR

dict3={

    "cat": "cutiee",
    "table": ["wooden", "iron", "plastic", "furniture"],

}
print(dict3)
print(dict3["cat"]) # cutiee


# you are given a list of subjects for students. assume one classroom is required for 1 subject. how many classrooms are neede by all students
subjects=["python","java","c","c++","html","css","javascript","python","java","c","c++","html","css","javascript"]
print(subjects) # ['python', 'java', 'c', 'c++', 'html', 'css', 'javascript', 'python', 'java', 'c', 'c++', 'html', 'css', 'javascript']
print(set(subjects)) # {'c++', 'css', 'html', 'python', 'c', 'java', 'javascript'}
print("the number of classroom",(len(set(subjects)))) # 7

##OR
print(len(subjects)) # 14
unique_subjects=set(subjects)
print(unique_subjects) # {'c++', 'css', 'html', 'python', 'c', 'java', 'javascript'}
print(len(unique_subjects)) # 7
print(f"number of classrooms needed: {len(unique_subjects)}") # number of classrooms needed: 7


#3 wap to enter marks of 3 subjects from the user and store them in a dictionary and print the dictionary. start with an empty dictionary and add one by one. use subjects name as key & marks as value.
marks={}
marks1=int(input("enter marks of subject 1: "))
marks2=int(input("enter marks of subject 2: "))
marks3=int(input("enter marks of subject 3: "))
marks["phy"]=marks1
marks["chem"]=marks2
marks["maths"]=marks3
print(marks)

#or
m1={}
x=int(input("enter marks of phy: "))
m1.update({"phy":x})
y=int(input("enter marks of chem: "))
m1.update({"chem":y})
z=int(input("enter marks of maths: "))
m1.update({"maths":z})
print(m1)

#4 figure out a way to store 9 & 9.0 as separate values in the set.(you  can take help of built in functions)

values={9,9.0} # 9 and 9.0 are considered same in set because they have same hash value , you cant store "9.0" as string because it is different from 9
print(values) # 9

#you can store as tuple
valu={
    ("float",9.0),
    ("int",9),
}
print(valu) # {('int', 9), ('float', 9.0)}
