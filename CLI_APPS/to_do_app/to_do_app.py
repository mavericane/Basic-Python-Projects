# Author: Amin (Mavericane)
# Github Link: https://github.com/mavericane/
# Website Link: https://mavericane.ir
# Description: This is a simple to_do app. In this app you can simply create, edit, view, delete, mark a task as completed.
# Version 4: Create, edit, view,mark task as completed
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
    print("1. Display all tasks")
    print("2. Add task")
    print("3. Edit task")
    print("4. View specific task")
    print("5. Mark task as completed")
    print("6. Delete specific task")
    print("7. Delete all tasks(reset data)")
    print("8. Quit")


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
        print(termcolor.colored("No tasks have been saved!", "yellow", "on_black"))
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
        print(
            f"Task ID: {termcolor.colored(task[0], output_color)} - Task name: {termcolor.colored(task[1], output_color)} - Status: {termcolor.colored(task[3], output_color)}"
        )
    print(termcolor.colored("`" * 3, "cyan", "on_black"))


# Function to add a new task
def add_task(edit=False, data=[]):
    # Get the last ID number stored in tasks.csv and old saved tasks
    with open(file_location + "tasks.csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        # Starting from "0" because first line is not a actual data and doesn't have number
        id = 0
        old_tasks = []
        for row in csv_reader:
            old_tasks.append(row)
            id += 1

    old_task_names = []
    for item in old_tasks:
        old_task_names.append(item[0])

    # Removing the name title
    old_task_names.pop(0)

    while True:
        task_name = input("Please enter the task name: ")
        if task_name == "" and not edit:
            print(termcolor.colored("Task name cannot be empty!", "yellow", "on_black"))
            continue
        break

    if task_name.casefold() in old_task_names and not edit:
        print(
            termcolor.colored(
                f"You saved a task with {task_name} name before!", "yellow", "on_black"
            )
        )
        while True:
            user_input = input("Do you want to edit your old task? (Y yes, N no): ")
            if user_input.casefold() == "y" or user_input.casefold() == "yes":
                for item in old_tasks:
                    if item[1] == task_name:
                        data = item
                edit_task(data)
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
    print(
        termcolor.colored(
            "Task Description is optional you can press Enter to skip it",
            "yellow",
            "on_black",
        )
    )
    task_description = input("Please enter your task description(optional): ")
    if task_description.isspace():
        task_description = ""

    # Data proccessing
    task = [id, task_name, task_description, "uncompleted"]

    # Data processing and returning data to be edited at its own function
    if edit:
        task = [data[0], task_name, task_description, data[3]]
        return task

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


# Function to edit a uncompleted task
def edit_task(data=[]):
    data = view_specific_task(data)

    if data == None:
        return None

    with open(file_location + "tasks.csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        csv_data = []
        for row in csv_reader:
            if (
                row[0].casefold() != data[0].casefold()
                and row[1].casefold() != data[1].casefold()
            ):
                csv_data.append(row)
            else:
                if row[3].casefold() == "uncompleted":
                    csv_data.append([])
                else:
                    print(
                        termcolor.colored(
                            "Selected task is completed and cannot be edited!",
                            "red",
                            "on_black",
                        )
                    )
                    return None
        csv_file.close()

    print(
        termcolor.colored(
            "You can press Enter to skip editing a specific data", "yellow", "on_black"
        )
    )

    new_data = add_task(edit=True, data=data)

    if new_data[1] == "":
        new_data[1] = data[1]

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

    with open(file_location + "tasks.csv", "w", newline="") as csv_file:
        csv_writer = csv.writer(csv_file)
        for item in csv_data:
            csv_writer.writerow(item)
        csv_file.close()

    print(
        termcolor.colored(
            f"Your selected task has been edited successfully!",
            "green",
            "on_black",
        )
    )

    view_specific_task(new_data)


# Function to view a specific task
def view_specific_task(data=[]):
    if len(data) == 0:
        while True:
            while True:
                print(
                    termcolor.colored(
                        "You can skip entering task name if you forget it!",
                        "yellow",
                        "on_black",
                    )
                )
                task_name = input("Please enter the task name: ")
                if task_name != "":
                    skip_task_id = True
                    empty_inputs = False
                else:
                    skip_task_id = False
                break
            if not skip_task_id:
                while True:
                    task_id = input("Please enter the task ID: ")
                    if task_id != "":
                        empty_inputs = False
                    else:
                        empty_inputs = True
                    break
            if empty_inputs:
                print(
                    termcolor.colored(
                        "You must either enter task name or task ID!", "red", "on_black"
                    )
                )
                while True:
                    user_input = input("Do you want to try again? (Y yes, N no): ")
                    if user_input.casefold() == "y" or user_input.casefold() == "yes":
                        edit_task(data)
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
            break

        # Searching task_name or task_ID in saved tasks
        with open(file_location + "tasks.csv", "r") as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                if skip_task_id:
                    if task_name.casefold() == row[1].casefold():
                        data = row
                        break
                else:
                    if task_id == row[0]:
                        data = row
                        break
            csv_file.close()
    else:
        # Searching task_name or task_ID in saved tasks
        with open(file_location + "tasks.csv", "r") as csv_file:
            csv_reader = csv.reader(csv_file)
            data_saved = False
            for row in csv_reader:
                if row[0] == data[0]:
                    data_saved = True
                    data = row
            if not data_saved:
                data = []
            csv_file.close()

    # Checking if task_name or task_ID exists in saved tasks
    if len(data) == 0:
        print(
            termcolor.colored(
                "There is no saved task with such name or ID!",
                "red",
                "on_black",
            )
        )
        return None

    # Task details output
    print(termcolor.colored("Task Detials: ", "green", "on_black"))
    print(termcolor.colored("`" * 3, "cyan", "on_black"))
    if data[3] == "completed":
        output_color = "green"
    elif data[3] == "uncompleted":
        output_color = "yellow"
    task_id = termcolor.colored(data[0], output_color)
    print(f"Task ID: {task_id}")
    task_name = termcolor.colored(data[1], output_color)
    print(f"Task Name: {task_name}")
    if data[2] != "":
        task_description = termcolor.colored(data[2], output_color)
        print(f"Task Description: {task_description}")
    status = termcolor.colored(data[3].capitalize(), output_color)
    print(f"Task status: {status}")
    print(termcolor.colored("`" * 3, "cyan", "on_black"))

    # Returning collected data to be used in other functions
    return data


# Function to mark a task as completed
def mark_task_completed():
    data = view_specific_task()

    if data == None:
        return None

    if data[3] == "completed":
        print(
            termcolor.colored("Selected task is already completed!", "red", "on_black")
        )
        return None

    # Changing task status to completed
    data[3] = "completed"
    # Loading all tasks to csv_data
    with open(file_location + "tasks.csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        csv_data = []
        for row in csv_reader:
            if (
                row[0].casefold() != data[0].casefold()
                and row[1].casefold() != data[1].casefold()
            ):
                csv_data.append(row)
            else:
                csv_data.append(data)
        csv_file.close()
    # Saving all tasks with marked task to tasks.csv
    with open(file_location + "tasks.csv", "w", newline="") as csv_file:
        csv_writer = csv.writer(csv_file)
        for item in csv_data:
            csv_writer.writerow(item)
        csv_file.close()
    # Output to complete the process
    print(termcolor.colored("Selected task marked as completed!", "green", "on_black"))


# Function to delete a specific task
def delete_specific_task():
    # TODO
    pass


# Function to delete all tasks(reset data)
def delete_all_tasks():
    # TODO
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
            add_task(edit=False)
        elif choice == "3":
            edit_task()
        elif choice == "4":
            view_specific_task()
        elif choice == "5":
            mark_task_completed()
        elif choice == "6":
            delete_specific_task()
        elif choice == "7":
            delete_all_tasks()
        elif choice == "8":
            print("Goodbye!")
            break
        else:
            print(
                termcolor.colored(
                    "Invalid choice. Please enter a valid option.", "red", "on_black"
                )
            )
