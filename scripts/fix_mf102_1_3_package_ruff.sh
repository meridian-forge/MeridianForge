#!/bin/bash

set -e

FILE="updates/packages/MF-102.1.3/files/src/meridianforge/intake/router.py"

echo "Fixing Ruff UP007..."

python3 <<PY
from pathlib import Path

path = Path("$FILE")

text = path.read_text()

text = text.replace(
    "from typing import Union\n\n",
    "",
)

text = text.replace(
"""AdapterType = Union[
    CSVAdapter,
    EmailAdapter,
    ManualAdapter,
    PDFAdapter,
    URLAdapter,
    XLSXAdapter,
]""",
"""AdapterType = (
    CSVAdapter
    | EmailAdapter
    | ManualAdapter
    | PDFAdapter
    | URLAdapter
    | XLSXAdapter
)"""
)

path.write_text(text)

print("UPDATED:", path)
PY

echo "MF-102.1.3 Ruff fix complete"