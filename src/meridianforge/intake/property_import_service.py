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
        self.csv_adapter = CSVPropertyAdapter()

    def import_file(
        self,
        file_path: Path,
    ) -> list[dict[str, Any]]:
        """
        Import CSV or Excel property files.
        """

        suffix = file_path.suffix.lower()

        if suffix == ".csv":
            return self.csv_adapter.load(
                file_path,
            )

        if suffix in {".xlsx", ".xls"}:
            return self._load_excel(
                file_path,
            )

        raise ValueError(
            f"Unsupported file type: {suffix}"
        )

    def import_csv(
        self,
        file_path: Path,
    ) -> list[dict[str, Any]]:
        """
        Backward compatible CSV import.
        """

        return self.csv_adapter.load(
            file_path,
        )

    def _load_excel(
        self,
        file_path: Path,
    ) -> list[dict[str, Any]]:
        """
        Load Excel property files.
        """

        from openpyxl import load_workbook

        workbook = load_workbook(
            file_path,
            data_only=True,
        )

        sheet = workbook.active

        rows = list(
            sheet.values,
        )

        headers = [
            str(value).strip()
            for value in rows[0]
        ]

        opportunities: list[dict[str, Any]] = []

        for row in rows[1:]:

            data = dict(
                zip(
                    headers,
                    row,
                )
            )

            opportunities.append(
                {
                    "name": data.get("name")
                    or data.get("address"),
                    "price": float(
                        data.get("price")
                        or data.get("purchase_price")
                    ),
                    "rent": float(
                        data.get("rent")
                        or data.get("monthly_rent")
                    ),
                }
            )

        return opportunities
