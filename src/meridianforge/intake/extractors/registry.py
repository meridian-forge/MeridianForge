"""
Extractor registry.

SP-411.2

Routes incoming artifact formats
to generic extractors.
"""

from pathlib import Path

from meridianforge.intake.extractors.base import Extractor
from meridianforge.intake.extractors.document import (
    DocumentExtractor,
)
from meridianforge.intake.extractors.excel import (
    ExcelExtractor,
)
from meridianforge.intake.extractors.pdf import (
    PDFExtractor,
)
from meridianforge.intake.extractors.text import (
    TextExtractor,
)


def get_extractor(
    file_path: Path,
) -> Extractor:
    """
    Return extractor for artifact type.
    """

    extension = file_path.suffix.lower()

    registry: dict[str, type[Extractor]] = {
        ".xlsx": ExcelExtractor,
        ".xls": ExcelExtractor,
        ".pdf": PDFExtractor,
        ".docx": DocumentExtractor,
        ".txt": TextExtractor,
        ".rtf": TextExtractor,
    }

    extractor = registry.get(extension)

    if extractor is None:
        raise ValueError(
            f"No extractor registered for '{extension}'."
        )

    return extractor()
