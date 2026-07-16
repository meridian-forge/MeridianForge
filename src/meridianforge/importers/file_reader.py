"""
Unified file reader.

Supports multiple external file formats and
returns raw investment records.
"""

import csv
from pathlib import Path

from openpyxl import load_workbook


class FileReader:
    """
    Reads supported investment files.
    """

    @staticmethod
    def read(
        file_path: str,
    ) -> list[dict[str, object]]:

        path = Path(file_path)

        suffix = path.suffix.lower()

        if suffix == ".csv":
            return FileReader._read_csv(path)

        if suffix in {".xlsx", ".xlsm"}:
            return FileReader._read_excel(path)

        raise ValueError(f"Unsupported file format: {suffix}")

    @staticmethod
    def _read_csv(
        path: Path,
    ) -> list[dict[str, object]]:

        with path.open(
            newline="",
            encoding="utf-8",
        ) as file:

            reader = csv.DictReader(file)

            return [dict(row) for row in reader]

    @staticmethod
    def _read_excel(
        path: Path,
    ) -> list[dict[str, object]]:

        workbook = load_workbook(
            path,
            read_only=True,
            data_only=True,
        )

        sheet = workbook.active

        rows = list(sheet.values)

        if not rows:
            return []

        headers = rows[0]

        return [
            {str(headers[index]): value for index, value in enumerate(row)}
            for row in rows[1:]
        ]
