"""Generate random passwords based on user-selected character counts."""

import random
import string

CHAR_SETS = {
    "lowercase": string.ascii_lowercase,
    "uppercase": string.ascii_uppercase,
    "digits": string.digits,
    "symbols": string.punctuation,
}


def prompt_count(label, chars):
    """Prompt for a non-negative count capped by available characters."""
    max_count = len(chars)
    while True:
        raw_value = input(f"How many {label} would you like in your password?\n==> ")
        try:
            count = int(raw_value)
        except ValueError:
            print("Please enter a valid number.")
            continue

        if 0 <= count <= max_count:
            return count
        print(f"Count must be between 0 and {max_count}.")


def build_password(counts):
    """Build a shuffled password string from requested counts."""
    password_chars = []
    for key, count in counts.items():
        password_chars.extend(random.choices(CHAR_SETS[key], k=count))

    random.shuffle(password_chars)
    return "".join(password_chars)


def run_once():
    """Collect requirements once and print a generated password."""
    counts = {
        "lowercase": prompt_count("lowercase letters", CHAR_SETS["lowercase"]),
        "uppercase": prompt_count("uppercase letters", CHAR_SETS["uppercase"]),
        "digits": prompt_count("numbers", CHAR_SETS["digits"]),
        "symbols": prompt_count("symbols", CHAR_SETS["symbols"]),
    }

    password = build_password(counts)
    print(f"Your password is: {password}")


def should_continue():
    """Return True unless the user explicitly types No."""
    answer = input("Generate another password? Type No to exit.\n==> ").strip().lower()
    return answer not in {"no", "n"}


def main():
    """Run the password generator until the user chooses to stop."""
    print("Welcome to Password Generator!")
    while True:
        run_once()
        if not should_continue():
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
