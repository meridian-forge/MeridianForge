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
        self.adapter = CSVPropertyAdapter()

    def import_csv(
        self,
        file_path: Path,
    ) -> list[dict[str, Any]]:

        return self.adapter.load(file_path)
