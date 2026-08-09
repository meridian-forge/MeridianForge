"""
Spreadsheet embedded image extractor.

Extracts visual assets embedded inside Excel workbooks.

MF-512.4.4
"""

from __future__ import annotations

from pathlib import Path

from openpyxl import load_workbook

from meridianforge.extraction.image_artifact import (
    ImageArtifact,
)


class SpreadsheetImageExtractor:
    """
    Extract embedded images from XLSX artifacts.
    """

    @classmethod
    def extract(
        cls,
        workbook_path: Path,
        output_directory: Path,
    ) -> list[ImageArtifact]:
        """
        Extract workbook images.
        """

        output_directory.mkdir(
            parents=True,
            exist_ok=True,
        )

        workbook = load_workbook(
            workbook_path,
            read_only=False,
        )

        artifacts: list[ImageArtifact] = []

        image_counter = 0

        for sheet in workbook.worksheets:

            for image in sheet._images:

                image_counter += 1

                extension = ".png"

                output_path = (
                    output_directory
                    / f"{workbook_path.stem}_image_{image_counter}{extension}"
                )

                output_path.write_bytes(image._data())

                artifacts.append(
                    ImageArtifact(
                        source_file=workbook_path,
                        sheet_name=sheet.title,
                        image_index=image_counter,
                        image_path=output_path,
                    )
                )

        return artifacts
