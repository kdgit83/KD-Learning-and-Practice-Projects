"""Question model class for the quiz game."""

class Question:  # pylint: disable=too-few-public-methods
    """Represents a quiz question and its correct answer."""

    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer
