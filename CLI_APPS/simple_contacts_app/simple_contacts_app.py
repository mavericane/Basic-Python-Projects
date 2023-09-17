# Author: Amin (Mavericane)
# Github Link: https://github.com/mavericane/
# Website Link: https://mavericane.ir
# Description: This is a simple contact app for creating, editing, deleting, and finding contacts.
# Version 1: Creating contact
# Importing required modules
# platform module for detecting os
import platform

# os module for checking files
import os

# csv module for creating and saving contacts
import csv

# termcolor module for colorizing outputs
import termcolor

# re(regex) module for checking if the numbers format and email format are correct or not
import re


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


# Checking if the contacts.csv file exists or doesn't exist to create a new contacts.csv file
def contacts_csv_exists():
    if os.path.exists(file_location + "contacts.csv"):
        return True
    else:
        return False


# Creating a new contacts.csv file for saving contacts
def contacts_csv_create():
    data = ["first_name", "last_name", "phone", "phone2", "email"]
    with open(file_location + "contacts.csv", "w", newline="") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(data)
        csv_file.close()


# Displaying main menu
def display_menu():
    print(termcolor.colored("Contacts App Menu:", "cyan"))
    print("1. Create a new contact")
    print("2. Quit")


# Function to create a new contact
def create_contact():
    first_name = input("Please enter the contact's first name(for example: Amin): ")
    last_name = input(
        "Please enter the contact's last name(for example: Khatoon Abadi): "
    )
    while True:
        phone = input(
            "Please enter the contact's first phone number(for example: 09123456789): "
        )
        pattern = r"^09\d{9}$"
        match = re.match(pattern, phone)
        if match:
            phone = "'" + phone + "'"
            break
        else:
            print(
                termcolor.colored(
                    "Your entered format for phone number is not correct",
                    "yellow",
                    "on_black",
                )
            )
    while True:
        print(
            termcolor.colored(
                "If you dont want to enter second phone number just skip by pressing Enter",
                "yellow",
                "on_black",
            )
        )
        phone2 = input(
            "Please enter the contact's second phone number(for example: 09123456789): "
        )
        restart_flag = False
        if phone2 == phone:
            print(
                termcolor.colored(
                    "You entered contact's first number again in second number",
                    "yellow",
                    "on_black",
                )
            )
            while True:
                user_input = input("Do you want to add another number? (Y yes, N no): ")
                if user_input.casefold() == "y" or user_input.casefold() == "yes":
                    restart_flag = True
                elif user_input.casefold() == "n" or user_input.casefold() == "no":
                    phone2 = ""
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
        if restart_flag:
            continue
        if phone2 == "":
            break
        match = re.match(pattern, phone2)
        if match:
            phone2 = "'" + phone2 + "'"
            break
        else:
            print(
                termcolor.colored(
                    "Your entered format for phone number is not correct",
                    "yellow",
                    "on_black",
                )
            )
    while True:
        print(
            termcolor.colored(
                "If you don't want to enter email address just skip by pressing Enter",
                "yellow",
                "on_black",
            )
        )
        email = input(
            "Please enter the contact's email address(for example: aminkhatoonabadi@gmail.com): "
        )
        if email == "":
            break
        pattern = f"([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\"([]!#-[^-~ \t]|(\\[\t -~]))+\")@([0-9A-Za-z]([0-9A-Za-z-]{0,61}[0-9A-Za-z])?(\.[0-9A-Za-z]([0-9A-Za-z-]{0,61}[0-9A-Za-z])?)*|\[((25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])(\.(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])){3}|IPv6:((((0|[1-9A-Fa-f][0-9A-Fa-f]{0,3}):){6}|::((0|[1-9A-Fa-f][0-9A-Fa-f]{0,3}):){5}|[0-9A-Fa-f]{0,4}::((0|[1-9A-Fa-f][0-9A-Fa-f]{0,3}):){4}|(((0|[1-9A-Fa-f][0-9A-Fa-f]{0,3}):)?(0|[1-9A-Fa-f][0-9A-Fa-f]{0,3}))?::((0|[1-9A-Fa-f][0-9A-Fa-f]{0,3}):){3}|(((0|[1-9A-Fa-f][0-9A-Fa-f]{0,3}):){0,2}(0|[1-9A-Fa-f][0-9A-Fa-f]{0,3}))?::((0|[1-9A-Fa-f][0-9A-Fa-f]{0,3}):){2}|(((0|[1-9A-Fa-f][0-9A-Fa-f]{0,3}):){0,3}(0|[1-9A-Fa-f][0-9A-Fa-f]{0,3}))?::(0|[1-9A-Fa-f][0-9A-Fa-f]{0,3}):|(((0|[1-9A-Fa-f][0-9A-Fa-f]{0,3}):){0,4}(0|[1-9A-Fa-f][0-9A-Fa-f]{0,3}))?::)((0|[1-9A-Fa-f][0-9A-Fa-f]{0,3}):(0|[1-9A-Fa-f][0-9A-Fa-f]{0,3})|(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])(\.(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])){3})|(((0|[1-9A-Fa-f][0-9A-Fa-f]{0,3}):){0,5}(0|[1-9A-Fa-f][0-9A-Fa-f]{0,3}))?::(0|[1-9A-Fa-f][0-9A-Fa-f]{0,3})|(((0|[1-9A-Fa-f][0-9A-Fa-f]{0,3}):){0,6}(0|[1-9A-Fa-f][0-9A-Fa-f]{0,3}))?::)|(?!IPv6:)[0-9A-Za-z-]*[0-9A-Za-z]:[!-Z^-~]+)])"
        match = re.match(pattern, email)
        if match:
            break
        else:
            print(
                termcolor.colored(
                    "Your entered format for email address is not correct",
                    "yellow",
                    "on_black",
                )
            )

    data = [first_name, last_name, phone, phone2, email]

    with open(file_location + "contacts.csv", "a", newline="") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(data)
        csv_file.close()

    print(
        termcolor.colored(
            f"Contact: {first_name} {last_name} addded successfully",
            "green",
            "on_black",
        )
    )


if __name__ == "__main__":
    file_location = os_detect()

    if not contacts_csv_exists():
        contacts_csv_create()

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            create_contact()
        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print(
                termcolor.colored(
                    "Invalid choice. Please enter a valid option.", "red", "on_black"
                )
            )
