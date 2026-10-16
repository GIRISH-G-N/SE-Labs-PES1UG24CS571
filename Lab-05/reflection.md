\# Lab 5 — Reflection on Static Code Analysis



\## 1. What is the purpose of static code analysis?



Static code analysis examines source code without executing it. It helps identify potential bugs, security vulnerabilities, code quality problems, and style violations early in development. In this lab, I used Pylint, Bandit, and Flake8 to analyze the radio scheduling program.



\## 2. What issues did you identify and fix?



I addressed SQL injection risk by using parameterized SQL queries and replaced unrestricted `eval()` with a restricted AST-based evaluator. I removed the hardcoded studio password, improved function naming, added docstrings, corrected formatting violations, and removed unnecessary global state.



\## 3. How did Pylint, Bandit, and Flake8 help improve the program?



Pylint helped identify code quality and maintainability problems. Bandit detected security risks, including unsafe expression evaluation, SQL query construction, and a hardcoded password. Flake8 identified formatting problems such as overly long lines and multiple statements on one line. Using all three tools provided complementary checks.



\## 4. What did you learn about static code analysis?



I learned that code can run successfully and still contain security, maintainability, and style problems. Static analysis helps identify these problems before they cause issues in production. After making the changes, Pylint improved from 2.41/10 to 10.00/10, Bandit reported no remaining issues, and Flake8 returned no violations.

