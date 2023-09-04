# Author: Amin (Mavericane)
# Github Link: https://github.com/mavericane/
# Website Link: https://mavericane.ir
# Description: Bingo game(number guessing game) for single user playing with computer
# Importing required modules
# random module for selecting random choice
import random

# termcolor module for colorizing outputs
import termcolor

number = random.choice(range(0, 100 + 1))

print("I picked a number from 0 to 100 guess what is it. You have 5 chances")

chances = 10


def check_answer(guessnumber):
    if guessnumber > number:
        print("The number is lower than your last guess!")
    elif guessnumber < number:
        print("The number is higher than your last guess!")
    else:
        return True


while True:
    if chances >= 0:
        while True:
            while True:
                try:
                    guessnumber = int(input("What is your guess? "))
                    break
                except:
                    print("Enter a valid number")

            if guessnumber > 100 or guessnumber < 0:
                print("Enter a number between 0 and 100")
            else:
                break
        if check_answer(guessnumber):
            print(termcolor.colored("Bingo!", "green", "on_black"))
            exit()
        else:
            chances -= 1
            print(termcolor.colored(f"You have left {chances} chances", "red"))
    else:
        print(
            termcolor.colored(
                f"You couldn't guess number with 5 chances to guess. The number was {number}",
                "red",
                "on_black",
            )
        )
        exit()
