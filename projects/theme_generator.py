# Program that creates generated files foot.ini, tokens.lua and theme.toml

from exercises import module_02, module_03
import json, argparse, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

OUT_FOOT = ROOT / "generated" / "foot.ini"
OUT_TOKENS = ROOT / "generated" / "tokens.lua"
OUT_THEME = ROOT / "generated" / "theme.toml"

def render_foot(tokens):
    lines = [
        "Generated file: do not edit by hand",
        "",
        "[colors]",
    ]

    for name in sorted(tokens):
        lines.append(f"{name}={tokens[name]}")

    return "\n".join(lines) + "\n"

def render_tokens(tokens):
    

def render_theme(tokens):


def write_file(path, content):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")

def main():
    raw_tokens = ROOT / "data" / "tokens.json"
    tokens = module_03.load_tokens(raw_tokens) 
    invalid = module_02.validate_tokens(tokens)
    
    if invalid:
        print(f"Invalid tokens: {invalid}")
        sys.exit(1)
    
    foot_content = render_foot(tokens)
    write_file(OUT_FOOT, foot_content)

    print(f"Generated {OUT_FOOT}")
    sys.exit(0)

if __name__ == "__main__":
    raise SystemExit(main())
