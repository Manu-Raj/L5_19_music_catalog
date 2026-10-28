# Reflection

Name: Maniish Rajendran | SRN: PES2UG24CS265

**1. Which issues were the easiest and which were the hardest to fix?**
The style issues (snake_case names, docstrings, line length, the one-line `if`) were the easiest because the tools say exactly what to change. The hardest was removing `pickle`: it meant changing the storage format to JSON and making sure `save_playlist` and `load_playlist` still worked together. The SQL injection fix was also important, but it was a small change once I knew to use `?` placeholders.

**2. Did the tools report any false positives?**
Mostly no, but the Bandit B311 warning on `random.choice` is arguably a false positive here, because picking a random song for shuffle does not need cryptographic security. I switched to `secrets.choice` to clear the report. In a real project, I might keep `random` and add a `# nosec` comment with a reason.

**3. How would you integrate static analysis into your workflow?**
I would run Flake8, Pylint and Bandit as a pre-commit hook and again in a CI pipeline (for example GitHub Actions), so a pull request fails if Bandit finds a Medium/High issue or the Pylint score drops below a threshold such as 9.5. I would also run them in my editor while writing code.

**4. What tangible improvements did you see in code quality, readability and security?**
Pylint went from 4.57/10 to 10.00/10, Flake8 from 7 warnings to 0, and Bandit from 4 findings to none. Readability improved through consistent naming, docstrings and shorter lines. Security improved by removing the SQL injection and the unsafe pickle deserialization. Reliability improved by fixing the shared mutable default list, which was a real bug, and the bare `except`.
