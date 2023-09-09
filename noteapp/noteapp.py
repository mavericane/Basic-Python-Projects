# Author: Amin (Mavericane)
# Github Link: https://github.com/mavericane/
# Website Link: https://mavericane.ir
# Description: This file is a simple note taking app. View, Creates, Edits, Delete text notes with txt file format(*.txt).
# Version 3: create a new note, edit a note, view a specific note.
# Importing required modules
# platform module for detecting os
import platform

# os module for checking files
import os

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
        file_location += "notes/"
        return file_location
    elif os_name == "Windows":
        file_location_system = __file__.split("\\")
        file_location = ""
        for i in range(len(file_location_system)):
            if file_location_system[i] == file_location_system[-1]:
                None
            else:
                file_location += file_location_system[i] + "\\"
        file_location += "notes\\"
        return file_location
    else:
        print("This program doesn't support your operating system")
        exit()


# Function to display the menu
def display_menu():
    print(termcolor.colored("Note-taking App Menu:", "cyan"))
    print("1. Create a new note")
    print("2. Edit a note")
    print("3. View a specific note")
    print("4. Quit")


# Function to create a new note
def create_note():
    file_location = os_detect()
    if not os.path.exists(file_location):
        os.makedirs(file_location)
    title = input("Enter note title: ")
    if os.path.exists(f"{file_location}" + f"{title}.txt"):
        print(
            termcolor.colored(
                f"There is a note named '{title}.txt'", "yellow", "on_black"
            )
        )
        user_input = input("Do you want to edit it? (Y yes, N no): ")
        if user_input.casefold() == "y" or user_input.casefold() == "yes":
            edit_note()
        elif user_input.casefold() == "n" or user_input.casefold() == "no":
            display_menu()
        else:
            print(
                termcolor.colored(
                    "Invalid choice. Please enter a valid option.", "red", "on_black"
                )
            )
    else:
        contents = []
        print(
            termcolor.colored(
                "This is a multi-line entry. To finish writing and save the note, press Ctrl+D",
                "yellow",
                "on_black",
            )
        )
        print("Enter note content: ")
        while True:
            try:
                content = input()
                contents.append(content)
            except EOFError:
                break
        with open(f"{file_location}" + f"{title}.txt", "w") as text_file:
            text_file.write("\n".join(contents))
            text_file.close()
        print(
            termcolor.colored(
                f"Note '{title}.txt' created successfully!", "green", "on_black"
            )
        )


# Function to edit a note
def edit_note():
    file_location = os_detect()
    filename = input("Enter note title to view: ")
    try:
        with open(f"{file_location}" + f"{filename}.txt", "r") as file:
            content = file.read()
            print(f"Content of '{filename}.txt':")
            print(termcolor.colored("`" * 3, "cyan", "on_black"))
            print(content)
            print(termcolor.colored("`" * 3, "cyan", "on_black"))

        print(
            f"Editing '{filename}.txt'. Enter your text. Press Ctrl+D to save and exit."
        )
        contents = []
        print(
            termcolor.colored(
                "This is a multi-line entry. To finish writing and save the note, press Ctrl+D",
                "yellow",
                "on_black",
            )
        )
        print("Enter note content: ")
        while True:
            try:
                content = input()
                contents.append(content)
            except EOFError:
                break
        file_location = os_detect()
        with open(f"{file_location}" + f"{filename}.txt", "w") as text_file:
            text_file.write("\n".join(contents))
            text_file.close()

        print(
            termcolor.colored(
                f"Changes saved to '{filename}.txt'.", "green", "on_black"
            )
        )
    except FileNotFoundError:
        print(termcolor.colored(f"File '{filename}' not found.", "yellow"))


# Function to view a specific note
def view_specific_note():
    file_location = os_detect()
    filename = input("Enter note title to view: ")
    try:
        with open(f"{file_location}" + f"{filename}.txt", "r") as file:
            content = file.read()
            print(
                termcolor.colored(f"Content of '{filename}.txt':", "green", "on_black")
            )
            print(termcolor.colored("`" * 3, "cyan", "on_black"))
            print(content)
            print(termcolor.colored("`" * 3, "cyan", "on_black"))
    except FileNotFoundError:
        print(termcolor.colored(f"File '{filename}' not found.", "yellow"))


if __name__ == "__main__":
    print(
        termcolor.colored(
            "Your notes are saved with the title for the text file name and with the note content for the contents of the text file",
            "yellow",
        )
    )
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            create_note()
        elif choice == "2":
            edit_note()
        elif choice == "3":
            view_specific_note()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print(
                termcolor.colored(
                    "Invalid choice. Please enter a valid option.", "red", "on_black"
                )
            )
