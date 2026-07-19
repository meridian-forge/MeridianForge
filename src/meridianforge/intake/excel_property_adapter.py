from pathlib import Path
from typing import Any

from openpyxl import load_workbook


class ExcelPropertyAdapter:
    """
    Adapter for importing property opportunities
    from Excel workbooks.
    """

    REQUIRED_FIELDS = {
        "name",
        "status",
        "score",
        "rent",
        "price",
    }

    def load(
        self,
        file_path: Path,
    ) -> list[dict[str, Any]]:
        """
        Load property records from Excel.
        """

        workbook = load_workbook(
            file_path,
            data_only=True,
        )

        sheet = workbook.active

        rows = list(sheet.values)

        if not rows:
            return []

        headers = [str(value).strip() for value in rows[0]]

        records: list[dict[str, Any]] = []

        for row in rows[1:]:

            record = dict(
                zip(
                    headers,
                    row,
                    strict=True,
                )
            )

            records.append(record)

        self._validate(records)

        return records

    def _validate(
        self,
        records: list[dict[str, Any]],
    ) -> None:

        for record in records:

            missing = self.REQUIRED_FIELDS - set(record.keys())

            if missing:
                raise ValueError(f"Missing fields: {missing}")
