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
