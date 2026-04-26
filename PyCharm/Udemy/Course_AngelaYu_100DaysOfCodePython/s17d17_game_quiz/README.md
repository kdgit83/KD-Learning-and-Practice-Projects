# Quiz App (Day 17)

A simple command-line True/False quiz app built with Python.

## What This App Does

- Loads quiz questions from `quiz_data.json`
- Validates the question schema at startup via `quiz_validation.py`
- Converts each record into a `Question` object
- Shuffles questions at the start of each round
- Shows question progress (`Question X/Y`) while you play
- Runs an interactive quiz loop, tracks your score, and supports replay
- Prints a recap of missed questions at the end of each round

## Project Files

- `quiz_main.py` - entry point that builds the question bank and runs the quiz
- `question_model.py` - `Question` data model
- `quiz_brain.py` - quiz flow, prompting, answer checking, score reporting
- `quiz_validation.py` - JSON loading, validation, and `question_data` export
- `quiz_data.json` - raw quiz question dataset

## Requirements

- Python 3.10+ (uses modern type hints)

## Run The App

From this folder (`s17d17_game_quiz`):

```powershell
python quiz_main.py
```

## Run Tests

From this folder (`s17d17_game_quiz`):

```powershell
python -m unittest -v
```

## Data Format

Each question record in `quiz_data.json` uses this shape:

```json
{
  "category": "Science: Computers",
  "type": "boolean",
  "difficulty": "easy|medium|hard",
  "question": "Question text",
  "correct_answer": "True|False",
  "incorrect_answers": ["..."]
}
```

If a record is malformed (missing keys, wrong types, empty/invalid `incorrect_answers`),
`quiz_validation.py` raises a `ValueError` during import so problems are caught early.

## Linting Notes

This project includes a few targeted inline pylint suppressions (for example, import
resolution in `quiz_main.py`) to fit local execution style and learning-project structure
