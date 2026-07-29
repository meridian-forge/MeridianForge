from pathlib import Path

from openpyxl import load_workbook

from meridianforge.intake.extracted_data import ExtractedData
from meridianforge.intake.extractors.base import Extractor


class ExcelExtractor(Extractor):
    """
    Excel extractor.

    Supports both:

    1. Tabular workbooks
       address | city | state | purchase_price | ...

    2. Legacy key/value workbooks
       Field | Value
    """

    def extract(self, file_path: Path) -> ExtractedData:
        workbook = load_workbook(
            file_path,
            data_only=True,
        )

        fields: dict[str, object] = {}

        for sheet in workbook.worksheets:
            rows = list(sheet.iter_rows(values_only=True))

            if not rows:
                continue

            # Detect tabular workbook:
            # first row contains headers and at least one data row exists.
            if len(rows) >= 2:
                headers = [str(value).strip() for value in rows[0] if value is not None]

                first_data_row = rows[1]

                if headers and len(first_data_row) >= len(headers):
                    for header, value in zip(
                        headers,
                        first_data_row,
                        strict=False,
                    ):
                        fields[header] = value

                    break

            # Fallback: legacy key/value workbook
            for row in rows:
                values = [value for value in row if value is not None]

                if len(values) >= 2:
                    fields[str(values[0]).strip()] = values[1]

        return ExtractedData(
            source_file=file_path.name,
            fields=fields,
        )
