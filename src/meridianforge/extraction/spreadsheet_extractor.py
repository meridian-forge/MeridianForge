"""
Universal spreadsheet extractor.

Discovers tabular data from arbitrary Excel workbooks.

No provider-specific assumptions.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

from openpyxl import load_workbook

from meridianforge.extraction.models import ExtractedArtifact


class SpreadsheetExtractor:
    """
    Generic Excel artifact extractor.
    """

    HEADER_SCAN_LIMIT = 25

    @classmethod
    def extract(
        cls,
        workbook_path: Path,
    ) -> ExtractedArtifact:

        workbook = load_workbook(
            workbook_path,
            read_only=True,
            data_only=True,
        )

        records: list[dict[str, Any]] = []

        for sheet in workbook.worksheets:

            rows = list(sheet.values)

            if not rows:
                continue

            header_index = cls._find_header_row(rows)

            if header_index is None:
                continue

            headers = [
                str(value).strip()
                if value is not None
                else ""
                for value in rows[header_index]
            ]

            for row in rows[header_index + 1:]:

                record = {
                    header: value
                    for header, value in zip(
                        headers,
                        row,
                    )
                    if header
                }

                if any(
                    value is not None
                    for value in record.values()
                ):
                    records.append(record)

        return ExtractedArtifact(
            source_file=workbook_path,
            artifact_type="xlsx",
            records=records,
        )

    @staticmethod
    def _find_header_row(
        rows: list[tuple[Any, ...]],
    ) -> int | None:
        """
        Detect likely table header row.
        """

        for index, row in enumerate(
            rows[: SpreadsheetExtractor.HEADER_SCAN_LIMIT]
        ):

            values = [
                str(value).strip().lower()
                for value in row
                if value is not None
            ]

            if len(values) < 3:
                continue

            keywords = {
                "price",
                "purchase price",
                "roi",
                "cash flow",
                "address",
                "state",
                "rent",
            }

            matches = sum(
                1
                for value in values
                if value in keywords
            )

            if matches >= 2:
                return index

        return None
