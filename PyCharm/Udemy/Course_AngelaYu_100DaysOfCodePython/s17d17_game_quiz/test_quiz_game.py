"""Unit tests for the Day 17 quiz app."""

import unittest
from types import SimpleNamespace
from unittest.mock import patch

from quiz_brain import QuizBrain
from quiz_main import ask_play_again


class TestNormalizeAnswer(unittest.TestCase):
    """Tests for input normalization logic."""

    def test_normalize_answer_accepts_true_variants(self):
        """Normalize true aliases to a canonical value."""
        self.assertEqual(QuizBrain.normalize_answer("True"), "true")
        self.assertEqual(QuizBrain.normalize_answer(" t "), "true")

    def test_normalize_answer_accepts_false_variants(self):
        """Normalize false aliases to a canonical value."""
        self.assertEqual(QuizBrain.normalize_answer("False"), "false")
        self.assertEqual(QuizBrain.normalize_answer("f"), "false")

    def test_normalize_answer_rejects_invalid_values(self):
        """Return None for unsupported inputs."""
        self.assertIsNone(QuizBrain.normalize_answer(""))
        self.assertIsNone(QuizBrain.normalize_answer("maybe"))


class TestCheckAnswer(unittest.TestCase):
    """Tests for score and missed-question tracking."""

    def test_check_answer_increments_score_when_correct(self):
        """Correct answers should increase score and not add misses."""
        quiz = QuizBrain([])
        quiz.question_number = 1

        is_correct = quiz.check_answer("t", "True", "Sample question")

        self.assertTrue(is_correct)
        self.assertEqual(quiz.score, 1)
        self.assertEqual(quiz.missed_questions, [])

    def test_check_answer_records_missed_question_when_wrong(self):
        """Wrong answers should not increase score and should be recorded."""
        quiz = QuizBrain([])
        quiz.question_number = 1

        is_correct = quiz.check_answer(" t ", "False", "Sample question")

        self.assertFalse(is_correct)
        self.assertEqual(quiz.score, 0)
        self.assertEqual(len(quiz.missed_questions), 1)
        self.assertEqual(quiz.missed_questions[0]["question"], "Sample question")
        self.assertEqual(quiz.missed_questions[0]["your_answer"], "t")
        self.assertEqual(quiz.missed_questions[0]["correct_answer"], "False")

    def test_next_question_reprompts_until_valid_answer(self):
        """Invalid input should trigger a reprompt and still process the question."""
        question = SimpleNamespace(text="Is Python fun?", answer="True")
        quiz = QuizBrain([question])

        with patch("builtins.input", side_effect=["maybe", "t"]):
            quiz.next_question()

        self.assertEqual(quiz.question_number, 1)
        self.assertEqual(quiz.score, 1)


class TestAskPlayAgain(unittest.TestCase):
    """Tests for replay prompt handling."""

    def test_ask_play_again_accepts_yes_values(self):
        """Yes-like inputs should return True."""
        with patch("builtins.input", side_effect=["yes"]):
            self.assertTrue(ask_play_again())

    def test_ask_play_again_accepts_no_values(self):
        """No-like inputs should return False."""
        with patch("builtins.input", side_effect=["n"]):
            self.assertFalse(ask_play_again())

    def test_ask_play_again_reprompts_after_invalid_input(self):
        """Invalid input should prompt again until accepted."""
        with patch("builtins.input", side_effect=["maybe", "y"]), patch(
            "builtins.print"
        ) as mock_print:
            self.assertTrue(ask_play_again())

        mock_print.assert_called_with("Please enter 'y', 'yes', 'n', or 'no'.")


class TestMissedRecap(unittest.TestCase):
    """Tests for end-of-round missed-question recap output."""

    def test_print_missed_recap_all_correct_message(self):
        """Print a success message when no questions were missed."""
        quiz = QuizBrain([])

        with patch("builtins.print") as mock_print:
            quiz.print_missed_recap()

        mock_print.assert_called_once_with(
            "Great job! You answered every question correctly."
        )

    def test_print_missed_recap_lists_all_missed_questions(self):
        """Print a numbered recap with user and correct answers."""
        quiz = QuizBrain([])
        quiz.missed_questions = [
            {
                "question": "Question one?",
                "your_answer": "t",
                "correct_answer": "False",
            },
            {
                "question": "Question two?",
                "your_answer": "f",
                "correct_answer": "True",
            },
        ]

        with patch("builtins.print") as mock_print:
            quiz.print_missed_recap()

        expected_calls = [
            (("Review - Questions you missed:",),),
            (("1. Question one?",),),
            (("   Your answer: t",),),
            (("   Correct answer: False",),),
            (("2. Question two?",),),
            (("   Your answer: f",),),
            (("   Correct answer: True",),),
        ]
        self.assertEqual(mock_print.call_args_list, expected_calls)


if __name__ == "__main__":
    unittest.main()
