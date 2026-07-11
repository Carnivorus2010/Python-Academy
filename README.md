# deepBlack Python Academy

A project-first Python refresher built around Linux automation and the deepBlack desktop project.

## Setup

```bash
sudo pacman -S python python-pip git
cd deepblack_python_academy
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip pytest
pytest -q
```

## Course map

1. Python refresh: values, strings, lists, dictionaries
2. Control flow and functions
3. Files, paths, and configuration
4. Errors, logging, and command-line arguments
5. Linux automation with `subprocess`
6. Testing and refactoring
7. Capstone: token-driven theme generator
8. Capstone: deepBlack release helper

Work in short sessions, type the code yourself, run it often, and read every traceback.
