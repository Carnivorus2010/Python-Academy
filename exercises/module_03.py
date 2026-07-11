"""Module 3 exercises."""

from pathlib import Path
import json

def load_tokens(path: Path) -> dict[str, str]:
    """Load and return a JSON object."""
    raise NotImplementedError

def generate_env(tokens: dict[str, str]) -> str:
    """Return sorted NAME=VALUE lines ending in one newline."""
    raise NotImplementedError

def write_env(tokens: dict[str, str], output_path: Path) -> None:
    """Create parent directories and write output."""
    raise NotImplementedError
