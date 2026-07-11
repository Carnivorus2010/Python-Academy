"""Module 1 exercises."""

TOKENS = {
    "surface_00": "#000000",
    "surface_01": "#101412",
    "text_primary": "#d5ddd8",
    "accent_primary": "#7fa88a",
}

def token_names(tokens: dict[str, str]) -> list[str]:
    """Return token names sorted alphabetically."""
    raise NotImplementedError

def format_tokens(tokens: dict[str, str]) -> list[str]:
    """Return sorted strings in the form NAME=VALUE."""
    raise NotImplementedError

def accent_tokens(tokens: dict[str, str]) -> dict[str, str]:
    """Return only tokens whose names begin with accent_."""
    raise NotImplementedError

if __name__ == "__main__":
    for line in format_tokens(TOKENS):
        print(line)
