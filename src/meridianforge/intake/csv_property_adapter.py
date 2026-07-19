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

                self._validate(row)

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

        missing = self.REQUIRED_FIELDS - set(row.keys())

        if missing:
            raise ValueError(f"Missing fields: {missing}")
