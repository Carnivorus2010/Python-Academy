"""Module 1 exercises."""

TOKENS = {
    "surface_00": "#000000",
    "surface_01": "#101412",
    "text_primary": "#d5ddd8",
    "accent_primary": "#7fa88a",
}

def token_names(tokens: dict[str, str]) -> list[str]:
    """Return token names sorted alphabetically."""
    return sorted(tokens.keys())

def format_tokens(tokens: dict[str, str]) -> list[str]:
    """Return sorted strings in the form NAME=VALUE."""
    formatted = []

    for name in token_names(tokens):
        formatted.append(f"{name}={tokens[name]}")

    return formatted

def accent_tokens(tokens: dict[str, str]) -> dict[str, str]:
    """Return only tokens whose names begin with accent_."""
    accent_only = {}

    for name in token_names(tokens):
        if name.startswith("accent_"):
            accent_only.update({name: tokens[name]})

    return accent_only

if __name__ == "__main__":
    for line in format_tokens(TOKENS):
        print(line)
