######  RANDOM PASSWORD GENERATOR  ######


import random
import string

# print(string.ascii_letters)
# print(string.digits)
# print(string.punctuation)
pass_length = 8
characters = string.ascii_letters + string.digits + string.punctuation

# print(characters)
# print("Welcome to the Password Generator!")
# length = int(input("Enter the length of the password: "))

#list comprehension [function for item in iterable range(n)]

password = ''.join(random.choice(characters) for i in range(pass_length))



password_str = ""
for i in range(pass_length):
    password_str += random.choice(characters)  # to print a random character from the characters string

print("Your password is: ", password_str)    




