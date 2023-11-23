# Author: Amin (Mavericane)
# GitHub Link: https://github.com/mavericane/
# Website Link: https://mavericane.ir
# Description: This program accurately converts length measurement units to each other(up to 4 decimal digits)
# Importing required modules
# termcolor module for colorizing outputs
import termcolor

# Decimal from decimal module for normalizing numbers(in this project: not printing zeros in decimals on right side of numbers)
from decimal import Decimal


# function to convert units to each other all units converted to millimeters then converted to all other units
def conversion(function_input):
    unit = function_input[0]
    number = function_input[1]

    def millimeter_to_centimeter(millimeter):
        centimeter = millimeter / 10
        return centimeter

    def millimeter_to_meter(millimeter):
        meter = millimeter / 1000
        return meter

    def millimeter_to_kilometer(millimeter):
        kilometer = millimeter / 1000000
        return kilometer

    def millimeter_to_inch(millimeter):
        inch = millimeter / 25.4
        return inch

    def millimeter_to_foot(millimeter):
        foot = millimeter / 304.8
        return foot

    def millimeter_to_yard(millimeter):
        yard = millimeter / 914.4
        return yard

    def millimeter_to_mile(millimeter):
        mile = millimeter / 1609350
        return mile

    def centimeter_to_millimeter(centimeter):
        millimeter = centimeter * 10
        return millimeter

    def meter_to_millimeter(meter):
        millimeter = meter * 1000
        return millimeter

    def kilometer_to_millimeter(kilometer):
        millimeter = kilometer * 1000000
        return millimeter

    def inch_to_millimeter(inch):
        millimeter = inch * 25.4
        return millimeter

    def foot_to_millimeter(foot):
        millimeter = foot * 304.8
        return millimeter

    def yard_to_millimeter(yard):
        millimeter = yard * 914.4
        return millimeter

    def mile_to_millimeter(mile):
        millimeter = mile * 1609350
        return millimeter

    if unit == "millimeter":
        millimeter = number
        centimeter = millimeter_to_centimeter(millimeter)
        meter = millimeter_to_meter(millimeter)
        kilometer = millimeter_to_kilometer(millimeter)
        inch = millimeter_to_inch(millimeter)
        foot = millimeter_to_foot(millimeter)
        yard = millimeter_to_yard(millimeter)
        mile = millimeter_to_mile(millimeter)

        function_output = [
            format(millimeter, ".4f"),
            format(centimeter, ".4f"),
            format(meter, ".4f"),
            format(kilometer, ".4f"),
            format(inch, ".4f"),
            format(foot, ".4f"),
            format(yard, ".4f"),
            format(mile, ".4f"),
        ]
        return function_output
    elif unit == "centimeter":
        newnumber = centimeter_to_millimeter(number)
    elif unit == "meter":
        newnumber = meter_to_millimeter(number)
    elif unit == "kilometer":
        newnumber = kilometer_to_millimeter(number)
    elif unit == "inch":
        newnumber = inch_to_millimeter(number)
    elif unit == "foot":
        newnumber = foot_to_millimeter(number)
    elif unit == "yard":
        newnumber = yard_to_millimeter(number)
    elif unit == "mile":
        newnumber = mile_to_millimeter(number)
    function_output = conversion(["millimeter", newnumber])
    return function_output


def number_normlizer(numbers):
    for i in range(len(numbers)):
        numbers[i] = Decimal(numbers[i])
        numbers[i] = (
            numbers[i].quantize(Decimal(1))
            if numbers[i] == numbers[i].to_integral()
            else numbers[i].normalize()
        )
    return numbers


def main():
    print("Length Converter")
    print(
        termcolor.colored(
            "Note: converted numbers only showing up to 4 decimal digits!", "yellow"
        )
    )
    # recieving unit
    while True:
        print(termcolor.colored("Inputs(Metric):", "yellow"))
        print("1.Millimeter, 2.Centimeter, 3.Meter, 4.Kilometer")
        print(termcolor.colored("Inputs(Imperial):", "yellow"))
        print("5.Inch, 6.Foot, 7.Yard, 8.Mile")
        user_input = input("Please enter your input unit (Enter number or type name): ")
        if user_input.casefold() == "1" or user_input.casefold() == "millimeter":
            unit = "millimeter"
        elif user_input.casefold() == "2" or user_input.casefold() == "centimeter":
            unit = "centimeter"
        elif user_input.casefold() == "3" or user_input.casefold() == "meter":
            unit = "meter"
        elif user_input.casefold() == "4" or user_input.casefold() == "kilometer":
            unit = "kilometer"
        elif user_input.casefold() == "5" or user_input.casefold() == "inch":
            unit = "inch"
        elif user_input.casefold() == "6" or user_input.casefold() == "foot":
            unit = "foot"
        elif user_input.casefold() == "7" or user_input.casefold() == "yard":
            unit = "yard"
        elif user_input.casefold() == "8" or user_input.casefold() == "mile":
            unit = "mile"
        else:
            print(termcolor.colored("Your entered option is not valid!", "red"))
            continue
        break

    # recieving number
    while True:
        number = float(input("Please enter your number to convert(greater than 0): "))
        if number <= 0:
            print(termcolor.colored("Your entered number is not valid!", "red"))
        else:
            break

    # gathering inputs data into a list to send for conversion function to convert data
    conversion_input = [unit, number]

    # converting units and given number
    conversion_output = conversion(conversion_input)

    # normlizing numbers(in this project: not printing zeros in decimals on right side of numbers)
    number_normlizer_output = number_normlizer(conversion_output)
    # The input number is only 1 number so we hand it with a single item list and in output we put index 0 into the number variable to replace it
    number = number_normlizer([number])[0]

    # printing converted units
    unit = unit.capitalize()
    print(termcolor.colored("Conversion Completed!", "green"))
    print(f"{number} {unit} to Millimeter: {number_normlizer_output[0]}")
    print(f"{number} {unit} to Centimeter: {number_normlizer_output[1]}")
    print(f"{number} {unit} to Meter: {number_normlizer_output[2]}")
    print(f"{number} {unit} to Kilometer: {number_normlizer_output[3]}")
    print(f"{number} {unit} to Inch: {number_normlizer_output[4]}")
    print(f"{number} {unit} to Foot: {number_normlizer_output[5]}")
    print(f"{number} {unit} to Yard: {number_normlizer_output[6]}")
    print(f"{number} {unit} to Mile: {number_normlizer_output[7]}")


if __name__ == "__main__":
    main()
