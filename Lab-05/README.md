# Lab 5: Static Code Analysis

## Objective

To analyze the Radio Schedule Python application using static code analysis tools, identify code-quality and security issues, fix the identified problems, and compare the results before and after modification.

## Tools Used

- **Pylint:** Analyzes Python code quality and coding conventions.
- **Flake8:** Checks Python style and formatting violations.
- **Bandit:** Detects potential security vulnerabilities in Python code.

## Issues Identified and Fixes

| No. | Issue | Fix Implemented |
|---:|---|---|
| 1 | Hardcoded password | Removed the hardcoded credential. |
| 2 | SQL injection risk | Replaced dynamically constructed SQL queries with parameterized queries. |
| 3 | Unsafe `eval()` usage | Replaced unrestricted evaluation with a restricted AST-based evaluator. |
| 4 | Non-standard function names | Applied Python `snake_case` naming conventions. |
| 5 | Missing docstrings | Added documentation to functions and relevant code sections. |
| 6 | Flake8 style violations | Fixed line-length and multiple-statement formatting issues. |
| 7 | Unnecessary global state | Removed the unnecessary global counter. |
| 8 | Broad exception handling | Narrowed exception handling to specific expected errors. |
| 9 | Non-preferred string formatting | Used f-strings where appropriate. |
| 10 | Missing main guard | Added `if __name__ == "__main__":` to control script execution. |

## Before-and-After Results

| Tool | Before | After |
|---|---|---|
| Pylint | 2.41/10 | 10/10 |
| Bandit | 3 findings | 0 findings |
| Flake8 | Style violations reported | No violations reported |

## Files Included

- `radio_schedule.py` — Modified source code.
- `radio_schedule_before.py` — Original source code for comparison.
- `pylint_before.txt` and `pylint_after.txt` — Pylint reports.
- `flake8_before.txt` and `flake8_after.txt` — Flake8 reports.
- `bandit_before.txt` and `bandit_after.txt` — Bandit reports.
- `issues.md` — Issue analysis.
- `reflection.md` — Learning reflection.
- `Lab5_Static_Code_Analysis_Report.docx` — Lab report.

## Conclusion

Static code analysis helped identify security risks, coding-quality problems, and style violations in the Radio Schedule application. The fixes improved the Pylint score from 2.41/10 to 10/10, reduced Bandit findings from three to zero, and eliminated the reported Flake8 violations.

These results reflect the checks performed by the selected tools and do not guarantee that the application is entirely free of defects or security vulnerabilities.
