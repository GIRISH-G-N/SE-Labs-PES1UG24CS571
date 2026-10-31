\# Lab 06: Code and Branch Coverage Analysis



\*\*Name:\*\* Girish G N

\*\*SRN:\*\* PES1UG24CS571

\*\*Assigned repo:\*\* L6\_L7\_22\_hotel\_booking



\## Forked repo (code and test files)



https://github.com/GIRISH-G-N/L6\_L7\_22\_hotel\_booking



The fork contains:

\- `CodeCoverageTest\_hotel\_booking.py` (test cases for line coverage)

\- `BranchCoverageTest\_hotel\_booking.py` (test cases for branch coverage)

\- `code\_coverage.png` and `branch\_coverage.png` (result screenshots)



\## What I did



1\. Installed `coverage` and `pytest`.

2\. Cloned the assigned repo, then forked it, since I had no push access to the original.

3\. Ran the given test file to get the starting coverage (before).

4\. Added tests in `CodeCoverageTest\_hotel\_booking.py` to reach more than 90% line coverage, then committed.

5\. Added tests in `BranchCoverageTest\_hotel\_booking.py` to reach more than 90% branch coverage, then committed.



\## Commands used
coverage run -m pytest <test\_file>

coverage report -m

coverage run --branch -m pytest <test\_file>

coverage report -m



\## Results



| Stage | Tests | Coverage of hotel\_booking.py |

|---|---|---|

| Before, line coverage (original test file) | 2 | 44% |

| Before, branch coverage (original test file) | 2 | 37% |

| After, line coverage | 13 | 97% (only line 39 missed) |

| After, branch coverage | 18 | 100% (22/22 branches) |



\## Screenshots



\### Before: line coverage

!\[Before line coverage](screenshots/before\_code\_coverage.png)



\### Before: branch coverage

!\[Before branch coverage](screenshots/before\_branch\_coverage.png)



\### After: line coverage

!\[After line coverage](screenshots/code\_coverage.png)



\### After: branch coverage

!\[After branch coverage](screenshots/branch\_coverage.png)



\## Line vs branch coverage



Line coverage only checks whether each line ran at least once. Branch coverage checks that every `if` and `else` outcome (True and False) was taken. Line coverage stopped at 97% because the final `return room` in `room\_upgrade` was never reached. Adding tests for non-members and suite members closed that gap and gave 100% branch coverage.



