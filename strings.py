
# TO RUN THIS FILE WITH NODEMON USE THE COMMAND
# nodemon --exec "python lecture2.py"

#string

str1="hello"
str2='world'
str3='''this is a multi line
string'''
# 'this is apnacollege's class'  # error
"this is apnacollege's class"  # correct

print(str1 + " " + str2)  # concatenation
print(str3)
len1=len(str1)
print(len1)
final_str=str1 + " " + str2 
print(final_str)
print(len(final_str))

# indexing 
print(final_str[0])  # h
print(final_str[1])  # e
print(final_str[2])  # l    
print(final_str[-1])  # l    
print(final_str[-2])  # e


str4="apna college"
# str[4]='A'  # error, string is immutable
# print(str4)
# str object does not support item assignment

#slicing
# str[start:end] ending index is not included  () bicch ka tukda return karta hai)
print(str4[0:4])  # apna
print(str4[0:])  # apna college
print(str4[:5])  # apna c
print(str4[:])  # apna college  
print(str4[0:-1])  # apna college
print(str4[0:11:2])  # an olge
print(str4[::2])  # an olge
print(str4[::3])  # a oec
print(str4[::-1])  # egelloc anpa
print(str4[5 :len(str4)])  # college
print(str4[-7:-1])  # college
print(str4[5:])  # college
print(str4[-7:])  # college

# string methods
print(str4.upper())  # APNA COLLEGE
print(str4.lower())  # apna college
print(str4.title())  # Apna College
print(str4.capitalize())  # Apna college
print(str4.swapcase())  # APNA COLLEGE

#string functions
str5="   apna college   "
print(str5.strip())  # apna college
print(str5.lstrip())  # apna college   (left strip) 
print(str5.rstrip())  #   apna college (right strip)    
print(str5.replace("a","A"))  #   ApnA college   
print(str5.replace("apna","my"))  #   my college   
print(str5.split())  # ['apna', 'college']  
print(str5.split(" "))  # ['apna', 'college']   
print(str5.split(","))  # ['   apna college   ']    
print(str5.split(","))  # ['   apna college   ']
print(str5.split("a"))  # ['   ', 'pn', ' college   ']
print(str5.split("e"))  # ['   apna coll', 'g', '   ']
print(str5.count("a"))  # 2
print(str5.count("college"))  # 1
print(str5.capitalize())  # Apna college
print(str5.find("college"))  # 7 (starting index of the substring)

print(str5.find("z"))  # -1 (substring not found)
print(str5.index("college"))  # 7 (starting index of the substring)

#WAP TO INPUT USER'S FIRST NAM & PRINT ITS LENGTH.

# first_name= input("enter the first name:")
# print("the length of the first name is:", len(first_name))

#Wap to find the occurence of '$' in the string "I am a $ student of apna college and I have $ 1000"
str6="I am a $ student of apna college and I have $ 1000"
print( "the occurence of $ is:",str6.count("$"))


#conditional statements
# if, if-else, if-elif-else

age=21
if age>=18:
    print("you are eligible to vote") #tab== 4 spaces for indentation
print("thank you")  # no indentation, always executes

age=17
if age>=18:
    print("you are eligible to vote")   
elif age==17:
    print("you will be eligible next year")


num=10
if num>0:
    print("number is positive")
elif num<0:
    print("number is negative")
else:
    print("number is zero")

marks= int(input("enter your marks:"))
if marks>=90:
    print("grade A")
elif marks>=80 and marks<90:
    print("grade B")
elif marks>=70 and marks<80:
    print("grade C")
elif marks>=60 and marks<70:
    print("grade D")
else:
    print("grade F")


#nesting of conditional statements
age = 34
if age>=18:
    print("you are eligible to vote")
    if age>=65:
        print("you are senior citizen")
    else:
        print("you are not a senior citizen")

else:
    print("you are not eligible to vote")  


    # wap to calculate even or odd
    # 
num= int(input("enter the number:"))
if num%2==0:
    print("number is even")
else:
    print("number is odd") 

    # wap to check the gretatest of 3 numbers
num1= int(input("enter the first number:"))
num2= int(input("enter the second number:"))
num3= int(input("enter the third number:"))
if num1>num2 and num1>num3:
    print("num1 is greatest")
elif num2>num3:
    print("num2 is greatest")
else:
    print("num3 is greatest") 