#conditional loop
'''import random

comp_guess = random.randint(1, 3)

guess = int(input("enter your guess: "))

if guess < comp_guess:
    print("guess is too low.")
elif guess > comp_guess:
    print("guess is too high.")

else:
    print("you won!")

#while loop.
'''

import random

comp_guess = random.randint(1, 10)
guess = None

while guess != comp_guess:
    guess = int(input("Enter your guess: "))
    
    if guess < comp_guess:
        print("Guess is too low.")
    elif guess > comp_guess:
        print("Guess is too high.")
    else:
        print("You won!")
