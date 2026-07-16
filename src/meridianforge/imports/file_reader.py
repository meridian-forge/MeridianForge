"""
Generic property file reader.

Reads external files without applying business interpretation.
"""

import csv
import json
from pathlib import Path

from meridianforge.models.results.import_result import (
    ImportResult,
)


class FileReader:
    """
    Reads structured property data files.
    """

    SUPPORTED_EXTENSIONS = {
        ".csv",
        ".json",
    }

    @staticmethod
    def read(
        file_path: str,
    ) -> ImportResult:
        """
        Read a supported file and return raw records.
        """

        path = Path(file_path)

        if path.suffix.lower() not in FileReader.SUPPORTED_EXTENSIONS:
            return ImportResult(
                rows_processed=0,
                rows_loaded=0,
                rows_failed=0,
                warnings=[f"Unsupported file type: {path.suffix}"],
            )

        if path.suffix.lower() == ".csv":
            return FileReader._read_csv(path)

        return FileReader._read_json(path)

    @staticmethod
    def _read_csv(
        path: Path,
    ) -> ImportResult:
        """
        Read CSV files.
        """

        records: list[dict[str, object]] = []

        with path.open(
            newline="",
            encoding="utf-8",
        ) as file:

            reader = csv.DictReader(file)

            for row in reader:
                records.append(
                    dict(row),
                )

        return ImportResult(
            rows_processed=len(records),
            rows_loaded=len(records),
            rows_failed=0,
            records=records,
        )

    @staticmethod
    def _read_json(
        path: Path,
    ) -> ImportResult:
        """
        Read JSON files.
        """

        with path.open(
            encoding="utf-8",
        ) as file:

            data = json.load(file)

        if isinstance(data, list):
            records = data
        else:
            records = [data]

        return ImportResult(
            rows_processed=len(records),
            rows_loaded=len(records),
            rows_failed=0,
            records=records,
        )
