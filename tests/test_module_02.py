from exercises.module_02 import is_hex_color, validate_tokens, normalize_token_name

def test_valid_hex_colors():
    assert is_hex_color("#000000")
    assert is_hex_color("#12abEF")

def test_invalid_hex_colors():
    assert not is_hex_color("000000")
    assert not is_hex_color("#fff")
    assert not is_hex_color("#gg0000")
    assert not is_hex_color(123456)

def test_validate_tokens():
    tokens = {"good": "#abcdef", "bad_two": "green", "bad_one": "#123"}
    assert validate_tokens(tokens) == ["bad_one", "bad_two"]

def test_normalize_token_name():
    assert normalize_token_name("  Accent Primary  ") == "accent_primary"
