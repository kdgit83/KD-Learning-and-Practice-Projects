"""Main module for running the quiz game."""

import random

from question_model import Question # pylint: disable=import-error
from quiz_validation import question_data  # pylint: disable=import-error
from quiz_brain import QuizBrain    # pylint: disable=import-error


def build_question_bank():
    """Create Question objects from raw question data."""
    question_bank = []
    for question in question_data:
        question_text = question["question"]
        question_answer = question["correct_answer"]
        new_question = Question(question_text, question_answer)
        question_bank.append(new_question)

    # Shuffle each round so replay runs feel different.
    random.shuffle(question_bank)
    return question_bank


def run_quiz_once():
    """Run one full quiz round and print the final score."""
    quiz = QuizBrain(build_question_bank())
    total_questions = len(quiz.question_list)

    while quiz.still_has_questions():
        print(f"Question {quiz.question_number + 1}/{total_questions}")
        quiz.next_question()

    print("You've completed the quiz")
    print(f"Your final score was: {quiz.score}/{quiz.question_number}")
    quiz.print_missed_recap()


def ask_play_again():
    """Return True if the user wants to play another round."""
    while True:
        play_again = input("Do you want to play again? (y/n or yes/no): ").strip().lower()
        if play_again in {"y", "yes", "n", "no"}:
            return play_again in {"y", "yes"}
        print("Please enter 'y', 'yes', 'n', or 'no'.")


def main():
    """Run the quiz and optionally restart based on user input."""
    while True:
        run_quiz_once()
        if not ask_play_again():
            print("Thanks for playing!")
            break
        print()


if __name__ == "__main__":
    main()
