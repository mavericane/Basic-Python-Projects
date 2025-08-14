# Author: Amin (Mavericane)
# GitHub: https://github.com/mavericane/
# Website: https://mavericane.ir
# Description: Calculates precise age, with optional leap year day inclusion.

import datetime
from termcolor import colored
from dateutil.relativedelta import relativedelta

MONTHS = [
    "1. January",
    "2. February",
    "3. March",
    "4. April",
    "5. May",
    "6. June",
    "7. July",
    "8. August",
    "9. September",
    "10. October",
    "11. November",
    "12. December",
]

today = datetime.date.today()


def input_int(prompt, min_val, max_val, future_check=None):
    """Safe integer input with validation."""
    while True:
        try:
            value = int(input(prompt))
            if min_val <= value <= max_val:
                if future_check and not future_check(value):
                    print(
                        colored("Your date of birth cannot be in the future.", "yellow")
                    )
                else:
                    return value
            else:
                print(
                    colored(
                        f"Please enter a number between {min_val} and {max_val}", "red"
                    )
                )
        except ValueError:
            print(colored("Invalid input. Please enter a valid number.", "red"))


# Year
birth_year = input_int(
    "Please enter the year you were born: ", 0, today.year, lambda y: y <= today.year
)

# Month
print(MONTHS)
birth_month = input_int(
    "Please enter the month you were born (number): ",
    1,
    12,
    lambda m: not (birth_year == today.year and m > today.month),
)

# Day
if birth_year == today.year and birth_month == today.month:
    max_day = today.day
else:
    max_day = (
        datetime.date(birth_year, birth_month, 28) + datetime.timedelta(days=4)
    ).replace(day=1) - datetime.timedelta(days=1)
    max_day = max_day.day

birth_day = input_int(
    f"Please enter the day you were born (1-{max_day}): ",
    1,
    max_day,
    lambda d: not (
        birth_year == today.year and birth_month == today.month and d > today.day
    ),
)

birth_date = datetime.date(birth_year, birth_month, birth_day)

# Calculate age
age_delta = relativedelta(today, birth_date)
age_in_days = (today - birth_date).days

print(
    colored(
        f"You have lived for: {age_delta.years} years, {age_delta.months} months, and {age_delta.days} days",
        "green",
    )
)
print(colored(f"You have lived for: {age_in_days} days", "green"))

# Leap year count
leap_days = sum(
    1
    for year in range(birth_year, today.year + 1)
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0
)

if leap_days > 0:
    choice = (
        input(colored("Consider leap years extra days? (Y/N): ", "cyan"))
        .strip()
        .lower()
    )
    if choice in ("y", "yes"):
        print(colored(f"You lived {leap_days} days in leap years", "green"))
        adjusted_days = age_in_days + leap_days
        print(colored(f"With leap years: {adjusted_days} days", "green"))
else:
    print(
        colored(
            "You did not live in a leap year (probably you are less than 4 years old xD)",
            "green",
        )
    )
