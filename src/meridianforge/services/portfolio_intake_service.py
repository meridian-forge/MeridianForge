from __future__ import annotations

import csv
from pathlib import Path

from openpyxl import load_workbook

from meridianforge.intake.extracted_data import ExtractedData
from meridianforge.opportunity.normalizer import normalize
from meridianforge.portfolio.models import (
    PortfolioIngestionResult,
    PortfolioOpportunity,
    QuarantinedRecord,
)


class PortfolioIntakeService:
    """
    Load a workbook or CSV containing many investment opportunities.

    Each row becomes an independent normalized opportunity.
    Invalid rows are quarantined without stopping the batch.
    """

    def ingest(
        self,
        file_path: Path,
    ) -> PortfolioIngestionResult:

        suffix = file_path.suffix.lower()

        if suffix == ".xlsx":
            return self._ingest_xlsx(file_path)

        if suffix == ".csv":
            return self._ingest_csv(file_path)

        raise ValueError(f"Unsupported portfolio file: {file_path.suffix}")

    def _ingest_xlsx(
        self,
        file_path: Path,
    ) -> PortfolioIngestionResult:

        workbook = load_workbook(
            file_path,
            data_only=True,
        )

        sheet = workbook.active

        rows = list(sheet.values)

        result = PortfolioIngestionResult()

        if not rows:
            return result

        headers = [str(value).strip() if value is not None else "" for value in rows[0]]

        for row_number, row in enumerate(
            rows[1:],
            start=2,
        ):

            record = {
                header: value
                for header, value in zip(
                    headers,
                    row,
                    strict=False,
                )
            }

            self._process_record(
                result,
                file_path,
                row_number,
                record,
            )

        return result

    def _ingest_csv(
        self,
        file_path: Path,
    ) -> PortfolioIngestionResult:

        result = PortfolioIngestionResult()

        with file_path.open(
            "r",
            encoding="utf-8-sig",
            newline="",
        ) as handle:

            reader = csv.DictReader(handle)

            for row_number, record in enumerate(
                reader,
                start=2,
            ):

                normalized_record = {
                    str(key): value for key, value in record.items() if key is not None
                }

                self._process_record(
                    result,
                    file_path,
                    row_number,
                    normalized_record,
                )

        return result

    def _process_record(
        self,
        result: PortfolioIngestionResult,
        file_path: Path,
        row_number: int,
        record: dict[str, object],
    ) -> None:

        try:

            extracted = ExtractedData(
                source_file=file_path.name,
                fields=record,
            )

            opportunity = normalize(extracted)

            result.opportunities.append(
                PortfolioOpportunity(
                    source_file=file_path,
                    row_number=row_number,
                    opportunity=opportunity,
                )
            )

        except Exception as exc:

            result.quarantined.append(
                QuarantinedRecord(
                    source_file=file_path,
                    row_number=row_number,
                    reason=str(exc),
                    raw_record=record,
                )
            )
