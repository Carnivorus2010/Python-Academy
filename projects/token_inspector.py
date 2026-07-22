# Token Inspecting Program
# Stores, sorts and prints valid tokens

from exercises import module_01, module_02
from pathlib import Path
from collections import Counter
import json, sys

def next_token_name(tokens, category):
    count = 0

    for name in tokens:
        if name.startswith(f"{category}_"):
            count += 1

    return f"{category}_{count:02d}"

def main():
    repo_root = Path(__file__).resolve().parents[1]
    tokens_path = repo_root / "data" / "tokens.json"

    with tokens_path.open("r") as f:
        tokens = json.load(f)
    invalid = module_02.validate_tokens(tokens)

    if invalid:
        print(invalid)
        sys.exit(1)

    while len(tokens) < 6:
        more = "More tokens are needed"
        undered = ("\x1B[4m" + more + "\x1B[0m")
        added_token = input(
                f"{undered}\nWhich type of token would"
                " you like to add? [S]urface, [T]ext, or "
                "[A]ccent: "
        ).strip().upper()

        if added_token == "S":
            category = "surface"
        elif added_token == "T":
            category = "text"
        elif added_token == "A":
            category = "accent"
        else:
            error = "Error"
            format_err = ("\033[31m" + error + "\033[0m")
            print(f"{format_err}: please enter valid response ([S], [T], or [A])")
            continue

        new_name = next_token_name(tokens, category)
        new_color = input(f"Enter hex color for {new_name}: ").strip()    

        while not module_02.is_hex_color(new_color):
            error = "Error"
            format_err = ("\033[31m" + error + "\033[0m")
            new_color = input(f"{format_err}: Invalid hex color.\nPlease"
                               " re-enter valid color code: ")

        tokens[new_name] = new_color

    
    valid = module_01.format_tokens(tokens)

    header = "Tokens:"
    formatted_head = ("\n\033[36m\x1B[4m" + header + "\x1B[0m\033[0m")
    print(formatted_head)
    for token in valid:
        print(token)

    c = Counter()
    for token in tokens:
        if token.startswith("surface_"):
            c['s'] += 1
        elif token.startswith("text_"):
            c['t'] += 1
        elif token.startswith("accent_"):
            c['a'] += 1
    header = "Token Counts:"
    formatted_head = ("\n\033[36m\x1B[4m" + header + "\x1B[0m\033[0m")
    print(formatted_head)
    print(f"Surface - {c['s']}\nText - {c['t']}\nAccent - {c['a']}")

if __name__ == "__main__":
    main() 
