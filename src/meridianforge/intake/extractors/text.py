"""
Text artifact extractor.

SP-411.2

Extracts plain text and rich text exports
into MeridianForge ExtractedData.
"""

from pathlib import Path

from meridianforge.intake.extracted_data import ExtractedData
from meridianforge.intake.extractors.base import Extractor


class TextExtractor(Extractor):
    """
    Extracts text-based artifacts.
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
            fields={
                "content": content,
            },
        )
