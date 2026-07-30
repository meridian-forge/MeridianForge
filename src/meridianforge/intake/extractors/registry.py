from __future__ import annotations

from pathlib import Path

from meridianforge.intake.extractors.base import Extractor
from meridianforge.intake.extractors.csv import CsvExtractor
from meridianforge.intake.extractors.document import DocumentExtractor
from meridianforge.intake.extractors.excel import ExcelExtractor
from meridianforge.intake.extractors.pdf import PDFExtractor
from meridianforge.intake.extractors.text import TextExtractor

_EXTRACTORS: dict[str, Extractor] = {
    ".xlsx": ExcelExtractor(),
    ".xlsm": ExcelExtractor(),
    ".xls": ExcelExtractor(),
    ".csv": CsvExtractor(),
    ".pdf": PDFExtractor(),
    ".docx": DocumentExtractor(),
    ".txt": TextExtractor(),
}


def get_extractor(file_path: Path) -> Extractor:
    extension = file_path.suffix.lower()

    extractor = _EXTRACTORS.get(extension)

    if extractor is None:
        raise ValueError(f"No extractor registered for '{extension}'.")

    return extractor
