# Author: Amin (Mavericane)
# Github Link: https://github.com/mavericane/
# Website Link: https://mavericane.ir
# Description: Hangman game(guessing words with guessing letters) for single user playing with computer
# Importing required modules
# random module for selecting random choice
import random

# termcolor module for colorizing outputs
import termcolor

# list of words that the computer can randomly pick for the user to guess
words = [
    "computer",
    "android",
    "linux",
    "motherboard",
    "object",
    "python",
    "skywalker",
    "love",
    "home",
    "dream",
    "earbuds",
]

random_word = random.choice(words)

name = input("Please enter your name: ")

print(termcolor.colored(f"{name}, Welcome to Hangman game!", "yellow"))
print(termcolor.colored("Note: Game is not case sensitive!", "yellow"))
print("Start guessing...")
print(f"The word you have to guess has {len(random_word)} characters")

guesses = ""

chance_to_guess = 10

while chance_to_guess > 0:
    win_state = True
    for char in random_word:
        if char != random_word[-1]:
            if char in guesses:
                print(termcolor.colored(char, "green"), end="")
            else:
                print(termcolor.colored("_", "red"), end="")
                win_state = False
        else:
            if char in guesses:
                print(termcolor.colored(char, "green"))
            else:
                print(termcolor.colored("_", "red"))
                win_state = False
    if win_state:
        print(termcolor.colored(f"Congratulatiions {name}! You won", "green"))
        exit()
    guess = input("Guess a character: ")
    guesses += guess.lower()
    if guess not in random_word:
        if chance_to_guess >= len(guess):
            chance_to_guess -= len(guess)
        else:
            break
        print(termcolor.colored("Your guess is wrong!", "yellow"))
        print(termcolor.colored(f"You have {chance_to_guess} more guesses", "yellow"))

print(termcolor.colored("You lost!", "red"))
