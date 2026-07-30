from __future__ import annotations

import csv
from pathlib import Path

from meridianforge.intake.extracted_data import ExtractedData
from meridianforge.intake.extractors.base import Extractor


class CsvExtractor(Extractor):
    """
    CSV extractor.

    Supports standard broker exports where the first row contains headers.
    Returns the first data row as a normalized field dictionary.
    """

    def extract(self, file_path: Path) -> ExtractedData:
        with file_path.open("r", encoding="utf-8-sig", newline="") as handle:
            reader = csv.DictReader(handle)
            first_row = next(reader, None)

        fields: dict[str, object] = {}

        if first_row:
            for key, value in first_row.items():
                if key is None:
                    continue
                fields[str(key).strip()] = value

        return ExtractedData(
            source_file=file_path.name,
            fields=fields,
        )
