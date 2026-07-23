"""Module 3 exercises."""

from pathlib import Path
import json

def load_tokens(path: Path) -> dict[str, str]:
    """Load and return a JSON object."""
    with open(path, "r", encoding="utf-8") as f:
        tokens = json.load(f)

    return tokens 

def generate_env(tokens: dict[str, str]) -> str:
    """Return sorted NAME=VALUE lines ending in one newline."""
    tokens_list = []

    for key in tokens:
        token_str = f"{key}={tokens[key]}\n"
        tokens_list.append(token_str)

    sorted_tokens = sorted(tokens_list)
    sorted_str = "".join(sorted_tokens)

    return sorted_str

def write_env(tokens: dict[str, str], output_path: Path) -> None:
    """Create parent directories and write output."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    gen_str = generate_env(tokens)
    
    with output_path.open("w", encoding="utf-8") as f:
        f.write(gen_str) 
