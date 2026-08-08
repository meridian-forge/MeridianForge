from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal
from pathlib import Path

from meridianforge.extraction.identity_extractor import IdentityEvidence
from meridianforge.models.domain.opportunity_metrics import VerifiedMetrics


@dataclass(slots=True)
class EvidencePayload:
    """
    Canonical evidence payload flowing through the evidence pipeline.

    This replaces dictionary-based evidence contracts while remaining
    provider agnostic.
    """

    source_file: str
    source_method: str = "evidence"
    confidence: float = 1.0

    identity: IdentityEvidence = field(default_factory=IdentityEvidence)

    financial_fields: dict[str, Decimal] = field(default_factory=dict)

    raw_text: str | None = None

    image_paths: list[Path] = field(default_factory=list)

    validated_metrics: VerifiedMetrics | None = None

    def get_decimal(
        self,
        field_name: str,
    ) -> Decimal | None:
        return self.financial_fields.get(field_name)

    def get_float(
        self,
        field_name: str,
        default: float = 0.0,
    ) -> float:
        value = self.get_decimal(field_name)

        if value is None:
            return default

        return float(value)
