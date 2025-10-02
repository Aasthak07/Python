# File I/O in Python
# File I/O is the process of reading and writing data to and from files in a computer system.
# File I/O is a fundamental concept in computer programming that allows you to interact with external storage devices, such as hard drives, flash drives, or memory cards, to read and write data.

# There are two main types of file I/O in Python:
# Reading from a file
# Writing to a file

# open, read & close

# reading a file


# f=open("demo.txt", "r")
# print(f.read(3))
# print(type(f))
# f.close

# f1= open("demo.txt", "r")
# data = f1.read()
# print(data)

# line1 = f1.readline()
# print(line1)

# line2 = f1.readline()
# print(line2)

# line5= f1.readlines()
# print(line5)

# f1.close

# # writing to a file  # overwrite
# f2= open("demo.txt", "w")
# f2.write("this is a new line")
# f2.close

# # appending to a file
# f3= open("demo.txt", "a")
# f3.write("\nthis is a new line")
# f3.close

# f4= open("sample.txt", "w")
# f4.close() # it creates a new file which doesnt exist

# # r+ mode
# f5= open("sample.txt", "r+")
# f5.write("it is a new line")
# f5.close

# # w+ mode read and write and trunacte
# f6= open("sample.txt", "w+")
# f6.write("it is a new line")
# f6.close

# # a+ mode append and read
# f7= open("sample.txt", "a+")
# f7.write("it is a new line")
# f7.close

# WITH SYNTAX
with open("demo.txt", "r") as f8:
    data= f8.read()
    print(data)

# with open("demo.txt", "w") as f8:
#     f8.write(" new data")



# Deleting a file 

# import os
# os.remove("sample.txt")

# Renaming a file

# import os
# os.rename("demo.txt", "demo1.txt")

# ques. 1 create a new file "practice.txt" using python. add the following data 
# Hi everyone
# we are learning file i/o 
# using java.
# i like programming in java

with open("practice.txt", "w") as f9:
    f9.write("Hi everyone\n")
    f9.write("we are learning file i/o \n")
    f9.write("using java.\n")
    f9.write("i like programming in java\n")

# waf that replace all occurences of "java" with "python" in above created file. 
# 

with open("practice.txt", "r") as f10:
    data= f10.read()
    print(data)

new_data= data.replace("java", "python")
print(new_data) 

with open("practice.txt", "w") as f11:
     f11.write(new_data)


# search the word "learning" exist in the file or not.

def check_for_word():
    word = "learning"
    with open("practice.txt","r") as f12:
        data = f12.read()
        if data.find(word) != -1:
            print("word found")
        else:
            print("word not found")

check_for_word()
def check_for_line():
    word ="learning"
    data = True
    line_no = 1
    with open("practice.txt","r") as f13:
        while data:
            data = f13.readline()
            if(word in data):
                print(line_no)
                return 
            line_no += 1  

    return -1

check_for_line()          

# From a file containing numbers separated by comma, print the count of even numbers. 1,2,45,55, 86, 76

with open("example.txt","r") as f:
    data = f.read()
    print(data)

    # num = ""
    # for i in range (len(data)):
    #     if data[i] == ",":
    #         print(int(num))
    #         num = ""
    #     else:
    #         num += data[i]

    num = data.split(",")
    print(num)

    count = 0
    for i in range(len(num)):
        if int(num[i]) % 2 == 0:
            count += 1
    print(count)
            



    