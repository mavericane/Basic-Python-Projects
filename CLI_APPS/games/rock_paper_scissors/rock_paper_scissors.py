# Author: Amin (Mavericane)
# GitHub Link: https://github.com/mavericane/
# Website Link: https://mavericane.ir
# Description: This program simulates the two-player rock-paper-scissors game that is played between two people. In this program, the other side is the computer.
# Importing required modules
# random module for selecting random choice
import random

# termcolor module for colorizing outputs
import termcolor


# Checking game result
def game(random_selection, user_selection):
    if random_selection == user_selection:
        return (None, "We both selected same selection")
    elif (
        (random_selection == selections[0] and user_selection == selections[1])
        or (random_selection == selections[1] and user_selection == selections[2])
        or (random_selection == selections[2] and user_selection == selections[0])
    ):
        return (True, "You won")
    else:
        return (False, "You lost!")


# Selections list
selections = ["Rock", "Paper", "Scissors"]

# Choosing random selection to play
random_selection = random.choice(selections)

# Printing available selections
print("Selections: ", end="")
for i in range(len(selections)):
    if i != len(selections) - 1:
        print(f"{i+1}.{selections[i]}", end=" ")
    else:
        print(f"{i+1}.{selections[i]}")

# Getting user selection
while True:
    user_selection = input("Please select one of selections (type number or name): ")
    if user_selection.casefold() == "1" or user_selection.casefold() == "rock":
        user_selection = selections[0]
    elif user_selection.casefold() == "2" or user_selection.casefold() == "paper":
        user_selection = selections[1]
    elif user_selection.casefold() == "3" or user_selection.casefold() == "scissors":
        user_selection = selections[2]
    else:
        print(termcolor.colored("Your entered option is not valid!", "red"))
        continue
    break

# Printing user and random selections
print(f"I have selected: {random_selection}")
print(f"You have selected: {user_selection}")

# Playing game
result = game(random_selection, user_selection)

# Checking result
if result[0] == None:
    output_color = "yellow"
elif result[0]:
    output_color = "green"
elif not result[0]:
    output_color = "red"


# Printing result
print(termcolor.colored(result[1], output_color))
