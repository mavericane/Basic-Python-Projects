#Author: Amin (Mavericane)
#GitHub Link: https://github.com/mavericane/
#Website Link: https://mavericane.ir
#Description: This program is used to check the version number of installed applications on the Windows operating system that are available at supported_apps.csv by scanning all available drives
#Importing required modules
#os module for finding an executable location on a drive
import os
#psutil module for listing all available drives
import psutil
#win32api module for getting application versions from file attribute
import win32api
#termcolor module for colorizing output
import termcolor
#csv module for retrieving supported apps list
import csv

#Function to list all available drives
def get_available_drives():
    drives = []
    partitions = psutil.disk_partitions()
    for partition in partitions:
        drives.append(partition.device)
    return drives

#Function to search for application location in a drive
def find_executable(app_name,drive):
    for root, dirs, files in os.walk(drive):
        for file in files:
            if file.casefold() == app_name.casefold():
                return os.path.join(root, file)
    return False

#Function to get version number of application from file attribute
def get_version_number(file_path):  
    File_information = win32api.GetFileVersionInfo(file_path, "\\")
    ms_file_version = File_information['FileVersionMS']
    ls_file_version = File_information['FileVersionLS']
    version = [str(win32api.HIWORD(ms_file_version)), str(win32api.LOWORD(ms_file_version)), str(win32api.HIWORD(ls_file_version)), str(win32api.LOWORD(ls_file_version))]
    version = ".".join(version)
    return version

#The main function to get and store all available drives and check selected applications
def checker(selected_apps):
    drives = get_available_drives()
    for app in selected_apps:
        for drive in drives:
            executable_path = find_executable(app[1], drive)
            if not executable_path:
                print(termcolor.colored(f"{app[0]} not found", "red"))
                break
            else:
                file_path = fr"{executable_path}"
                version = get_version_number(file_path)
                print(termcolor.colored(f"{app[0]}: {version}", "green"))

#Finding running file location
file_location = __file__.split("\\")
file_location_string = "\\"
for i in range(len(file_location)):
    if i == 0 or file_location[i] == file_location[-1]:
        None
    else:
        file_location_string+= file_location[i] + "\\"

#Retrieving the list of supported apps from supported_apps.csv file
apps = []
with open(f"{file_location_string}"+"supported_apps.csv", "r") as supported_apps:
    apps_list = csv.reader(supported_apps)
    for row in apps_list:
        apps.append(tuple(row))

#Welcome output
print("""Welcome to the Version Checker Drive program
This program analyzes all drives to find the version number of supported applications
You can check the supported applications list in the supported_apps.csv file that comes with the program
To select apps if you want to check their version hit enter or type "yes"(y) to check and type "no"(n) to don't check""")

#List to store user-selected apps by prompt
selected_apps = []

#Loop to show and select apps by user needs
for app in apps:
    while True:
        result = input(f"Do you want to check for \"{termcolor.colored(app[0], 'yellow')}\":")
        if result == "" or result.casefold() == "yes" or result.casefold() == "y":
            selected_apps.append(app)
            break
        elif result.casefold() == "no" or result.casefold() == "n":
            break
        else:
            print("Your entered option is not available please reconsider")

#Output for starting the checking function
print(termcolor.colored("Your selected softwares will be checked in few moments", "yellow"))

#Checking function call
checker(selected_apps)
