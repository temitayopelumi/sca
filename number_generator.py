import random
import math

x = random.randint(0,21)
guess = int(input("Guess a number:- ")) 
while True:
        # Condition testing
    if x == guess:  
        print("Congratulations, you're correct")
        break

    elif x > guess:
        print("You Guessed too small!")
        guess = int(input("Guess an higher number:- ")) 
    else:
        print("You Guessed too high!")
        guess = int(input("Guess a lower number:- ")) 
