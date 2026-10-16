# Lab 5: Static Code Analysis — Radio Station Programme Schedule

**Student:** Girish G N  
**Repository:** https://github.com/GIRISH-G-N/L5_22_radio_schedule  
**Main program:** `radio_schedule.py`

## About the Project

This lab uses Pylint, Bandit, and Flake8 to identify code quality, security, and style issues in a Python radio programme scheduling application.

The program supports adding radio show slots, generating show labels, checking timing expressions, listing morning shows, and removing scheduled slots.

## Tools Used

- **Pylint:** Checks code quality, naming conventions, documentation, and maintainability.
- **Bandit:** Identifies potential security vulnerabilities.
- **Flake8:** Checks Python style and formatting.

## Changes Made

- Replaced dynamically constructed SQL queries with parameterized queries.
- Removed the hardcoded studio password.
- Replaced unrestricted `eval()` with a restricted expression evaluator.
- Renamed functions to follow Python's `snake_case` convention.
- Added module and function docstrings.
- Improved code formatting and line lengths.
- Removed the unnecessary global booking counter.

## Static Analysis Results

| Tool | Before | After |
|---|---|---|
| Pylint | 2.41/10 | 10.00/10 |
| Bandit | 3 reported issues | No issues reported |
| Flake8 | Multiple style violations | No violations |

See the corresponding `*_before.txt` and `*_after.txt` files for the saved reports.

## Running the Program

Activate the virtual environment, install the required tools, and run:

```bash
python radio_schedule.py
```

Run the analysis tools with:

```bash
pylint radio_schedule.py
bandit -r radio_schedule.py
flake8 radio_schedule.py
```

## Version Control

The project history includes commits for the corrected program, before-and-after analysis reports, and the original program for comparison.

## Deliverables

- `radio_schedule.py` — corrected program.
- `radio_schedule_before.py` — original program for comparison.
- `pylint_before.txt` and `pylint_after.txt`.
- `bandit_before.txt` and `bandit_after.txt`.
- `flake8_before.txt` and `flake8_after.txt`.
- `issues.md` — issue table.
- `reflection.md` — reflection answers.
- Lab report DOCX — issue table, analysis reports, and reflections.
