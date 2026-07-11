# Module 3 — Files and Paths

```python
from pathlib import Path
import json

path = Path("data") / "tokens.json"
tokens = json.loads(path.read_text(encoding="utf-8"))
```

Write generated output deterministically by sorting token names and ending the file with one newline.
