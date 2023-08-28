# Author: Amin (Mavericane)
# Github Link: https://github.com/mavericane/
# Website Link: https://mavericane.ir
# Description: This program is a simple alarm program that will play a sound as an alarm at the set time
# System requirements:
## Operating System: Windows, Linux
# Importing required modules
# platform module for detecting os
import platform
# time module for setting an alarm
import time
# termcolor module for colorizing outputs
import termcolor
# playsound function from playsound module to simply playing an alarm sound
from playsound import playsound

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
    
# Playing alarm sound file
def play_alarm_sound(sound_file):
    file_location = os_detect()
    playsound(file_location + sound_file)

# Setting alarm for user requested time
def set_alarm(alarm_time):
    while True:
        current_time = time.strftime("%H:%M:%S")
        if current_time == alarm_time:
            print("ALARM! Wake up!")
            # You can change your alarm sound by replacing alarm.mp3 with another sound file in code below
            play_alarm_sound("alarm.mp3")
            break
        time.sleep(1)

# Main function to run the program
def main():
    print("Simple Alarm Clock")

    while True:
        print(termcolor.colored("Note: Please enter full Hour:Minute:Second format like 03:05:01", "yellow", "on_black"))
        alarm_time = input("Set the alarm time (HH:MM:SS format): ")

        try:
            time.strptime(alarm_time, "%H:%M:%S")
            break
        except ValueError:
            print(termcolor.colored("Invalid time format. Please use HH:MM:SS format.", "red"))

    print(termcolor.colored(f"Alarm set for {alarm_time}", "green", "on_black", attrs=["blink"]))
    set_alarm(alarm_time)

if __name__ == "__main__":
    main()
