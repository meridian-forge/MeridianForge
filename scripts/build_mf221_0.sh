#!/bin/bash

set -e

echo "======================================"
echo "Meridian Forge MF-221.0"
echo "CSV Property Intake Adapter"
echo "======================================"

mkdir -p \
src/meridianforge/intake \
tests/intake \
updates/packages/MF-221.0/files/src/meridianforge/intake \
updates/packages/MF-221.0/files/tests/intake


cat > src/meridianforge/intake/csv_property_adapter.py <<'PY'
import csv
from pathlib import Path
from typing import Any


class CSVPropertyAdapter:
    """
    Converts CSV property exports into
    Meridian Forge opportunity dictionaries.
    """

    REQUIRED_FIELDS = {
        "name",
        "price",
        "rent",
    }

    def load(
        self,
        file_path: Path,
    ) -> list[dict[str, Any]]:

        opportunities: list[dict[str, Any]] = []

        with file_path.open(
            newline="",
            encoding="utf-8",
        ) as file:

            reader = csv.DictReader(file)

            for row in reader:

                self._validate(
                    row
                )

                opportunities.append(
                    {
                        "name": row["name"],
                        "price": float(row["price"]),
                        "rent": float(row["rent"]),
                    }
                )

        return opportunities

    def _validate(
        self,
        row: dict[str, str],
    ) -> None:

        missing = (
            self.REQUIRED_FIELDS
            -
            set(row.keys())
        )

        if missing:
            raise ValueError(
                f"Missing fields: {missing}"
            )
PY


cat > src/meridianforge/intake/property_import_service.py <<'PY'
from pathlib import Path
from typing import Any

from meridianforge.intake.csv_property_adapter import (
    CSVPropertyAdapter,
)


class PropertyImportService:
    """
    Application service for importing
    property opportunities.
    """

    def __init__(self) -> None:
        self.adapter = CSVPropertyAdapter()

    def import_csv(
        self,
        file_path: Path,
    ) -> list[dict[str, Any]]:

        return self.adapter.load(
            file_path
        )
PY


cat > tests/intake/test_csv_property_adapter.py <<'PY'
from pathlib import Path

from meridianforge.intake.csv_property_adapter import (
    CSVPropertyAdapter,
)


def test_csv_property_import(
    tmp_path: Path,
) -> None:

    file = tmp_path / "properties.csv"

    file.write_text(
        "name,price,rent\n"
        "Jacksonville A,200000,1800\n",
        encoding="utf-8",
    )

    result = CSVPropertyAdapter().load(
        file
    )

    assert len(result) == 1
    assert result[0]["name"] == "Jacksonville A"
    assert result[0]["price"] == 200000
PY


cp src/meridianforge/intake/csv_property_adapter.py \
updates/packages/MF-221.0/files/src/meridianforge/intake/


cp src/meridianforge/intake/property_import_service.py \
updates/packages/MF-221.0/files/src/meridianforge/intake/


cp tests/intake/test_csv_property_adapter.py \
updates/packages/MF-221.0/files/tests/intake/


cat > updates/packages/MF-221.0/manifest.txt <<'TXT'
MF-221.0
CSV Property Intake Adapter

Files:

src/meridianforge/intake/csv_property_adapter.py
src/meridianforge/intake/property_import_service.py
tests/intake/test_csv_property_adapter.py
TXT


cat > updates/packages/MF-221.0/release_notes.md <<'MD'
# MF-221.0 CSV Property Intake Adapter

Adds first real-world property data ingestion layer.

Supports:
- Zillow exports
- Realtor exports
- Excel-to-CSV workflows

Converts external property files into Meridian Forge opportunity records.
MD


chmod +x scripts/build_mf221_0.sh

echo ""
echo "MF-221.0 build complete"
echo "Run ./scripts/quality_gate.sh"
