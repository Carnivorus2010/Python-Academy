from module_02.config_parser import (
    meaningful_lines,
    parse_setting,
    parse_config,
    load_config
)

import pytest

def test_meaningful_lines_strips_and_filters():
    lines = [
        "",
        "   ",
        "# terminal settings",
        "  # another comment",
        " font = JetBrains Mono ",
        "opacity = 0.90",
        " accent = #7fa88a",
    ]

    assert meaningful_lines(lines) == [
        "font = JetBrains Mono",
        "opacity = 0.90",
        "accent = #7fa88a",
    ]

def test_parse_setting_returns_clean_key_and_value():
    assert parse_setting("font = JetBrains Mono") == (
        "font",
        "JetBrains Mono",
    )

def test_parse_setting_preserves_equals_inside_value():
    assert parse_setting("command = echo name=value") == (
        "command",
        "echo name=value",
        )

def test_parse_setting_rejects_missing_equals():
    with pytest.raises(ValueError):
        parse_setting("font JetBrains Mono")

def test_parse_config_builds_dictionary():
    lines = [
        "# terminal settings",
        "",
        "font = JetBrains Mono",
        "opacity = 0.90",
        "command = echo name=value",
    ]

    assert parse_config(lines) == {
        "font": "JetBrains Mono",
        "opacity": "0.90",
        "command": "echo name=value",
    }

def test_parse_config_rejects_duplicate_keys():
    lines = [
        "font = JetBrains Mono",
        "opacity = 0.90",
        "font = Iosevka",
    ]

    with pytest.raises(ValueError):
        parse_config(lines)

def test_parse_setting_rejects_empty_key():
    with pytest.raises(ValueError):
        parse_setting(" = JetBrains Mono")

def test_parse_setting_rejects_empty_value():
    with pytest.raises(ValueError):
        parse_setting("font =   ")

def test_load_config_reads_and_parses_file(tmp_path):
    config_path = tmp_path / "terminal.conf"

    config_path.write_text(
            "# terminal settings\n"
            "\n"
            "font = JetBrains Mono\n"
            "opacity = 0.90\n"
            "command = echo name=value\n",
            encoding="utf-8",
    )

    assert load_config(config_path) == {
            "font": "JetBrains Mono",
            "opacity": "0.90",
            "command": "echo name=value",
    }
