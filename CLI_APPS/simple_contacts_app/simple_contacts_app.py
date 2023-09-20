# Author: Amin (Mavericane)
# Github Link: https://github.com/mavericane/
# Website Link: https://mavericane.ir
# Description: This is a simple contacts app for creating, editing , deleting, finding contacts.
# Version 3: Creating, viewing, editing contact
# Importing required modules
# platform module for detecting os
import platform

# os module for checking files
import os

# csv module for creating and saving contacts
import csv

# termcolor module for colorizing outputs
import termcolor

# re(regex) module for checking if numbers format and emails format are correct or not
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


# Checking if contacts.csv file exists or doesn't exist to create a new contacts.csv file
def contacts_csv_exists():
    if os.path.exists(file_location + "contacts.csv"):
        return True
    else:
        return False


# Creating new contacts.csv file for saving contacts
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
    print("2. Edit a contact")
    print("3. View a specific contact")
    print("4. View all saved contacts")
    print("5. Delete a specific contact")
    print("6. Delete all saved contacts")
    print("7. Export contacts(VCARD) *.vcf file extension")
    print("8. Quit")


# Function to create a new contact
def create_contact(edit):
    while True:
        first_name = input("Please enter the contact's first name(for example: Amin): ")
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
    # Checking contact is already saved or not
    if not edit:
        data = []
        with open(file_location + "contacts.csv", "r") as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                if (
                    row[0].casefold() == first_name.casefold()
                    and row[1].casefold() == last_name.casefold()
                ):
                    data = row
                    break
            csv_file.close()
        if len(data) != 0:
            print(
                termcolor.colored(
                    f"Contact: {data[0]} {data[1]} is already saved!", "red", "on_black"
                )
            )
            user_input = input("Do you want to edit this contact? (Y yes, N no): ")
            if user_input.casefold() == "y" or user_input.casefold() == "yes":
                edit_contact(data)
                return None
            elif user_input.casefold() == "n" or user_input.casefold() == "no":
                return None
            else:
                print(
                    termcolor.colored(
                        "Invalid choice. Please enter a valid option.",
                        "red",
                        "on_black",
                    )
                )
    while True:
        phone = input(
            "Please enter the contact's first phone number(for example: 09123456789): "
        )
        pattern = r"^09\d{9}$"
        match = re.match(pattern, phone)
        if match:
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
                "If you dont want to enter email address just skip by pressing Enter",
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

    if edit:
        return data

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


# Function to edit a contact
def edit_contact(data=[]):
    data = view_specific_contact(data)

    if data == None:
        return None

    with open(file_location + "contacts.csv", "r") as csv_file:
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
        csv_file.close()

    new_data = create_contact(edit=True)

    for i in range(len(csv_data)):
        if csv_data[i] == []:
            csv_data[i] = new_data

    with open(file_location + "contacts.csv", "w", newline="") as csv_file:
        csv_writer = csv.writer(csv_file)
        for item in csv_data:
            csv_writer.writerow(item)
        csv_file.close()

    print(
        termcolor.colored(
            f"Contact: Old contact details: {data[0]} {data[1]} edited to new contact details: {new_data[0]} {new_data[1]} successfully",
            "green",
            "on_black",
        )
    )

    view_specific_contact(new_data)


# Function to view a specific contact(full contact information)(search by id or maybe first_name, lastname not decided)
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
        with open(file_location + "contacts.csv", "r") as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                if (
                    row[0].casefold() == first_name.casefold()
                    and row[1].casefold() == last_name.casefold()
                ):
                    data = row
                    break
            csv_file.close()
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
    print(f"First phone number: {data[2]}")
    if data[3] != "":
        print(f"Second phone number: {data[3]}")
    if data[4] != "":
        print(f"Email address: {data[4]}")
    print(termcolor.colored("`" * 3, "cyan", "on_black"))
    return data


# Function to view all saved contacts(id, first_name, last_name)
def view_all_contacts():
    # TODO
    pass


# Function to delete a specific contact(with id or first_name, last_name)
def delete_specific_contact():
    # TODO
    pass


# Function to delete all saved contacts
def delete_all_contacts():
    # TODO
    pass


# Function to export contacts to be saved in other applications with compatibility
def export_contacts():
    # TODO
    pass


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
