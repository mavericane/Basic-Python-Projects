# Author: Amin (Mavericane)
# GitHub Link: https://github.com/mavericane/
# Website Link: https://mavericane.ir
# Description: This program calculates the BMI factor, which is a factor to identify the body mass status, and determines your status.
# Importing required modules
# termcolor module for colorizing outputs
import termcolor


# Calculating BMI factor
def calculate_bmi(weight, height):
    bmi = weight / ((height / 100) ** 2)
    return bmi


def main():
    print("BMI Calculator")
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in centimeters: "))

    bmi = calculate_bmi(weight, height)

    print("Your BMI is:", bmi)

    # BMI, basic categories
    if bmi < 16:
        print(termcolor.colored("You are Underweight (Severe thinness).", "red"))
    elif 16 <= bmi < 17:
        print(termcolor.colored("You are Underweight (Moderate thinness).", "yellow"))
    elif 17 <= bmi < 18.5:
        print(termcolor.colored("You are Underweight (Mild thinness).", "cyan"))
    elif 18.5 <= bmi < 25:
        print(termcolor.colored("You are in Normal range.", "green"))
    elif 25 <= bmi < 30:
        print(termcolor.colored("You are Overweight (Pre-obese).", "cyan"))
    elif 30 <= bmi < 35:
        print(termcolor.colored("You are Obese (Class I).", "yellow"))
    elif 35 <= bmi < 40:
        print(termcolor.colored("You are Obese (Class II).", "red"))
    elif 40 <= bmi:
        print(termcolor.colored("You are Obese (Class III).", "red", "on_black"))
    else:
        print("Your calculated bmi number does not exist in the mass category!")


if __name__ == "__main__":
    main()
