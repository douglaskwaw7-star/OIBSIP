"""BMI Calculator - calculates Body Mass Index and classifies it."""

import math


def get_positive_float(prompt, unit_hint):
    """Keep asking until the user enters a valid number greater than 0."""
    while True:
        raw = input(prompt).strip()
        try:
            value = float(raw)
        except ValueError:
            print(f"Error: '{raw}' is not a number. Please enter digits only, {unit_hint}.")
            continue

        if math.isnan(value) or math.isinf(value):
            print(f"Error: '{raw}' is not a valid value. Please enter a real number, {unit_hint}.")
        elif value < 0:
            print("Error: value cannot be negative. Please enter a positive number.")
        elif value == 0:
            print("Error: value cannot be zero. Please enter a number greater than 0.")
        else:
            return value


def calculate_bmi(weight_kg, height_m):
    """BMI = weight / (height ^ 2)"""
    return weight_kg / (height_m ** 2)


def classify_bmi(bmi):
    """Return the standard health category for a BMI value."""
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"


def main():
    print("=== BMI Calculator ===")
    weight = get_positive_float("Enter your weight (kg): ", "e.g. 70 or 68.5")
    height = get_positive_float("Enter your height (m): ", "e.g. 1.75")

    bmi = calculate_bmi(weight, height)
    category = classify_bmi(bmi)

    print(f"\nYour BMI is {bmi:.2f}")
    print(f"Category: {category}")


if __name__ == "__main__":
    main()
