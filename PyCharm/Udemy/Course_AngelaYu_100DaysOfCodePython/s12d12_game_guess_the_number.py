"""Command-line number guessing game with difficulty levels and score multipliers."""

from collections.abc import Sequence
from random import randint
from typing import TypedDict
from utilities.guessthenumber_art import logo  # pylint: disable=import-error

# Turns
EASY_LEVEL_TURNS = 10
MEDIUM_LEVEL_TURNS = 7
HARD_LEVEL_TURNS = 5
# Factors
EASY_LEVEL_FACTOR = 1
MEDIUM_LEVEL_FACTOR = 2
HARD_LEVEL_FACTOR = 4
# Guess Threshold
CLOSE_GUESS_THRESHOLD = 5
FAR_GUESS_THRESHOLD = 15


DifficultySetting = tuple[str, int, int]


class RoundSummary(TypedDict):
    """Per-round summary used for final session reporting."""

    round_number: int
    difficulty_level: str
    attempts: int
    guessed_number: bool
    points_collected: int

DIFFICULTY_SETTINGS: dict[int, DifficultySetting] = {
    1: ("Easy", EASY_LEVEL_TURNS, EASY_LEVEL_FACTOR),
    2: ("Medium", MEDIUM_LEVEL_TURNS, MEDIUM_LEVEL_FACTOR),
    3: ("Hard", HARD_LEVEL_TURNS, HARD_LEVEL_FACTOR),
}


def check_answer(
    guess: int,
    answer: int,
    turns: int,
    difficulty_factor: int,
) -> tuple[int, bool]:
    """Compare guess to answer and return updated turns and match status."""
    if guess == answer:
        print(f"You got it RIGHT! The answer was {answer}.")
        print(f"You have earned {turns * difficulty_factor} points.")
        return turns, True

    difference = abs(guess - answer)
    if guess > answer:
        if difference >= FAR_GUESS_THRESHOLD:
            print("You are too high.")
        elif difference >= CLOSE_GUESS_THRESHOLD:
            print("You are high, but close.")
        else:
            print("You are very close, but little high.")
    else:
        if difference >= FAR_GUESS_THRESHOLD:
            print("You are too low.")
        elif difference >= CLOSE_GUESS_THRESHOLD:
            print("You are low, but close.")
        else:
            print("You are very close, but little low.")

    return turns - 1, False


def set_difficulty() -> DifficultySetting:
    """Sets Game Difficulty Level"""
    prompt = (
        "Choose a Difficulty Level.\n"
        "Type 1 for 'easy', 2 for 'medium', 3 for 'hard': "
    )
    level = int(input(prompt))
    return DIFFICULTY_SETTINGS.get(level, DIFFICULTY_SETTINGS[3])


def print_final_summary(round_summaries: list[RoundSummary]) -> None:
    """Print a table with per-round details and final totals."""
    headers = [
        "Round Number",
        "Difficulty Level",
        "Number of Attempts",
        "Guessed the Number",
        "Points Collected",
    ]

    rows: list[list[str]] = [
        [
            str(summary["round_number"]),
            summary["difficulty_level"],
            str(summary["attempts"]),
            "Yes" if summary["guessed_number"] else "No",
            str(summary["points_collected"]),
        ]
        for summary in round_summaries
    ]

    total_rounds = len(round_summaries)
    total_points = sum(summary["points_collected"] for summary in round_summaries)
    totals_row = [f"TOTAL ROUNDS: {total_rounds}", "", "", "", str(total_points)]

    all_rows: list[list[str]] = rows + [totals_row]
    column_widths = [
        max(len(headers[index]), *(len(row[index]) for row in all_rows))
        for index in range(len(headers))
    ]

    def format_row(values: Sequence[str]) -> str:
        return "| " + " | ".join(
            value.ljust(column_widths[index])
            for index, value in enumerate(values)
        ) + " |"

    def separator() -> str:
        return "+-" + "-+-".join("-" * width for width in column_widths) + "-+"

    print("\nFinal Game Summary")
    print(separator())
    print(format_row(headers))
    print(separator())
    for row in rows:
        print(format_row(row))
    print(separator())
    print(format_row(totals_row))
    print(separator())


def should_play_next_round() -> bool:
    """Ask the user whether to play another round."""
    while True:
        response = input(
            "Play another round? Type 'y' to continue or 'n' to exit: "
        ).strip().lower()
        if response in {"y", "yes"}:
            return True
        if response in {"n", "no", "exit", "quit"}:
            return False
        print("Please type 'y' to continue or 'n' to exit.")


def game(round_number: int) -> RoundSummary:
    """Play one round and return round summary data."""
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print()
    difficulty_level, turns, difficulty_factor = set_difficulty()
    print()
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)

    guess_number = 1
    attempts = 0
    while turns > 0:
        print(f"\nYou have {turns} attempts remaining to guess the number.")
        print()
        guess = int(input(f"Make guess #{guess_number}: "))
        print()
        attempts += 1

        turns, is_correct = check_answer(guess, answer, turns, difficulty_factor)
        if is_correct:
            points = turns * difficulty_factor
            return {
                "round_number": round_number,
                "difficulty_level": difficulty_level,
                "attempts": attempts,
                "guessed_number": True,
                "points_collected": points,
            }

        if turns == 0:
            print("You've run out of guesses, you lose.")
            return {
                "round_number": round_number,
                "difficulty_level": difficulty_level,
                "attempts": attempts,
                "guessed_number": False,
                "points_collected": 0,
            }

        guess_number += 1

        if guess != answer:
            print("Guess again.")

    # Defensive fallback for static analyzers; normal gameplay returns inside loop.
    return {
        "round_number": round_number,
        "difficulty_level": difficulty_level,
        "attempts": attempts,
        "guessed_number": False,
        "points_collected": 0,
    }


def main() -> None:
    """Run game rounds until the user explicitly exits."""
    round_summaries: list[RoundSummary] = []

    while True:
        round_number = len(round_summaries) + 1
        round_summaries.append(game(round_number))

        if not should_play_next_round():
            print("\nThanks for playing!")
            print_final_summary(round_summaries)
            return


if __name__ == "__main__":
    main()
