# BMI Calculator

A command-line Python program that calculates a user's Body Mass Index (BMI) and classifies it into a standard health category.

**Tech stack:** Python 3, `input()`, basic arithmetic (no external libraries).

## Features

- Prompts for weight (kg) and height (m) via the command line
- Calculates BMI using `BMI = weight / (height ^ 2)`
- Classifies the result as Underweight, Normal, Overweight, or Obese
- Displays the BMI rounded to 2 decimal places, plus the category
- Validates input: rejects non-numeric, negative, and zero values with a helpful message

## How to Run

```bash
python bmi_calculator.py
```

Requires Python 3.6+.

### Example

```
=== BMI Calculator ===
Enter your weight (kg): abc
Error: 'abc' is not a number. Please enter digits only, e.g. 70 or 68.5.
Enter your weight (kg): 70
Enter your height (m): 1.75

Your BMI is 22.86
Category: Normal
```

## BMI Categories

| BMI | Category |
|---|---|
| below 18.5 | Underweight |
| 18.5 to 24.9 | Normal |
| 25 to 29.9 | Overweight |
| 30 or above | Obese |

The code uses `< 25` and `< 30` as upper bounds instead of `24.9` and `29.9`, so values like 24.95 don't fall between categories.

## Code Walkthrough

The program is split into four small functions.

### `get_positive_float(prompt, unit_hint)`

Asks the user for a number and keeps asking until the input is valid. It runs in a `while True` loop and checks, in order:

1. **Non-numeric input:** `float(raw)` raises `ValueError`, so the program prints an error with an example of valid input.
2. **`nan` / `inf`:** Python's `float()` accepts these strings, so `math.isnan` and `math.isinf` reject them.
3. **Negative values:** rejected with a clear message.
4. **Zero:** rejected, because a height of 0 would cause a divide-by-zero error.

Once the value passes every check, it is returned.

### `calculate_bmi(weight_kg, height_m)`

Applies the formula `weight_kg / (height_m ** 2)` and returns the result.

### `classify_bmi(bmi)`

Uses an `if / elif / else` chain to return the matching category name. Because the checks run from lowest to highest, each `elif` only needs an upper bound.

### `main()`

Ties everything together: it prints a header, collects weight and height, calculates and classifies the BMI, and prints the result formatted to 2 decimal places using `f"{bmi:.2f}"`.

The script ends with `if __name__ == "__main__": main()`, so the program runs only when executed directly and the functions can be imported into other files without side effects.

## Project Structure

```
.
├── bmi_calculator.py
└── README.md
```

## Notes

- Height must be entered in **meters** (e.g. `1.75`, not `175`).
- BMI is a general screening measure. It doesn't account for muscle mass, age, or body composition, and it isn't a medical diagnosis.
