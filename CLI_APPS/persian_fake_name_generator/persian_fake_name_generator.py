# Author: Amin (Mavericane)
# Github Link: https://github.com/mavericane/
# Website Link: https://mavericane.ir
# Description: This is a simple fake Persian name-generating app that uses two CSV files to load first and last names to generate a random name
# Importing required modules
# platform module for detecting os
import platform

# os module for checking files
import os

# csv module for loading names
import csv

# random module for selecting random choices for first and last names from lists
import random

# termcolor module for colorizing outputs
import termcolor


# Detecting os and running file location
def os_detect():
    os_name = platform.system()
    if os_name == "Linux":
        file_location_system = __file__.split("/")
        file_location = "/"
        for i in range(len(file_location_system)):
            if i == 0 or file_location_system[i] == file_location_system[-1]:
                None
            else:
                file_location += file_location_system[i] + "/"
        return file_location
    elif os_name == "Windows":
        file_location_system = __file__.split("\\")
        file_location = ""
        for i in range(len(file_location_system)):
            if file_location_system[i] == file_location_system[-1]:
                None
            else:
                file_location += file_location_system[i] + "\\"
        return file_location
    else:
        print("This program doesn't support your operating system")
        exit()


# Checking if the first_names.csv and last_names.csv file exists or not
def names_csv_exists():
    if os.path.exists(file_location + "first_names.csv") and os.path.exists(
        file_location + "last_names.csv"
    ):
        return True
    else:
        return False


# Choosing a random first name from the first_names.csv file
def choose_first_name(gender):
    # Loading first_names from CSV file
    with open(file_location + "first_names.csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        first_names = []
        for row in csv_reader:
            if row[0] == gender:
                first_names.append(row[1])
        csv_file.close()

    # Choosing random first_name from first_names list
    first_name = random.choice(first_names)
    # Function output
    return first_name


# Choosing a random last name from the last_names.csv file
def choose_last_name():
    # Loading last_names from CSV file
    with open(file_location + "last_names.csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        last_names = []
        for row in csv_reader:
            last_names.append(row[0])
        csv_file.close()

    # Choosing random first_name from first_names list
    last_name = random.choice(last_names)
    # Function output
    return last_name


if __name__ == "__main__":
    file_location = os_detect()
    if names_csv_exists():
        while True:
            gender = input("Choose your gender (1.Male 2.Female): ")
            if gender.casefold() == "male" or gender == "1":
                gender = "m"
            elif gender.casefold() == "female" or gender == "2":
                gender = "f"
            else:
                print(
                    termcolor.colored(
                        "Invalid choice. Please enter a valid option.",
                        "red",
                        "on_black",
                    )
                )
                continue
            break
        first_name = choose_first_name(gender)
        last_name = choose_last_name()
        # Combining first and last names to print together in the complete name
        name = f"{first_name} {last_name}"
        output = f"Your random generated name is: " + termcolor.colored(
            name, "green", "on_black"
        )
        print(output)
    else:
        print(
            termcolor.colored(
                "Error: first_names.csv or last_names.csv file is missing!",
                "red",
                "on_black",
            )
        )
