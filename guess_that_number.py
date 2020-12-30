
# importing random module
from random import randint

# generating random number
random_number = randint(0,100)
random_number

# basic instructions
print("You, the player, must choose a random integer from 1 to 100. \nIf you choose the correct number, you win.")

# creating empty list for guesses
guesses = []
new_guess = int(input("Please guess a random integer between 1 and 100 \n"))
guesses.append(new_guess)

# while loop to carry out the rest of the game
while guesses[-1] != random_number:
    if guesses[-1] < 1 or guesses[-1] > 100: 
        print("OUT OF BOUNDS!")
        print("Input new guess")
        new_guess = int(input())
        guesses.append(new_guess)
    elif len(guesses) == 1: 
        if abs(random_number - guesses[0]) <= 10: 
            print("WARM! \n")
            print("Input new guess")
            new_guess = int(input())
            guesses.append(new_guess)
        else: 
            print("COLD! \n")
            print("Input new guess")
            new_guess = int(input())
            guesses.append(new_guess)
    elif len(guesses) > 1: 
        if abs(random_number - guesses[-1]) > abs(random_number - guesses[-2]):
            print("COLDER! \n")
            print("Input new guess")
            new_guess = int(input())
            guesses.append(new_guess)
        else:
            print("WARMER \n")
            print("Input new guess")
            new_guess = int(input())
            guesses.append(new_guess)
                  
else: 
    guess_count = len(guesses)
    print("You are correct! Yay!")
    print("You guessed {} times".format(guess_count))