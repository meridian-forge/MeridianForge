"""
Evidence consolidation layer.

Combines raw extracted evidence and recognized
financial fields into a canonical evidence object.

Provider agnostic.

MF-512.4.3-D
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from meridianforge.extraction.evidence_field_extractor import (
    ExtractedField,
)
from meridianforge.extraction.image_extractor import (
    ImageEvidence,
)


@dataclass(frozen=True, slots=True)
class InvestmentEvidence:
    """
    Canonical evidence extracted from an artifact.
    """

    source_file: Path
    raw_text: str
    fields: tuple[ExtractedField, ...]
    extraction_method: str
    confidence: float


class EvidenceConsolidator:
    """
    Combine extraction outputs into canonical evidence.
    """

    @staticmethod
    def from_image(
        evidence: ImageEvidence,
        fields: list[ExtractedField],
    ) -> InvestmentEvidence:
        """
        Create canonical evidence from image OCR.
        """

        confidence_values = [
            evidence.confidence,
            *[field.confidence for field in fields],
        ]

        confidence = (
            sum(confidence_values) / len(confidence_values)
            if confidence_values
            else 0.0
        )

        return InvestmentEvidence(
            source_file=evidence.source_file,
            raw_text=evidence.text,
            fields=tuple(fields),
            extraction_method="OCR",
            confidence=round(
                confidence,
                3,
            ),
        )
