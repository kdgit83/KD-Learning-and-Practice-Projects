"""Shared input validation helpers for the OOP coffee machine."""

INVALID_NUMBER_MESSAGE = "Invalid input. Please enter a non-negative whole number."


def read_non_negative_int(prompt: str) -> int:
    """Prompts until the user enters a non-negative whole number."""
    while True:
        raw_value = input(prompt).strip()
        if raw_value.isdigit():
            return int(raw_value)
        print(INVALID_NUMBER_MESSAGE)
