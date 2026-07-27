"""
Text artifact extractor.

SP-411.2
"""

from pathlib import Path

from meridianforge.intake.extracted_data import ExtractedData
from meridianforge.intake.extractors.base import Extractor
from meridianforge.intake.text_parser import parse_text_fields


class TextExtractor(Extractor):
    """
    Extracts plain text artifacts.
    """

    def extract(
        self,
        file_path: Path,
    ) -> ExtractedData:

        content = file_path.read_text(
            encoding="utf-8",
            errors="ignore",
        )

        return ExtractedData(
            source_file=file_path.name,
            fields=parse_text_fields(content),
        )
