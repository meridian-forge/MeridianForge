"""
Evidence normalization layer.

Converts extracted evidence fields from any source
(OCR, PDF, spreadsheet, API, etc.) into normalized
investment opportunity attributes.

MF-512.4.4
"""

from __future__ import annotations

from decimal import Decimal
from typing import Iterable

from meridianforge.extraction.evidence_field_extractor import (
    ExtractedField,
)


class EvidenceNormalizer:
    """
    Normalize extracted evidence into pipeline-ready fields.
    """

    @classmethod
    def normalize(
        cls,
        fields: Iterable[ExtractedField],
        source_file: str | None = None,
    ) -> dict[str, object]:
        """
        Convert evidence fields into normalized opportunity data.
        """

        result: dict[str, object] = {
            "source_method": "evidence",
            "source_file": source_file or "unknown",
        }

        confidence_values: list[float] = []

        for field in fields:
            result[field.name] = cls._convert_value(
                field.value,
            )

            confidence_values.append(
                field.confidence,
            )

        if confidence_values:
            result["confidence"] = round(
                sum(confidence_values) / len(confidence_values),
                3,
            )

        return result

    @staticmethod
    def _convert_value(
        value: Decimal,
    ) -> float:

        return float(value)
