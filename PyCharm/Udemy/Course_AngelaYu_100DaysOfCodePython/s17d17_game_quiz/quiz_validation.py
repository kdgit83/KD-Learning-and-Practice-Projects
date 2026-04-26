"""Quiz questions data module with typed records and startup validation."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, TypedDict, cast


class QuestionRecord(TypedDict):
    """Schema for one quiz question record."""

    category: str
    type: str
    difficulty: str
    question: str
    correct_answer: str
    incorrect_answers: list[str]


_REQUIRED_KEYS = {
    "category": str,
    "type": str,
    "difficulty": str,
    "question": str,
    "correct_answer": str,
    "incorrect_answers": list,
}


def _validate_record(record: dict[str, Any], index: int) -> None:
    """Validate a single record and raise ValueError with context when invalid."""
    for key, expected_type in _REQUIRED_KEYS.items():
        if key not in record:
            raise ValueError(f"Question #{index} is missing required key: {key}")
        if not isinstance(record[key], expected_type):
            actual = type(record[key]).__name__
            expected = expected_type.__name__
            raise ValueError(
                f"Question #{index} key '{key}' must be {expected}, got {actual}"
            )

    incorrect_answers = record["incorrect_answers"]
    if not incorrect_answers:
        raise ValueError(f"Question #{index} must include at least one incorrect answer")
    if not all(isinstance(item, str) for item in incorrect_answers):
        raise ValueError(f"Question #{index} has non-string values in incorrect_answers")


def _validate_question_data(records: list[dict[str, Any]]) -> list[QuestionRecord]:
    """Validate all records and return the validated question list."""
    validated: list[QuestionRecord] = []
    for index, record in enumerate(records, start=1):
        _validate_record(record, index)
        validated.append(cast(QuestionRecord, cast(object, record)))
    return validated


def load_question_data() -> list[QuestionRecord]:
    """Load question data from `quiz_data.json` beside this module."""
    data_path = Path(__file__).with_name("quiz_data.json")
    with data_path.open("r", encoding="utf-8") as source_file:
        raw_data = json.load(source_file)

    if not isinstance(raw_data, list):
        raise ValueError("Question data file must contain a JSON list of records")
    if not all(isinstance(item, dict) for item in raw_data):
        raise ValueError("Each question entry must be a JSON object")

    return _validate_question_data(cast(list[dict[str, Any]], raw_data))


question_data: list[QuestionRecord] = load_question_data()
