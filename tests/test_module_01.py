from exercises.module_01 import token_names, format_tokens, accent_tokens

def test_token_names_are_sorted():
    assert token_names({"z": "1", "a": "2"}) == ["a", "z"]

def test_format_tokens():
    assert format_tokens({"beta": "2", "alpha": "1"}) == ["alpha=1", "beta=2"]

def test_accent_tokens():
    tokens = {"accent_primary": "#123456", "surface_00": "#000000"}
    assert accent_tokens(tokens) == {"accent_primary": "#123456"}
