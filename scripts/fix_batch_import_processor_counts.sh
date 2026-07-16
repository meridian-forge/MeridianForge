#!/bin/bash

set -e

echo "Fixing BatchImportProcessor counters..."

python3 - <<'PYTHON'
from pathlib import Path

path = Path(
    "src/meridianforge/services/batch_import_processor.py"
)

text = path.read_text()

text = text.replace(
"""            failed_records=result.records_failed,
            total_records=result.records_processed
            + result.records_failed,
""",
"""            failed_records=(
                len(records)
                -
                len(result.assets)
            ),
            total_records=len(records),
"""
)

text = text.replace(
"""            records_processed=len(result.assets),
            records_failed=result.records_failed,
""",
"""            records_processed=len(result.assets),
            records_failed=(
                len(records)
                -
                len(result.assets)
            ),
"""
)

path.write_text(text)

print("Batch processor counters fixed.")
PYTHON

black src/meridianforge/services/batch_import_processor.py

echo "Done."
