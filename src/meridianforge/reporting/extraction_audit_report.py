"""
Extraction audit reporting.

MF-513.3.2

Exports extraction audit records into a structured report that can be
reviewed after a Monday execution cycle. This provides the human
feedback loop that will later feed the learning engine.
"""

from __future__ import annotations

import json
from pathlib import Path

from meridianforge.models.domain.extraction_audit import (
    ExtractionAuditRecord,
    ExtractionAuditStatus,
)


class ExtractionAuditReport:
    """
    Build and export extraction audit review reports.
    """

    @staticmethod
    def summary(
        records: list[ExtractionAuditRecord],
    ) -> dict[str, object]:
        total = len(records)

        accepted = [
            record
            for record in records
            if record.status is ExtractionAuditStatus.ACCEPTED
        ]

        review = [
            record
            for record in records
            if record.status is ExtractionAuditStatus.REVIEW
        ]

        rejected = [
            record
            for record in records
            if record.status is ExtractionAuditStatus.REJECTED
        ]

        average_confidence = (
            sum(record.confidence for record in records) / total
            if total
            else 0.0
        )

        return {
            "total_fields": total,
            "accepted": len(accepted),
            "review": len(review),
            "rejected": len(rejected),
            "average_confidence": round(
                average_confidence,
                4,
            ),
        }

    @classmethod
    def export_json(
        cls,
        records: list[ExtractionAuditRecord],
        output_path: Path,
    ) -> Path:
        payload = {
            "summary": cls.summary(records),
            "records": [
                {
                    "artifact_id": record.artifact_id,
                    "source_file": record.source_file,
                    "field_name": record.field_name,
                    "raw_value": record.raw_value,
                    "normalized_value": record.normalized_value,
                    "confidence": record.confidence,
                    "extractor": record.extractor,
                    "status": record.status.value,
                }
                for record in records
            ],
        }

        output_path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        output_path.write_text(
            json.dumps(payload, indent=2),
        )

        return output_path
