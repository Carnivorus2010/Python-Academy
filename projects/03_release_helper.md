# Project 3 — Release Helper

Build a safe Git release assistant.

Requirements:
- verify the working tree is clean
- read the current branch
- accept a version such as `0.2.0`
- support `--dry-run`
- never push unless `--push` is explicitly supplied
- use `subprocess.run(..., check=True)`
