# Author: Amin (Mavericane)
# GitHub Link: https://github.com/mavericane/
# Website Link: https://mavericane.ir
# Description: This is a simple rolling dice simulator
# termcolor module for colorizing outputs
import termcolor

# random module for randomizing numbers in dice (rolling dice)
import random

print("Dice Rolling Simulator")

while True:
    try:
        num_dice = int(input("Enter the number of dice: "))
        break
    except ValueError:
        print(termcolor.colored("Please enter real numbers only!", "red"))
        continue

for i in range(num_dice):
    print(
        termcolor.colored(
            f"Die {i+1}: {random.choice(range(1,6+1))}", "green", "on_black"
        )
    )
