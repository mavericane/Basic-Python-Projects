# Author: Amin (Mavericane)
# GitHub Link: https://github.com/mavericane/
# Website Link: https://mavericane.ir
# Description: This program is a slot machine simulator
# Importing required modules
# random module for randomizing slots
import random

# termcolor module for colorizing outputs
import termcolor

# Maximum line for betting and rows in slot machine
MAX_LINES = 10

# Maximum bet on each play ($)
MAX_BET = 100

# Minimum bet on each play ($)
MIN_BET = 1

# Number of columns on slot machine
COLS = 3

# Chance of symbols getting in slot machine
symbol_count = {"$": 2, "&": 4, "#": 6, "*": 8}

# Value of symbols for winning on slot machine
symbol_value = {"$": 10, "&": 4, "#": 3, "*": 2}


# Depositing money
def deposit():
    while True:
        amount = input("How much money would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print(termcolor.colored("Amount must be greater than 0.", "yellow"))
        else:
            print(termcolor.colored("Please enter a number", "red"))
    return amount


# Get the number of betting lines from the user
def get_number_of_lines():
    while True:
        lines = input(
            "Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? "
        )
        if lines.isdigit():
            lines = int(lines)
            if MAX_LINES >= lines >= 1:
                break
            else:
                print("Enter a valid number of lines")
        else:
            print("Please enter a number.")
    return lines


# Get the bet value of each line on the slot machine from the user
def get_bet():
    while True:
        amount = input("What whould you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MAX_BET >= amount >= MIN_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_LINES}")
        else:
            print("Please enter a number.")
    return amount


# Spinning slot machine
def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns


# Printing slot machine
def print_slot_machine(columns):
    output_color = "cyan"
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                output = termcolor.colored(column[row], output_color)
                print(output, end=" | ")
            else:
                output = termcolor.colored(column[row], output_color)
                print(output, end="")
        print()


# Check if there is a win
def check_winnings(columns, lines, bet, values):
    winings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winings += values[symbol] * bet
            winning_lines.append(line + 1)
    return winings, winning_lines


# Spin the slot machine with checking the balance of user
def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(
                f"You do not have enough to bet that amount, your current balance is: ${balance}"
            )
        else:
            break
    print(
        f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}"
    )
    slots = get_slot_machine_spin(MAX_LINES, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    if winnings == 0:
        print(termcolor.colored("You lost this round", "yellow"))
    else:
        output_color = "green"
        print(termcolor.colored(f"You won ${winnings}.", output_color))
    if len(winning_lines) == 1:
        print(
            termcolor.colored(
                f"You won on line: " + str(winning_lines[0]), output_color
            )
        )
    elif len(winning_lines) > 1:
        print(
            termcolor.colored(
                f"You won on lines: " + ",".join(map(str, winning_lines)), output_color
            )
        )
    return winnings - total_bet


# Main function to run each time for gambling and checking money balance
def main():
    starting_balance = deposit()
    # Remembering starting balance to use for balance output color in game
    balance = starting_balance
    while True:
        # Checking balance state
        balance_output_color = "green"
        if starting_balance // 2 > balance > 0:
            balance_output_color = "yellow"
        elif balance == 0:
            balance_output_color = "red"
            while True:
                again = input(
                    "Do you want to deposit money and play again? (Y yes, N no): "
                )
                if again.casefold() == "y" or again.casefold() == "yes":
                    main()
                elif again.casefold() == "n" or again.casefold() == "no":
                    exit()
                else:
                    print(termcolor.colored("Your entered option is not valid!", "red"))
        print(termcolor.colored(f"Current balance is ${balance}", balance_output_color))
        # Starting to play
        while True:
            answer = input("Press enter or type play to spin machine (Q quit): ")
            if answer.casefold() == "q" or answer.casefold() == "quit":
                exit()
            elif answer.casefold() == "" or answer.casefold() == "play":
                break
            else:
                print(termcolor.colored("Your entered option is not valid!", "red"))
        balance += spin(balance)


# Main function call
main()
