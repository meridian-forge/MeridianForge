#!/bin/bash

set -e

echo "Fixing Financing loan_term_years type conversion..."

python - <<'PYTHON'
from pathlib import Path

path = Path(
    "src/meridianforge/normalization/real_estate_adapter.py"
)

text = path.read_text()

old = """            loan_term_years=int(
                data.get(
                    "loan_term_years",
                    30,
                )
            ),
"""

new = """            loan_term_years=int(
                RealEstateAdapter._to_float(
                    data.get(
                        "loan_term_years",
                        30,
                    )
                )
            ),
"""

if old not in text:
    raise SystemExit(
        "Expected code block not found. No changes made."
    )

text = text.replace(old, new)

path.write_text(text)

print(
    "Loan term conversion fixed."
)
PYTHON

echo "B002.3.5 financing type fix complete."
