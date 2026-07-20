"""Module 2 exercises."""
import string

def is_hex_color(value: object) -> bool:
    """Return True only for strings formatted like #12abEF."""
    if type(value) != str or not value.startswith("#"):
        return False
    
    value = value[1:]

    if len(value) == 6 and all(char in string.hexdigits for char in value):
        return True 
    else:
        return False 

def validate_tokens(tokens: dict[str, str]) -> list[str]:
    """Return invalid token names, sorted alphabetically."""
    invalid = []

    for key in tokens:
        if not is_hex_color(tokens[key]):
            invalid.append(key)
    invalid = sorted(invalid)
    
    return invalid

def normalize_token_name(name: str) -> str:
    """Trim, lowercase, and replace spaces with underscores."""
    trimmed = name.strip()
    lowered = trimmed.lower()
    normalized = lowered.replace(" ", "_")
    return normalized
