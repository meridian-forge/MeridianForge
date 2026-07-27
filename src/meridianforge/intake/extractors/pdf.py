"""
PDF artifact extractor.

SP-411.2
"""

from pathlib import Path

from meridianforge.intake.extracted_data import ExtractedData
from meridianforge.intake.extractors.base import Extractor


class PDFExtractor(Extractor):
    """
    Extracts text from PDF artifacts.
    """

    def extract(
        self,
        file_path: Path,
    ) -> ExtractedData:

        try:
            from pypdf import PdfReader

            reader = PdfReader(
                str(file_path),
            )

            content = "\n".join(
                page.extract_text() or ""
                for page in reader.pages
            )

        except ImportError:
            content = ""

        return ExtractedData(
            source_file=file_path.name,
            fields={
                "content": content,
            },
        )
