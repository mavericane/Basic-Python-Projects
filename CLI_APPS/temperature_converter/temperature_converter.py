# Author: Amin (Mavericane)
# GitHub Link: https://github.com/mavericane/
# Website Link: https://mavericane.ir
# Description: This program accurately converts temperature measurement units to each other
# Importing required modules
# termcolor module for colorizing outputs
import termcolor


def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius


def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit


def celsius_to_kelvin(celsius):
    kelvin = celsius + 273.15
    return kelvin


def kelvin_to_celsius(kelvin):
    celsius = kelvin - 273.15
    return celsius


def fahrenheit_to_kelvin(fahrenheit):
    celsius = fahrenheit_to_celsius(fahrenheit)
    kelvin = celsius_to_kelvin(celsius)
    return kelvin


def kelvin_to_fahrenheit(kelvin):
    celsius = kelvin_to_celsius(kelvin)
    fahrenheit = celsius_to_fahrenheit(celsius)
    return fahrenheit


def main():
    print("Temperature Converter")
    # recieving input temperature from user
    while True:
        print(termcolor.colored("Inputs: 1.Celsius, 2.Farenheit, 3.Kelvin", "yellow"))
        user_input = input("Please enter your input unit (Enter number or type name): ")
        if user_input.casefold() == "1" or user_input.casefold() == "celsius":
            outputs = "Outputs: 1.Farenheit, 2.Kelvin"
        elif user_input.casefold() == "2" or user_input.casefold() == "farenheit":
            outputs = "Outputs: 1.Celsius, 2.Kelvin"
        elif user_input.casefold() == "3" or user_input.casefold() == "kelvin":
            outputs = "Outputs: 1.Celsius, 2.Farenheit"
        else:
            print(termcolor.colored("Your entered option is not valid!", "red"))
            continue
        break
    # recieving and calculating output
    while True:
        print(termcolor.colored(outputs, "yellow"))
        user_output = input(
            "Please enter your output unit (Enter number or type name): "
        )
        if user_input.casefold() == "1" or user_input.casefold() == "celsius":
            if user_output.casefold() == "1" or user_output.casefold() == "farenheit":
                c_temp = float(input("Enter temperature in Celsius: "))
                f_temp = celsius_to_fahrenheit(c_temp)
                print(
                    termcolor.colored(f"Temperature in Fahrenheit: {f_temp}", "green")
                )
            elif user_output.casefold() == "2" or user_output.casefold() == "kelvin":
                c_temp = float(input("Enter temperature in Celsius: "))
                k_temp = celsius_to_kelvin(c_temp)
                print(termcolor.colored(f"Temperature in Kelvin: {k_temp}", "green"))
            else:
                print(termcolor.colored("Your entered option is not valid!", "red"))
                continue
            break
        if user_input.casefold() == "2" or user_input.casefold() == "farenheit":
            if user_output.casefold() == "1" or user_output.casefold() == "celsius":
                f_temp = float(input("Enter temperature in Fahrenheit: "))
                c_temp = fahrenheit_to_celsius(f_temp)
                print(termcolor.colored(f"Temperature in Celsius: {c_temp}", "green"))
            elif user_output.casefold() == "2" or user_output.casefold() == "kelvin":
                f_temp = float(input("Enter temperature in Fahrenheit: "))
                k_temp = fahrenheit_to_kelvin(f_temp)
                print(termcolor.colored(f"Temperature in Kelvin: {k_temp}", "green"))
            else:
                print(termcolor.colored("Your entered option is not valid!", "red"))
                continue
            break
        if user_input.casefold() == "3" or user_input.casefold() == "kelvin":
            if user_output.casefold() == "1" or user_output.casefold() == "celsius":
                k_temp = float(input("Enter temperature in Kelvin: "))
                c_temp = kelvin_to_celsius(k_temp)
                print(termcolor.colored(f"Temperature in Celsius: {c_temp}", "green"))
            elif user_output.casefold() == "2" or user_output.casefold() == "farenheit":
                k_temp = float(input("Enter temperature in Kelvin: "))
                f_temp = kelvin_to_fahrenheit(k_temp)
                print(
                    termcolor.colored(f"Temperature in Fahrenheit: {f_temp}", "green")
                )
            else:
                print(termcolor.colored("Your entered option is not valid!", "red"))
                continue
            break


if __name__ == "__main__":
    main()
