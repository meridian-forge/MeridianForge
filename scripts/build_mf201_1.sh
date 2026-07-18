#!/bin/bash

set -e

PACKAGE="updates/packages/MF-201.1"

echo "======================================"
echo "BUILD MF-201.1 EXTRACTION ENGINE FOUNDATION"
echo "======================================"

rm -rf "$PACKAGE"

mkdir -p \
"$PACKAGE/files/src/meridianforge/intake/extractors" \
"$PACKAGE/files/tests/intake"


cat > "$PACKAGE/manifest.txt" <<'EOF'
MF-201.1

Extraction Engine Foundation

Adds:
- Extracted data model
- Extractor abstraction
- Excel extractor
- Extractor registry
- Extraction tests
EOF


cat > "$PACKAGE/release_notes.md" <<'EOF'
# MF-201.1

Introduces the first extraction layer.

Purpose:

Convert source files into structured extracted fields.
EOF


cat > "$PACKAGE/files/src/meridianforge/intake/extracted_data.py" <<'EOF'
from dataclasses import dataclass, field


@dataclass
class ExtractedData:
    source_file: str
    fields: dict[str, str] = field(default_factory=dict)
EOF


cat > "$PACKAGE/files/src/meridianforge/intake/extractors/base.py" <<'EOF'
from abc import ABC, abstractmethod
from pathlib import Path

from meridianforge.intake.extracted_data import ExtractedData


class Extractor(ABC):

    @abstractmethod
    def extract(self, file_path: Path) -> ExtractedData:
        pass
EOF


cat > "$PACKAGE/files/src/meridianforge/intake/extractors/excel.py" <<'EOF'
from pathlib import Path

from openpyxl import load_workbook

from meridianforge.intake.extracted_data import ExtractedData
from meridianforge.intake.extractors.base import Extractor


class ExcelExtractor(Extractor):

    def extract(self, file_path: Path) -> ExtractedData:

        workbook = load_workbook(
            file_path,
            data_only=True,
        )

        fields: dict[str, str] = {}

        for sheet in workbook.worksheets:
            for row in sheet.iter_rows(values_only=True):
                values = [
                    str(value)
                    for value in row
                    if value is not None
                ]

                if len(values) >= 2:
                    fields[values[0]] = values[1]

        return ExtractedData(
            source_file=file_path.name,
            fields=fields,
        )
EOF


cat > "$PACKAGE/files/src/meridianforge/intake/extractors/registry.py" <<'EOF'
from pathlib import Path

from meridianforge.intake.extractors.base import Extractor
from meridianforge.intake.extractors.excel import ExcelExtractor


def get_extractor(file_path: Path) -> Extractor:

    extension = file_path.suffix.lower()

    if extension in {".xlsx", ".xls"}:
        return ExcelExtractor()

    raise ValueError(
        f"No extractor available for {extension}"
    )
EOF


cat > "$PACKAGE/files/tests/intake/test_excel_extractor.py" <<'EOF'
from pathlib import Path

from openpyxl import Workbook

from meridianforge.intake.extractors.excel import ExcelExtractor


def test_excel_extraction(tmp_path: Path) -> None:

    file_path = tmp_path / "property.xlsx"

    workbook = Workbook()
    sheet = workbook.active

    sheet.append(
        [
            "Purchase Price",
            "250000",
        ]
    )

    workbook.save(file_path)

    result = ExcelExtractor().extract(file_path)

    assert result.fields["Purchase Price"] == "250000"
EOF


echo
echo "MF-201.1 PACKAGE CREATED"