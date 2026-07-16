"""
Unified file reader.

Supports CSV and XLSX sources.
"""

import csv
from pathlib import Path

from openpyxl import load_workbook


class FileReader:
    """
    Reads supported investment data files.
    """

    @staticmethod
    def read(
        file_path: str,
    ) -> list[dict[str, object]]:
        """
        Read supported file formats.
        """

        path = Path(file_path)

        suffix = path.suffix.lower()

        if suffix == ".csv":
            return FileReader._read_csv(path)

        if suffix in (".xlsx", ".xlsm"):
            return FileReader._read_excel(path)

        raise ValueError(f"Unsupported file format: {suffix}")

    @staticmethod
    def _read_csv(
        path: Path,
    ) -> list[dict[str, object]]:
        """
        Read CSV file.
        """

        with path.open(
            mode="r",
            encoding="utf-8",
            newline="",
        ) as file:

            reader = csv.DictReader(file)

            return [dict(row) for row in reader]

    @staticmethod
    def _read_excel(
        path: Path,
    ) -> list[dict[str, object]]:
        """
        Read Excel worksheet.

        First row is treated as headers.
        """

        workbook = load_workbook(
            path,
            read_only=True,
            data_only=True,
        )

        worksheet = workbook.active

        rows = list(worksheet.values)

        if not rows:
            return []

        headers = [str(header) if header is not None else "" for header in rows[0]]

        records: list[dict[str, object]] = []

        for row in rows[1:]:

            record = {
                headers[index]: value
                for index, value in enumerate(row)
                if index < len(headers)
            }

            records.append(record)

        return records
