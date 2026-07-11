from pathlib import Path
import json
from exercises.module_03 import load_tokens, generate_env, write_env

def test_load_tokens(tmp_path: Path):
    path = tmp_path / "tokens.json"
    path.write_text(json.dumps({"accent": "#123456"}), encoding="utf-8")
    assert load_tokens(path) == {"accent": "#123456"}

def test_generate_env():
    assert generate_env({"beta": "2", "alpha": "1"}) == "alpha=1\nbeta=2\n"

def test_write_env(tmp_path: Path):
    output = tmp_path / "generated" / "tokens.env"
    write_env({"accent": "#123456"}, output)
    assert output.read_text(encoding="utf-8") == "accent=#123456\n"
