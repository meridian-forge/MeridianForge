#!/bin/bash

set -e

PACKAGE="updates/packages/MF-105.0"

echo "======================================"
echo "BUILD MF-105.0 DATA ACQUISITION LAYER"
echo "======================================"

rm -rf "$PACKAGE"

mkdir -p \
"$PACKAGE/files/src/meridianforge/data" \
"$PACKAGE/files/tests/data"


cat > "$PACKAGE/manifest.txt" <<'EOF'
MF-105.0
Data Acquisition Layer

Adds:
- Property data loader
- Data normalization
- Validation engine
- Import pipeline
EOF


cat > "$PACKAGE/release_notes.md" <<'EOF'
# MF-105.0 Data Acquisition Layer

Introduces external property data ingestion.

Supports:
- CSV-style imports
- Field normalization
- Validation
- Opportunity creation foundation
EOF


cat > "$PACKAGE/files/src/meridianforge/data/__init__.py" <<'PY'
PY


cat > "$PACKAGE/files/src/meridianforge/data/loader.py" <<'PY'
from typing import Any


class PropertyLoader:

    def load(
        self,
        records: list[dict[str, Any]],
    ) -> list[dict[str, Any]]:

        return records
PY


cat > "$PACKAGE/files/src/meridianforge/data/normalizer.py" <<'PY'
from typing import Any


class PropertyNormalizer:

    def normalize(
        self,
        record: dict[str, Any],
    ) -> dict[str, Any]:

        return {
            "address": record.get("address"),
            "purchase_price": float(
                record.get(
                    "price",
                    0,
                )
            ),
            "rent": float(
                record.get(
                    "rent",
                    0,
                )
            ),
        }
PY


cat > "$PACKAGE/files/src/meridianforge/data/validator.py" <<'PY'
from typing import Any


class PropertyValidator:

    REQUIRED_FIELDS = [
        "address",
        "purchase_price",
    ]

    def validate(
        self,
        record: dict[str, Any],
    ) -> bool:

        for field in self.REQUIRED_FIELDS:

            if not record.get(field):
                return False

        return True
PY


cat > "$PACKAGE/files/src/meridianforge/data/import_pipeline.py" <<'PY'
from typing import Any

from meridianforge.data.loader import (
    PropertyLoader,
)

from meridianforge.data.normalizer import (
    PropertyNormalizer,
)

from meridianforge.data.validator import (
    PropertyValidator,
)


class ImportPipeline:

    def __init__(self) -> None:

        self.loader = PropertyLoader()
        self.normalizer = PropertyNormalizer()
        self.validator = PropertyValidator()

    def run(
        self,
        records: list[dict[str, Any]],
    ) -> list[dict[str, Any]]:

        output = []

        for record in self.loader.load(records):

            normalized = self.normalizer.normalize(
                record
            )

            if self.validator.validate(
                normalized
            ):
                output.append(
                    normalized
                )

        return output
PY


cat > "$PACKAGE/files/tests/data/test_pipeline.py" <<'PY'
from meridianforge.data.import_pipeline import (
    ImportPipeline,
)


def test_import_pipeline():

    result = ImportPipeline().run(
        [
            {
                "address": "123 Main",
                "price": "250000",
                "rent": "2200",
            }
        ]
    )

    assert len(result) == 1
    assert result[0]["purchase_price"] == 250000
PY


echo
echo "MF-105.0 PACKAGE CREATED"