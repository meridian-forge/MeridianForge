#!/bin/bash

set -e

echo "======================================"
echo "Meridian Forge MF-222.0"
echo "CSV Intake Monday Integration"
echo "======================================"

mkdir -p \
src/meridianforge/services \
src/meridianforge/workspace \
tests/services \
updates/packages/MF-222.0/files/src/meridianforge/services \
updates/packages/MF-222.0/files/src/meridianforge/workspace \
updates/packages/MF-222.0/files/tests/services

cat > src/meridianforge/services/monday_execution.py <<'PY'
from pathlib import Path
from typing import Any

from meridianforge.intake.property_import_service import (
    PropertyImportService,
)
from meridianforge.reporting.monday_dashboard import (
    MondayDashboardGenerator,
)


class MondayExecutionService:
    """
    Executes Monday analysis from imported properties.
    """

    def __init__(self) -> None:
        self.importer = PropertyImportService()
        self.dashboard = MondayDashboardGenerator()

    def execute(
        self,
        file_path: Path,
    ) -> str:

        opportunities: list[dict[str, Any]] = (
            self.importer.import_csv(
                file_path
            )
        )

        return self.dashboard.generate(
            opportunities
        )
PY


cat > tests/services/test_monday_execution.py <<'PY'
from pathlib import Path

from meridianforge.services.monday_execution import (
    MondayExecutionService,
)


def test_monday_execution(
    tmp_path: Path,
) -> None:

    file = tmp_path / "properties.csv"

    file.write_text(
        "name,price,rent\n"
        "Test Property,200000,1800\n",
        encoding="utf-8",
    )

    result = MondayExecutionService().execute(
        file
    )

    assert result is not None
PY


cp src/meridianforge/services/monday_execution.py \
updates/packages/MF-222.0/files/src/meridianforge/services/

cp tests/services/test_monday_execution.py \
updates/packages/MF-222.0/files/tests/services/


cat > updates/packages/MF-222.0/manifest.txt <<'TXT'
MF-222.0
CSV Intake Monday Integration
TXT


cat > updates/packages/MF-222.0/release_notes.md <<'MD'
# MF-222.0 CSV Intake Monday Integration

Connects CSV property imports to Monday analysis workflow.
MD


chmod +x scripts/build_mf222_0.sh

echo "MF-222.0 build complete"
