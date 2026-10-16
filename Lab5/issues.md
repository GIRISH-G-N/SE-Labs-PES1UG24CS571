\# Lab 5 — Static Code Analysis Issues



| Issue | Type | Line(s) | Description | Fix Approach |

|---|---|---|---|---|

| SQL query built using string formatting | Security — Medium | Original line 11 | User-controlled values were inserted directly into SQL, creating SQL injection risk. | Replaced string formatting with parameterized SQL placeholders (`?`). |

| Use of `eval()` | Security — Medium | Original line 21 | Arbitrary expressions could execute through `eval()`. | Replaced it with an AST evaluator that permits only approved arithmetic and comparison operations. |

| Hardcoded password | Security — Low | Original line 7 | A studio password was stored directly in the source code. | Removed the unused hardcoded password. |

| Non-snake\_case function names | Code quality | Original lines 10, 15, 30, 35 | Function names did not follow standard Python naming conventions. | Renamed functions to `add\_slot`, `slot\_label`, `overlap\_free`, `morning\_shows`, and `remove\_slot`. |

| Missing documentation strings | Code quality | Multiple original lines | The module and functions lacked docstrings. | Added module-level and function-level docstrings. |

| Lines too long and multiple statements on one line | Style | Original lines 4, 11, 27 | Formatting violations made the code less readable and failed Flake8 checks. | Split long expressions across lines and separated statements. |

| Unnecessary global variable | Code quality | Original lines 6, 9–12, 30–31 | `booked\_minutes` required global mutable state and was used to control the morning-show query unnecessarily. | Removed the counter and made `morning\_shows()` query the schedule directly. |



\## Verification



\- Pylint: improved from 2.41/10 to 10.00/10.

\- Bandit: the original report contained three findings; the final report reported no issues.

\- Flake8: the final check completed without violations.

