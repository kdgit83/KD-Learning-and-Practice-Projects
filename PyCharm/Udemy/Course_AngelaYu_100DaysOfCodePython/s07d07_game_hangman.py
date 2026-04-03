"""Hangman game with replay support."""

import random

from utilities.hangman_art import logo, stages  # pylint: disable=import-error
from utilities.hangman_words import word_list  # pylint: disable=import-error


def prompt_guess(guessed_letters):
    """Prompt for one new alphabetic character."""
    while True:
        guess = input("Guess a letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter exactly one letter.")
            continue

        if guess in guessed_letters:
            print(f"You've already guessed {guess}")
            continue

        return guess


def play_round():
    """Play one round of hangman and return True on win, False on loss."""
    chosen_word = random.choice(word_list)
    display = ["_"] * len(chosen_word)
    lives = len(stages) - 1
    guessed_letters = set()

    print(logo)
    print("\t\t\tWelcome to Hangman")
    print(f"You have to guess the word for {''.join(display)}")
    print(f"It consists of {len(display)} letters.\n")

    while lives > 0 and "_" in display:
        guess = prompt_guess(guessed_letters)
        guessed_letters.add(guess)

        if guess in chosen_word:
            for position, char in enumerate(chosen_word):
                if char == guess:
                    display[position] = guess
        else:
            lives -= 1
            print(f"You guessed {guess}, that's not in the word. You lose a life.")

        print(f"\nCurrent status of the word: {''.join(display)}\n")
        print(stages[lives])

    if "_" not in display:
        print("You win!! End of Game!!")
        return True

    print("You lose! End of Game!")
    print(f"The solution is: {chosen_word}")
    return False


def main():
    """Run hangman until the user decides to stop."""
    while True:
        play_round()
        again = input("\nPlay again? Type No to exit.\n==> ").strip().lower()
        if again in {"no", "n"}:
            print("Thanks for playing Hangman!")
            break
        print()


if __name__ == "__main__":
    main()
