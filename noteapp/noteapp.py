# Author: Amin (Mavericane)
# Github Link: https://github.com/mavericane/
# Website Link: https://mavericane.ir
# Description: This file is a simple note taking app. View, Creates, Edits, Delete text notes with txt file format(*.txt).
# Version 2: view a specific note, create a new note
# Importing required modules
# platform module for detecting os
import platform

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


# Function to display the menu
def display_menu():
    print(termcolor.colored("Note-taking App Menu:", "cyan"))
    print("1. Create a new note")
    print("2. View a specific note")
    print("3. Quit")


# Function to create a new note
def create_note():
    title = input("Enter note title: ")
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
    with open(f"{file_location}" + f"{title}.txt", "a") as text_file:
        text_file.write("\n".join(contents))
        text_file.close()
    print(f"Note '{title}.txt' created successfully!")


# Function to view a specific note
def view_specific_note():
    file_location = os_detect()
    filename = input("Enter note title to view: ")
    try:
        with open(f"{file_location}" + f"{filename}.txt", "r") as file:
            content = file.read()
            print(f"Content of '{filename}.txt':")
            print(termcolor.colored("`" * 3, "green"))
            print(content)
            print(termcolor.colored("`" * 3, "green"))
    except FileNotFoundError:
        print(f"File '{filename}' not found.")


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
            view_specific_note()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print(
                termcolor.colored(
                    "Invalid choice. Please enter a valid option.", "red", "on_black"
                )
            )
