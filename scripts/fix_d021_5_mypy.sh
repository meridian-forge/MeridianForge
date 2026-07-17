#!/bin/bash

set -e

echo "======================================"
echo "Fix D021.5 MyPy Type Issue"
echo "Acquisition Report"
echo "======================================"

FILE="updates/packages/D021.5/files/src/meridianforge/reports/acquisition_report.py"

if [ ! -f "$FILE" ]; then
    echo "ERROR: File not found:"
    echo "$FILE"
    exit 1
fi


echo "Applying type fix..."

python3 - <<'PY'
from pathlib import Path

path = Path(
    "updates/packages/D021.5/files/src/meridianforge/reports/acquisition_report.py"
)

text = path.read_text()


if "from meridianforge.models.results.acquisition_assessment import" not in text:
    text = text.replace(
        "from meridianforge.models.results.acquisition_result import (\n",
        "from meridianforge.models.results.acquisition_assessment import (\n"
        "    AcquisitionAssessment,\n"
        ")\n"
        "from meridianforge.models.results.acquisition_result import (\n"
    )


old = """        assessment = result.metadata.get(
            "assessment",
        )
"""

new = """        assessment = result.metadata.get(
            "assessment",
        )

        if not isinstance(
            assessment,
            AcquisitionAssessment,
        ):
            assessment = None
"""

if old not in text:
    raise SystemExit(
        "Expected code block not found. File may already be fixed."
    )

text = text.replace(old, new)

path.write_text(text)

PY


echo
echo "Formatting..."

black updates/packages/D021.5/files/src/meridianforge/reports/acquisition_report.py


echo
echo "Fix applied successfully."

echo
echo "Next step:"
echo "./scripts/apply_update.sh D021.5"

