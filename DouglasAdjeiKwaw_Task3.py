import random
import string


def get_password_length():
    """Ask the user for a valid password length."""

    while True:
        try:
            length = int(input("\nEnter password length (minimum 8): "))

            if length < 8:
                print("❌ Password must be at least 8 characters long.")
            else:
                return length

        except ValueError:
            print("❌ Please enter a valid number.")


def get_character_types():
    """Ask the user which character types to include."""

    while True:
        print("\nChoose the character types to include:")
        print("1. Uppercase letters (A-Z)")
        print("2. Lowercase letters (a-z)")
        print("3. Numbers (0-9)")
        print("4. Symbols (!@#$%^&*...)")

        choice = input(
            "\nEnter your choices separated by commas "
            "(example: 1,2,3,4): "
        )

        choices = set(choice.replace(" ", "").split(","))

        valid_choices = {"1", "2", "3", "4"}

        # Check whether all choices are valid
        if not choices.issubset(valid_choices):
            print("❌ Invalid choice. Please choose only 1, 2, 3, or 4.")
            continue

        # At least two character types are required
        if len(choices) < 2:
            print("❌ Please select at least TWO character types.")
            continue

        return choices


def generate_password(length, choices):
    """Generate a password based on the user's selected criteria."""

    character_sets = []

    # Store the selected character groups
    if "1" in choices:
        character_sets.append(string.ascii_uppercase)

    if "2" in choices:
        character_sets.append(string.ascii_lowercase)

    if "3" in choices:
        character_sets.append(string.digits)

    if "4" in choices:
        character_sets.append(string.punctuation)

    # Make sure every selected type appears at least once
    password_characters = [
        random.SystemRandom().choice(character_set)
        for character_set in character_sets
    ]

    # Combine all selected character types
    all_characters = "".join(character_sets)

    # Fill the remaining positions
    remaining = length - len(password_characters)

    for _ in range(remaining):
        password_characters.append(
            random.SystemRandom().choice(all_characters)
        )

    # Shuffle the password so required characters are not predictable
    random.SystemRandom().shuffle(password_characters)

    return "".join(password_characters)


def main():
    print("=" * 45)
    print("       RANDOM PASSWORD GENERATOR")
    print("=" * 45)

    while True:

        # Get password length
        length = get_password_length()

        # Get character types
        choices = get_character_types()

        # Generate password
        password = generate_password(length, choices)

        # Display password
        print("\n" + "=" * 45)
        print("Generated Password:")
        print(password)
        print("=" * 45)

        # Ask whether the user wants another password
        while True:
            again = input(
                "\nGenerate another password? (y/n): "
            ).lower().strip()

            if again == "y":
                break

            elif again == "n":
                print("\nThank you for using the Password Generator!")
                return

            else:
                print("❌ Please enter 'y' or 'n'.")


# Start the program
if __name__ == "__main__":
    main()