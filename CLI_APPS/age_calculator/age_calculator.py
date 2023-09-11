# Author: Amin (Mavericane)
# GitHub Link: https://github.com/mavericane/
# Website Link: https://mavericane.ir
# Description: This program accurately calculates the age of people including leap years (selectable).
# Importing required modules
# datetime module for retrieving today's date
import datetime

# termcolor module for colorizing outputs
import termcolor

# Retrieving today's date
today = datetime.date.today()

# Year selection
while True:
    try:
        birthyear = int(input("Please enter the year you were born: "))
        if today.year >= birthyear >= 0:
            break
        else:
            print(
                termcolor.colored(
                    "Your date of birth cannot be in the future.", "yellow"
                )
            )
    except:
        print("Please enter a valid year")
print(
    [
        "1.January",
        "2.February",
        "3.March",
        "4.April",
        "5.May",
        "6.June",
        "7.July",
        "8.August",
        "9.September",
        "10.October",
        "11.November",
        "12.December",
    ]
)

# Month selection
while True:
    try:
        birthmonth = int(
            input("Please enter the month you were born(Number of month): ")
        )
        if birthyear == today.year:
            if today.month >= birthmonth >= 1:
                break
            else:
                print(
                    termcolor.colored(
                        "Your date of birth cannot be in the future.", "yellow"
                    )
                )
        else:
            break
    except:
        print(termcolor.colored("Please enter a valid month", "red"))

# Determining days of the month available (considering leap year 29 February)
if birthyear == today.year and birthmonth == today.month:
    days = today.day
else:
    if (
        birthmonth == 1
        or birthmonth == 3
        or birthmonth == 5
        or birthmonth == 7
        or birthmonth == 8
        or birthmonth == 10
        or birthmonth == 12
    ):
        days = 31
    elif birthmonth == 2:
        if (birthyear % 4 == 0 and birthyear % 100 != 0) or birthyear % 400 == 0:
            days = 29
        else:
            days = 28
    else:
        days = 30

# Day selection
while True:
    try:
        birthday = int(
            input(f"Please enter the date you were born days between: 1-{days}: ")
        )
        if days >= birthday >= 1:
            break
        elif (
            birthyear == today.year
            and birthmonth == today.month
            and birthday > today.day
        ):
            print(
                termcolor.colored(
                    "Your date of birth cannot be in the future.", "yellow"
                )
            )
        else:
            print(termcolor.colored("Please enter a valid day", "red"))
    except:
        print(termcolor.colored("Please enter a valid day", "red"))

# Calculating leap years within the range of year of birth and year living in
leap_counter = 0
for i in range(birthyear, today.year):
    if (i % 4 == 0 and i % 100 != 0) or i % 400 == 0:
        leap_counter += 1
if (today.year % 4 == 0 and today.year % 100 != 0) or today.year % 400 == 0:
    if today.month > 2 or (today.month == 2 and today.day == 29):
        leap_counter += 1

# Calculating years lived
if birthyear == today.year:
    lived_years = 0
elif birthyear == today.year - 1 and birthmonth >= today.month and birthday > today.day:
    lived_years = 0
else:
    if birthmonth == today.month and birthday > today.day:
        lived_years = (today.year - birthyear) - 1
    elif birthmonth > today.month:
        lived_years = today.year - birthyear - 1
    else:
        lived_years = today.year - birthyear

# Calculating months lived
if birthmonth < today.month - 1 + 12 and birthday > today.day:
    lived_months = today.month - birthmonth + 12 - 1
elif birthmonth == today.month - 1 + 12 and birthday > today.day:
    lived_months = today.month - 1
else:
    if today.month - birthmonth == 0:
        lived_months = 0
    else:
        lived_months = today.month - birthmonth + 12

# Calculating days lived
if birthmonth == today.month - 1 + 12 and birthday > today.day:
    lived_days = today.day - birthday + days
else:
    if today.day - birthday == 0:
        lived_days = 0
    elif today.month - birthmonth == 0 and birthday < today.day:
        lived_days = today.day - birthday
    else:
        lived_days = today.day - birthday + days

# Calculating age in days
birthdate = f"{birthyear}-{birthmonth}-{birthday}"
birthdate = datetime.datetime.strptime(birthdate, "%Y-%m-%d").date()
age_in_days = (today - birthdate).days

# Age output
print(
    termcolor.colored(
        f"You have lived for: {lived_years} years, {lived_months} months and {lived_days} days",
        "green",
    )
)
print(termcolor.colored(f"You have lived for: {age_in_days} days", "green"))

# Calculating age with considring extra days in leap years
if leap_counter > 0:
    while True:
        consider_leap = input(
            termcolor.colored(
                "Do you want to consider leap years and extra 1 day(s) in your age? (Y yes, N no): ",
                "cyan",
            )
        )
        if consider_leap.casefold() == "y" or consider_leap.casefold() == "yes":
            print(f"You lived {leap_counter} days in leap years")
            if lived_days + leap_counter >= 31:
                lived_months = lived_months + 1
                lived_days_with_leap = lived_days + leap_counter - 31
                print(
                    termcolor.colored(
                        f"You have lived for {lived_years} years, {lived_months} months and {lived_days_with_leap} days.",
                        "green",
                    )
                )
            else:
                print(
                    termcolor.colored(
                        f"You have lived for {lived_years} years, {lived_months} months and {lived_days+leap_counter} days.",
                        "green",
                    )
                )
            print(
                termcolor.colored(
                    f"You have lived for: {age_in_days+leap_counter} days", "green"
                )
            )
            break
        elif consider_leap.casefold() == "n" or consider_leap.casefold() == "no":
            exit()
        else:
            print(termcolor.colored("Your entered option is not valid!", "red"))
else:
    print(
        termcolor.colored(
            "You did not live in a leap year (probably you are less than 4 years old xD)",
            "green",
        )
    )
