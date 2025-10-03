#########  GUESS THE NUMBER #########


import random

target = random.randint(1, 100)

while True:
    userChoice = input("Enter your guess  or Quit(Q): ")
    if userChoice == "Q" or userChoice == "q":
        break
    try:
        guess = int(userChoice)
    except ValueError:
        print("Please enter a valid number or Q to quit.")
        continue
    if guess == target:
        print("You guessed it right!")
        break
    elif guess < target:
        print("Too low! Try a bigger number again.")
    else:
        print("Too high! Try a smaller number again.")

print("Thank you for playing!")    