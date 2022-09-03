import random

the_guess = int(input("I'm thinking of a number between 1 and 20\nTake a guess: "))

the_number = random.randint(1, 20)

while the_number != the_guess:
    if the_guess > the_number:
        the_guess = int(input("Your guess was too high!\nTry again: "))
    elif the_guess < the_number:
        the_guess = int(input("Your guess was too low!\nTry again: "))
    else:
        break

print("Congrats!!! You guessed the number!")

