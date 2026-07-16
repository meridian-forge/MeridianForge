#!/bin/bash

set -e

echo "Fixing batch confidence float precision test..."

python3 - <<'PYTHON'
from pathlib import Path

path = Path(
    "tests/test_batch_confidence.py"
)

text = path.read_text()

text = text.replace(
    "assert confidence == 0.85",
    "assert round(confidence, 2) == 0.85",
)

path.write_text(text)

print("Test precision fixed.")
PYTHON

black tests/test_batch_confidence.py

echo "Done."
