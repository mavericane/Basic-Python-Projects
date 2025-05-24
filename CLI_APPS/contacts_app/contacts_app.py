# Author: Amin (Mavericane)
# Github Link: https://github.com/mavericane/
# Website Link: https://mavericane.ir
# Description: This is a simple contacts app for creating, editing, viewing, deleting, and exporting to other apps for contact management.
# Version 5.2: Create a new contact, edit a contact, view a specific contact, view all saved contacts, delete a specific contact, and delete all saved contacts.
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

# Path function from pathlib module for detecting running file location if script is running as a .py file
from pathlib import Path

# sys module for detecting running file location if script is compiled
import sys


# Detect file location (supports both .py and compiled executable)
if getattr(sys, "frozen", False):
    file_location = Path(sys.executable).parent
else:
    file_location = Path(__file__).resolve().parent


# Checking if the contacts.csv file exists or doesn't exist to create a new contacts.csv file
def contacts_csv_exists():
    if os.path.exists(csv_file_path):
        return True
    else:
        return False


# Creating a new contacts.csv file for saving contacts
def contacts_csv_create():
    data = ["first_name", "last_name", "phone", "phone2", "email"]
    with open(csv_file_path, "w", newline="") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(data)


# Displaying main menu
def display_menu():
    print(termcolor.colored("Contacts App Menu:", "cyan"))
    print("1. Create a new contact")
    print("2. Edit a contact")
    print("3. View a specific contact")
    print("4. View all saved contacts")
    print("5. Delete a specific contact")
    print("6. Delete all saved contacts")
    print("7. Export contacts(VCARD) *.vcf file extension")
    print("8. Quit")


# Function to create a new contact
def create_contact(edit):
    print(
        termcolor.colored(
            "Contact information is stored in a case-sensitive manner",
            "yellow",
            "on_black",
        )
    )
    while True:
        if edit:
            first_name = input("Please enter the new first name: ")
        else:
            first_name = input(
                "Please enter the contact's first name(for example: Amin): "
            )
        if first_name == "" and not edit:
            print(
                termcolor.colored(
                    "Contact's first name cannot be empty!", "yellow", "on_black"
                )
            )
            continue
        break
    while True:
        if edit:
            last_name = input("Please enter the new last name: ")
        else:
            last_name = input(
                "Please enter the contact's last name(for example: Khatoon Abadi): "
            )
        if last_name == "" and not edit:
            print(
                termcolor.colored(
                    "Contact's last name cannot be empty!", "yellow", "on_black"
                )
            )
            continue
        break
    # Checking whether contact is already saved or not
    if not edit:
        data = []
        with open(csv_file_path, "r") as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                if (
                    row[0].casefold() == first_name.casefold()
                    and row[1].casefold() == last_name.casefold()
                ):
                    data = row
                    break
        if len(data) != 0:
            print(
                termcolor.colored(
                    f"Contact: {data[0]} {data[1]} is already saved!", "red", "on_black"
                )
            )
            while True:
                user_input = input("Do you want to edit this contact? (Y yes, N no): ")
                if user_input.casefold() == "y" or user_input.casefold() == "yes":
                    edit_contact(data)
                elif user_input.casefold() == "n" or user_input.casefold() == "no":
                    pass
                else:
                    print(
                        termcolor.colored(
                            "Invalid choice. Please enter a valid option.",
                            "red",
                            "on_black",
                        )
                    )
                    continue
                return None
    while True:
        if edit:
            phone = input("Please enter the new phone number: ")
        else:
            phone = input(
                "Please enter the contact's phone number(for example: 09123456789): "
            )
        if phone == "" and not edit:
            print(
                termcolor.colored(
                    "Contact's phone cannot be empty!", "yellow", "on_black"
                )
            )
            continue
        if phone == "" and edit:
            break
        pattern = r"^09\d{9}$"
        match = re.match(pattern, phone)
        if match:
            break
        else:
            print(
                termcolor.colored(
                    "Your entered format for the phone number is not correct",
                    "yellow",
                    "on_black",
                )
            )
    while True:
        print(
            termcolor.colored(
                "If you don't want to enter a second phone number just skip by pressing Enter",
                "yellow",
                "on_black",
            )
        )
        if edit:
            phone2 = input("Please enter the new second phone number: ")
        else:
            phone2 = input(
                "Please enter the contact's second phone number(for example: 09123456789): "
            )
        restart_flag = False
        if phone2 == phone and not edit:
            print(
                termcolor.colored(
                    "You entered the contact's number again in the second number",
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
        pattern = r"^09\d{9}$"
        match = re.match(pattern, phone2)
        if match:
            break
        else:
            print(
                termcolor.colored(
                    "Your entered format for the phone number is not correct",
                    "yellow",
                    "on_black",
                )
            )
    while True:
        print(
            termcolor.colored(
                "If you do not want to enter email address just skip by pressing Enter",
                "yellow",
                "on_black",
            )
        )
        if edit:
            email = input("Please enter the new email address: ")
        else:
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

    if edit:
        return data

    with open(csv_file_path, "a", newline="") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(data)

    print(
        termcolor.colored(
            f"Contact: {first_name} {last_name} added successfully",
            "green",
            "on_black",
        )
    )


# Function to edit a contact
def edit_contact(data=[]):
    print(
        termcolor.colored(
            "Contact information is stored in a case-sensitive manner",
            "yellow",
            "on_black",
        )
    )
    data = view_specific_contact(data)

    if data == None:
        return None

    with open(csv_file_path, "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        csv_data = []
        for row in csv_reader:
            if (
                row[0].casefold() != data[0].casefold()
                and row[1].casefold() != data[1].casefold()
            ):
                csv_data.append(row)
            else:
                csv_data.append([])

    print(
        termcolor.colored(
            "You can press Enter to skip editing a specific data", "yellow", "on_black"
        )
    )

    new_data = create_contact(edit=True)

    for i in range(2 + 1):
        if new_data[i] == "":
            new_data[i] = data[i]

    if new_data == data:
        print(
            termcolor.colored(
                "You have not edited any information. Editing has been cancelled",
                "red",
                "on_black",
            )
        )
        return None

    for i in range(len(csv_data)):
        if csv_data[i] == []:
            csv_data[i] = new_data

    with open(csv_file_path, "w", newline="") as csv_file:
        csv_writer = csv.writer(csv_file)
        for item in csv_data:
            csv_writer.writerow(item)

    print(
        termcolor.colored(
            f"Contact: Old contact details: {data[0]} {data[1]} edited to new contact details: {new_data[0]} {new_data[1]} successfully",
            "green",
            "on_black",
        )
    )

    view_specific_contact(new_data)


# Function to view a specific contact
def view_specific_contact(data=[]):
    if len(data) == 0:
        while True:
            first_name = input(
                "Please enter the contact's first name(for example: Amin): "
            )
            if first_name == "":
                print(
                    termcolor.colored(
                        "Contact's first name cannot be empty!", "yellow", "on_black"
                    )
                )
                continue
            break
        while True:
            last_name = input(
                "Please enter the contact's last name(for example: Khatoon Abadi): "
            )
            if last_name == "":
                print(
                    termcolor.colored(
                        "Contact's last name cannot be empty!", "yellow", "on_black"
                    )
                )
                continue
            break
        data = []
        with open(csv_file_path, "r") as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                if (
                    row[0].casefold() == first_name.casefold()
                    and row[1].casefold() == last_name.casefold()
                ):
                    data = row
                    break
        if len(data) == 0:
            print(
                termcolor.colored(
                    "There is no contact with such first and last name!",
                    "red",
                    "on_black",
                )
            )
            return None

    # Contact information output
    print(termcolor.colored("Contact Information: ", "green", "on_black"))
    print(termcolor.colored("`" * 3, "cyan", "on_black"))
    print(f"First name: {data[0]}")
    print(f"Last name: {data[1]}")
    print(f"Phone number: {data[2]}")
    if data[3] != "":
        print(f"Second phone number: {data[3]}")
    if data[4] != "":
        print(f"Email address: {data[4]}")
    print(termcolor.colored("`" * 3, "cyan", "on_black"))
    return data


# Function to view all saved contacts
def view_all_contacts():
    # Loading all contacts.csv data to a list
    data = []
    with open(csv_file_path, "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            data.append(row)

    # Removing the title's
    data.pop(0)

    # Output to show all saved contacts
    if len(data) == 0:
        print(
            termcolor.colored("No contacts have been saved yet!", "yellow", "on_black")
        )
        return None
    contacts_num = len(data)
    print(
        termcolor.colored(
            f"There is {contacts_num} contacts have been saved with below details:",
            "green",
            "on_black",
        )
    )
    print(termcolor.colored("`" * 3, "cyan", "on_black"))
    for item in data:
        output = "Contact: "
        first_name = termcolor.colored("First name:", "green") + " " + item[0]
        last_name = termcolor.colored("Last name:", "green") + " " + item[1]
        phone = termcolor.colored("Phone number:", "blue") + " " + item[2]
        output += f"{first_name}{termcolor.colored(',', 'green')} {last_name}{termcolor.colored(',', 'green')} {phone}"
        if item[3] != "":
            phone2 = (
                termcolor.colored("Second phone number:", "light_blue") + " " + item[3]
            )
            output += f"{termcolor.colored(',', 'green')} {phone2}"
        if item[4] != "":
            email = termcolor.colored("Email:", "light_green") + " " + item[4]
            output += f"{termcolor.colored(',', 'green')} {email}"
        print(output)
    print(termcolor.colored("`" * 3, "cyan", "on_black"))


# Function to delete a specific contact(with id or first_name, last_name)
def delete_specific_contact():
    data = view_specific_contact()

    if data == None:
        return None

    with open(csv_file_path, "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        csv_data = []
        for row in csv_reader:
            if (
                row[0].casefold() != data[0].casefold()
                and row[1].casefold() != data[1].casefold()
            ):
                csv_data.append(row)

    with open(csv_file_path, "w", newline="") as csv_file:
        csv_writer = csv.writer(csv_file)
        for item in csv_data:
            csv_writer.writerow(item)

    print(
        termcolor.colored(
            f"Contact: {data[0]} {data[1]} was successfully deleted",
            "green",
            "on_black",
        )
    )


# Function to delete all saved contacts
def delete_all_contacts():
    user_input = input("Do you want to delete all your saved contacts? (Y yes, N no): ")
    if user_input.casefold() == "y" or user_input.casefold() == "yes":
        # Loading all contacts.csv data to a list
        data = []
        with open(csv_file_path, "r") as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                data.append(row)

        # Removing the title's
        data.pop(0)

        # Output to show all saved contacts
        if len(data) == 0:
            print(
                termcolor.colored(
                    "No contacts have been saved yet!", "yellow", "on_black"
                )
            )
            return None

        # Removing all contacts(recreating contacts.csv)
        contacts_csv_create()
        print(
            termcolor.colored(
                f"{len(data)} saved contacts have been deleted", "green", "on_black"
            )
        )

    elif user_input.casefold() == "n" or user_input.casefold() == "no":
        return None
    else:
        print(
            termcolor.colored(
                "Invalid choice. Please enter a valid option.", "red", "on_black"
            )
        )


# Function to export contacts to be saved in other applications with compatibility
def export_contacts():
    # TODO
    pass


if __name__ == "__main__":
    csv_file_path = str(file_location) + "contacts.csv"

    if not contacts_csv_exists():
        contacts_csv_create()

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        os.system("cls" if os.name == "Windows" else "clear")
        if choice == "1":
            create_contact(edit=False)
        elif choice == "2":
            edit_contact()
        elif choice == "3":
            view_specific_contact()
        elif choice == "4":
            view_all_contacts()
        elif choice == "5":
            delete_specific_contact()
        elif choice == "6":
            delete_all_contacts()
        elif choice == "7":
            export_contacts()
        elif choice == "8":
            print("Goodbye!")
            break
        else:
            print(
                termcolor.colored(
                    "Invalid choice. Please enter a valid option.", "red", "on_black"
                )
            )
