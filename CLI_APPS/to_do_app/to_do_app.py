# Author: Amin (Mavericane)
# Github Link: https://github.com/mavericane/
# Website Link: https://mavericane.ir
# Description: This is a simple to_do app. In this app you can simply create, edit, view, delete, mark a task az completed.
# Version 1: Create a task
# Importing required modules
# platform module for detecting os
import platform

# os module for checking files
import os

# csv module for task management
import csv

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

# Checking if the tasks.csv file exists or doesn't exist to create a new tasks.csv file
def tasks_csv_exists():
    if os.path.exists(file_location + "tasks.csv"):
        return True
    else:
        return False
    
# Creating a new tasks.csv file for tasks management
def tasks_csv_create():
    data = ["id", "name", "status"]
    with open(file_location + "tasks.csv", "w", newline="") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(data)
        csv_file.close()

# Displaying main menu
def display_menu():
    print(termcolor.colored("Options:", "cyan"))
    print("1. Display tasks")
    print("2. Add task")
    print("3. Quit")

# Function to display the current tasks
def display_tasks():
    # Loading all tasks from task.csv to a list structure
    tasks = []

    with open(file_location + "tasks.csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            tasks.append(row)
    
    # Removing the title's
    tasks.pop(0)

    # Sorting tasks
    total_tasks_num = len(tasks)

    completed_tasks = []
    uncompleted_tasks = []
    for task in tasks:
        if task[3].casefold() == "completed":
             completed_tasks.append(task)
        elif task[3].casefold() == "uncompleted":
             uncompleted_tasks.append(task)
    tasks = completed_tasks + uncompleted_tasks
    completed_tasks_num = len(completed_tasks)
    uncompleted_tasks_num = len(uncompleted_tasks)

    
    # Output to show all saved tasks
    if len(tasks) == 0:
        print(
            termcolor.colored("No tasks have been saved!", "yellow", "on_black")
        )
        return None
    
    print(
        termcolor.colored(
            f"There is total {total_tasks_num} tasks saved:",
            "green",
            "on_black",
        )
    )
    print(termcolor.colored(f"Completed tasks: {completed_tasks_num}", "green"))
    print(termcolor.colored(f"Uncompleted tasks: {uncompleted_tasks_num}", "yellow"))
    print(termcolor.colored("`" * 3, "cyan", "on_black"))
    for task in tasks:
        if task[3].casefold() == "completed":
            output_color = "green"
        elif task[3].casefold() == "uncompleted":
            output_color = "yellow"
        print(f"Task ID: {termcolor.colored(task[0], output_color)} - Task name: {termcolor.colored(task[1], output_color)} - Status: {termcolor.colored(task[3], output_color)}")
    print(termcolor.colored("`" * 3, "cyan", "on_black"))

# Function to add a new task
def add_task():
    # Get the last ID number stored in tasks.csv
    with open(file_location + "tasks.csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        # Starting from "0" because first line is not a actual data and doesn't have number
        id = 0
        old_task_names = []
        for row in csv_reader:
            old_task_names.append(row[1])
            id += 1

    # Removing the name title
    old_task_names.pop(0)
    
    task_name = input("Please enter your task name: ")

    if task_name.casefold() in old_task_names:
        print(termcolor.colored(f"You saved a task with {task_name} name before!", "yellow", "on_black"))
        while True:
            user_input = input("Do you want to edit your old task? (Y yes, N no): ")
            if user_input.casefold() == "y" or user_input.casefold() == "yes":
                # edit_task(task_name)
                pass
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
    print(termcolor.colored("Task Description is optional you can press Enter to skip it", "yellow", "on_black"))
    task_description = input("Please enter your task description(optional): ")
    if task_description.isspace():
         task_description = ""
    
    # Data proccessing
    task = [id, task_name, task_description, "uncompleted"]

    # Adding task to tasks.csv
    with open(file_location + "tasks.csv", "a", newline="") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(task)
        csv_file.close()

    print(
        termcolor.colored(
            f"Task ID: {id} - Task Name: {task_name} added successfully",
            "green",
            "on_black",
        )
    )


    
# Function to mark a task as completed
def complete_task():
    #TODO
    pass

# Function to delete a task
def delete_task():
    #TODO
    pass

if __name__ == "__main__":
    file_location = os_detect()

    if not tasks_csv_exists():
        tasks_csv_create()
    
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        os.system("cls" if os.name == "Windows" else "clear")
        if choice == "1":
            display_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print(
                termcolor.colored(
                    "Invalid choice. Please enter a valid option.", "red", "on_black"
                )
            )
