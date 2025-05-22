# Author: Amin (Mavericane)
# Github Link: https://github.com/mavericane/
# Website Link: https://mavericane.ir
# Description: This program is a simple alarm clock that plays a sound as an alarm at the set time.
# System requirements:
## Operating System: Windows, Linux, Mac OS

# Importing required modules
# argparse module for optional CLI argument support
import argparse

# Path function from pathlib module for detecting running file location if script is running as a .py file
from pathlib import Path

# sys module for detecting running file location if script is compiled
import sys

# time module for setting an alarm
import time

# termcolor module for colorizing outputs
import termcolor

# os module for suppressing pygame welcome message
import os


# pygame module for simply playing an alarm sound, imported silently
def import_pygame_silently():
    original_stdout = sys.stdout
    sys.stdout = open(os.devnull, "w")  # Redirect stdout to null device
    import pygame

    sys.stdout.close()
    sys.stdout = original_stdout
    return pygame


pygame = import_pygame_silently()

# keyboard module to detect user interaction
import keyboard

# Detect file location (supports both .py and compiled executable)
if getattr(sys, "frozen", False):
    file_location = Path(sys.executable).parent
else:
    file_location = Path(__file__).resolve().parent


# Parse optional command-line arguments using argparse
def parse_args():
    parser = argparse.ArgumentParser(description="Simple Alarm Clock")
    parser.add_argument("alarm_time", nargs="?", help="Alarm time in HH:MM:SS format")
    return parser.parse_args()


# Play alarm sound file
def play_alarm_sound(sound_file):
    sound_path = file_location / sound_file
    pygame.mixer.init()
    try:
        pygame.mixer.music.load(str(sound_path))
    except pygame.error as error:
        print(termcolor.colored(f"Error loading sound file: {error}", "red"))
        sys.exit(1)

    print("Alarm is ringing... Press 'S' to stop.")

    while True:
        pygame.mixer.music.play()
        # Wait for the sound to finish or for 's' key press
        while pygame.mixer.music.get_busy():
            if keyboard.is_pressed("s"):
                print("Alarm stopped.")
                pygame.mixer.music.stop()
                sys.exit()
            time.sleep(0.1)


# Set alarm for user requested time
def set_alarm(alarm_time):
    try:
        while True:
            current_time = time.strftime("%H:%M:%S")
            if current_time == alarm_time:
                print("ALARM! Wake up!")
                print("Press 'S' to stop alarm.")
                play_alarm_sound("alarm.mp3")
            time.sleep(1)
    except KeyboardInterrupt:
        print(termcolor.colored("Alarm cancelled by user.", "red"))
        sys.exit()


# Main function to run the program
def main():
    args = parse_args()

    print("Simple Alarm Clock")

    # Ask for alarm time if not passed as argument, and validate
    alarm_time = args.alarm_time
    while True:
        if alarm_time:
            try:
                time.strptime(alarm_time, "%H:%M:%S")
                break
            except ValueError:
                print(
                    termcolor.colored(
                        "Invalid time format. Please use HH:MM:SS format.", "red"
                    )
                )
        print(
            termcolor.colored(
                "Note: Please enter the full Hour:Minute:Second format like 03:05:01",
                "yellow",
                "on_black",
            )
        )
        alarm_time = input("Set the alarm time (HH:MM:SS format): ")

    print(
        termcolor.colored(
            f"Alarm set for {alarm_time}", "green", "on_black", attrs=["blink"]
        )
    )
    print(termcolor.colored("Press Ctrl+C to cancel before the alarm rings.", "cyan"))
    # Start monitoring time
    set_alarm(alarm_time)


if __name__ == "__main__":
    main()
