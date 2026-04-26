"""Quiz logic module for handling question flow and scoring."""

class QuizBrain:
    """Manage quiz question flow, answer checking, and score tracking."""

    def __init__(self, q_list):
        """Initialize the quiz state with a list of question objects."""
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.missed_questions = []

    @staticmethod
    def normalize_answer(user_answer):
        """Map user input to canonical True/False strings, or None when invalid."""
        normalized = user_answer.strip().lower()
        if normalized in {"true", "t"}:
            return "true"
        if normalized in {"false", "f"}:
            return "false"
        return None

    @staticmethod
    def _normalize_answer(user_answer):
        """Backward-compatible alias for normalize_answer."""
        return QuizBrain.normalize_answer(user_answer)

    def still_has_questions(self):
        """Return True when there are questions left to ask."""
        return self.question_number < len(self.question_list)

    def next_question(self):
        """Prompt the user with the next question and evaluate the response."""
        current_question = self.question_list[self.question_number]
        self.question_number += 1

        while True:
            user_answer = input(
                f"Q.{self.question_number}: {current_question.text} (True/False): "
            )
            if self._normalize_answer(user_answer) is not None:
                break
            print("Please enter a valid answer: True/False (or T/F).")

        self.check_answer(user_answer, current_question.answer, current_question.text)

    def check_answer(self, user_answer, correct_answer, question_text):
        """Compare normalized answers, update score, and return correctness."""
        is_correct = self._normalize_answer(user_answer) == self._normalize_answer(
            correct_answer
        )
        if is_correct:
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
            self.missed_questions.append(
                {
                    "question": question_text,
                    "your_answer": user_answer.strip(),
                    "correct_answer": correct_answer,
                }
            )
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")
        return is_correct

    def print_missed_recap(self):
        """Print a recap of questions missed in the current round."""
        if not self.missed_questions:
            print("Great job! You answered every question correctly.")
            return

        print("Review - Questions you missed:")
        for index, missed in enumerate(self.missed_questions, start=1):
            print(f"{index}. {missed['question']}")
            print(f"   Your answer: {missed['your_answer']}")
            print(f"   Correct answer: {missed['correct_answer']}")
