"""
Document artifact extractor.

SP-411.2

Handles DOCX style documents.
"""

from pathlib import Path

from meridianforge.intake.extracted_data import ExtractedData
from meridianforge.intake.extractors.base import Extractor
from meridianforge.intake.text_parser import parse_text_fields


class DocumentExtractor(Extractor):
    """
    Extracts text from DOCX documents.
    """

    def extract(
        self,
        file_path: Path,
    ) -> ExtractedData:

        from docx import Document

        document = Document(
            str(file_path),
        )

        content = "\n".join(paragraph.text for paragraph in document.paragraphs)

        return ExtractedData(
            source_file=file_path.name,
            fields=parse_text_fields(content),
        )
