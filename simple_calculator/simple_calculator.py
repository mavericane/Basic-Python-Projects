# Author: Amin (Mavericane)
# GitHub Link: https://github.com/mavericane/
# Website Link: https://mavericane.ir
# Description: This is a simple calculator program for arithmetic math operators and some more operators
# termcolor module for colorizing outputs
import termcolor


# Addition function
def addition(num1, num2):
    return num1 + num2


# Subtraction function
def subtraction(num1, num2):
    return num1 - num2


# Multiplication function
def multiplication(num1, num2):
    return num1 * num2


# Division function
def division(num1, num2):
    if num2 == 0:
        return "You can't divide number by Zero(0)"
    else:
        return num1 / num2


# Modulus function
def modulus(num1, num2):
    if num2 == 0:
        return "You can't divide number by Zero(0)"
    else:
        return num1 % num2


# Exponentiation function
def exponentiation(num1, num2):
    return num1**num2


# Floor division function
def floor_division(num1, num2):
    return num1 // num2


# Main calculate function to process all operators
def calculate(num1, num2, opt):
    if opt == operators[0]:
        return addition(num1, num2)
    elif opt == operators[1]:
        return subtraction(num1, num2)
    elif opt == operators[2]:
        return multiplication(num1, num2)
    elif opt == operators[3]:
        return division(num1, num2)
    elif opt == operators[4]:
        return modulus(num1, num2)
    elif opt == operators[5]:
        return exponentiation(num1, num2)
    elif opt == operators[6]:
        return floor_division(num1, num2)


# All available operators for calculation
operators = ["+", "-", "*", "/", "%", "**", "//"]


# Main function to run program
def main():
    while True:
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Modulus (%)")
        print("6. Exponentiation (**)")
        print("7. Floor division (//)")
        print("8. Exit Program")
        while True:
            opt = input("Please select an option (enter option number): ")
            if (
                opt == "1"
                or opt == "2"
                or opt == "3"
                or opt == "4"
                or opt == "5"
                or opt == "6"
                or opt == "7"
            ):
                opt = operators[int(opt) - 1]
                break
            elif opt == "8" or opt.casefold() == "exit":
                exit()
            else:
                print(termcolor.colored("Entered option is not valid!", "red"))
        while True:
            try:
                num1 = float(input("Enter first number: "))
                break
            except ValueError:
                print(termcolor.colored("Please enter real numbers only!", "red"))
                continue
        while True:
            try:
                num2 = float(input("Enter second number: "))
                break
            except ValueError:
                print(termcolor.colored("Please enter real numbers only!", "red"))
                continue
        result = calculate(num1, num2, opt)
        print(termcolor.colored(f"{num1} {opt} {num2} = {result}", "green"))
        while True:
            again = input("Do you want to continue using calculator? (Y yes, N no): ")
            if again.casefold() == "no" or again.casefold() == "n":
                exit()
            elif again.casefold() == "yes" or again.casefold() == "y":
                break
            else:
                print(termcolor.colored("Entered option is not valid!", "red"))


# Main function call
main()
