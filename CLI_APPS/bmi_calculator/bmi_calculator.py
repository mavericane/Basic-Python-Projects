# Author: Amin (Mavericane)
# GitHub Link: https://github.com/mavericane/
# Website Link: https://mavericane.ir
# Description: BMI Calculator with color-coded status, healthy weight range, and weight adjustment suggestion.

import termcolor  # For colored text output in the terminal

# BMI categories with limits, labels, color, and helpful messages
BMI_CATEGORIES = [
    {
        "limit": 16,
        "label": "Underweight (Severe thinness)",
        "color": "red",
        "message": "You are significantly underweight, consider consulting a healthcare professional.",
    },
    {
        "limit": 17,
        "label": "Underweight (Moderate thinness)",
        "color": "yellow",
        "message": "You are moderately underweight, a balanced diet may help.",
    },
    {
        "limit": 18.5,
        "label": "Underweight (Mild thinness)",
        "color": "cyan",
        "message": "You are slightly underweight, try to include nutritious meals.",
    },
    {
        "limit": 25,
        "label": "Normal",
        "color": "green",
        "message": "You have a healthy BMI, keep up the good work!",
    },
    {
        "limit": 30,
        "label": "Overweight (Pre-obese)",
        "color": "yellow",
        "message": "You are slightly overweight, consider healthy diet and exercise.",
    },
    {
        "limit": 35,
        "label": "Obese (Class I)",
        "color": "red",
        "message": "You are obese, consulting a healthcare professional is recommended.",
    },
    {
        "limit": 40,
        "label": "Obese (Class II)",
        "color": "red",
        "message": "You are severely obese, please seek medical guidance.",
    },
    {
        "limit": float("inf"),
        "label": "Obese (Class III)",
        "color": "red",
        "message": "You are extremely obese, urgent medical advice is recommended.",
    },
]

# Normal BMI range for healthy weight
NORMAL_BMI_RANGE = (18.5, 24.9)


def calculate_bmi(weight, height):
    """Calculate BMI given weight in kilograms and height in centimeters."""
    return weight / ((height / 100) ** 2)


def get_bmi_category(bmi):
    """Return the BMI category dictionary corresponding to the given BMI."""
    for category in BMI_CATEGORIES:
        if bmi < category["limit"]:
            return category
    return {
        "label": "Unknown",
        "color": "white",
        "message": "",
    }  # Fallback if BMI is invalid


def get_positive_float(prompt):
    """
    Prompt the user to enter a positive float.
    Users can enter 'q' to quit.
    """
    while True:
        user_input = input(prompt).strip()
        if user_input.lower() == "q":
            return None  # Signal to quit
        try:
            value = float(user_input)
            if value <= 0:
                print(termcolor.colored("Please enter a positive number.", "red"))
                continue
            return value
        except ValueError:
            print(
                termcolor.colored(
                    "Invalid input. Enter a number or 'q' to quit.", "red"
                )
            )


def calculate_normal_weight_range(height):
    """
    Calculate the weight range corresponding to normal BMI for a given height.
    Returns a tuple (min_weight, max_weight) in kilograms.
    """
    min_weight = round(NORMAL_BMI_RANGE[0] * ((height / 100) ** 2), 1)
    max_weight = round(NORMAL_BMI_RANGE[1] * ((height / 100) ** 2), 1)
    return min_weight, max_weight


def weight_adjustment_message(weight, min_weight, max_weight):
    """
    Generate a message indicating how much weight the user needs to gain or lose
    to reach the normal BMI range.
    """
    if weight < min_weight:
        diff = round(min_weight - weight, 1)
        return f"You need to gain approximately {diff} kg to reach the normal weight range."
    elif weight > max_weight:
        diff = round(weight - max_weight, 1)
        return f"You need to lose approximately {diff} kg to reach the normal weight range."
    else:
        return "You are within the normal weight range."


def main():
    """Main program loop."""
    print(termcolor.colored("=== BMI Calculator ===", "blue", attrs=["bold"]))
    print("Type 'q' at any prompt to quit.\n")

    while True:
        # Get user input
        weight = get_positive_float("Enter your weight in kilograms: ")
        if weight is None:
            break  # Quit program
        height = get_positive_float("Enter your height in centimeters: ")
        if height is None:
            break  # Quit program

        # Calculate BMI
        bmi = round(calculate_bmi(weight, height), 2)

        # Determine BMI category
        category = get_bmi_category(bmi)

        # Calculate healthy weight range and adjustment guidance
        min_weight, max_weight = calculate_normal_weight_range(height)
        adjustment_msg = weight_adjustment_message(weight, min_weight, max_weight)

        # Display results
        print(termcolor.colored(f"\nYour BMI is: {bmi}", "magenta"))
        print(termcolor.colored(f"Status: {category['label']}", category["color"]))
        print(termcolor.colored(f"Message: {category['message']}", "white"))
        print(
            termcolor.colored(
                f"Healthy weight range for your height: {min_weight}kg - {max_weight}kg",
                "green",
            )
        )
        print(termcolor.colored(adjustment_msg, "cyan"))
        print("-" * 60)  # Separator


if __name__ == "__main__":
    main()
