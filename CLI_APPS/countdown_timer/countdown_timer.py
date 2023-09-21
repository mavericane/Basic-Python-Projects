# Author: Amin (Mavericane)
# Github Link: https://github.com/mavericane/
# Website Link: https://mavericane.ir
# Description: This program is a simple countdown timer program that will play a sound as an alarm when timer reaches 00:00
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


# Function to get user input for the countdown duration
def get_countdown_duration():
    while True:
        try:
            duration = int(input("Enter countdown duration in seconds: "))
            if duration >= 0:
                return duration
            else:
                print(termcolor.colored("Please enter a non-negative number.", "red"))
        except ValueError:
            print(
                termcolor.colored("Invalid input. Please enter a valid number.", "red")
            )


# Function to start the countdown timer
def countdown_timer(duration):
    for remaining_duration in range(duration, 0, -1):
        minutes, seconds = divmod(remaining_duration, 60)
        print(
            termcolor.colored(f"Time left: {minutes:02d}:{seconds:02d}", "yellow"),
            end="\r",
        )
        time.sleep(1)

    print(termcolor.colored("Time left: 00:00", "yellow"))
    print(termcolor.colored("Time's up!", "green", "on_black", ["blink"]))
    play_alarm_sound("alarm.mp3")


if __name__ == "__main__":
    print("Simple Countdown Timer")
    countdown_duration = get_countdown_duration()
    countdown_timer(countdown_duration)
