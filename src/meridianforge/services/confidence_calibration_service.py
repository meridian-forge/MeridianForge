"""
Confidence calibration service.

MF-440.7.2

Transforms raw extractor confidence into historically calibrated confidence.
"""

from __future__ import annotations

from meridianforge.models.domain.extractor_confidence_calibration import (
    ExtractorConfidenceCalibration,
)
from meridianforge.repositories.extraction_audit_repository import (
    ExtractionAuditRepository,
)


class ConfidenceCalibrationService:
    """
    Calibrate extractor confidence using historical extraction outcomes.
    """

    def __init__(
        self,
        repository: ExtractionAuditRepository | None = None,
    ) -> None:
        self._repository = repository or ExtractionAuditRepository()

    def calibrate(
        self,
        extractor: str,
        raw_confidence: float,
        provider: str | None = None,
    ) -> ExtractorConfidenceCalibration:
        """
        Return calibrated confidence for an extractor.

        Historical accepted/rejected outcomes adjust raw confidence.
        """

        records = [
            record
            for record in self._repository.all()
            if record.extractor == extractor and record.provider == provider
        ]

        if not records:
            return ExtractorConfidenceCalibration(
                extractor=extractor,
                provider=provider,
                raw_confidence=raw_confidence,
                calibrated_confidence=raw_confidence,
            )

        accepted = sum(1 for record in records if record.status.value == "accepted")

        calibration_factor = accepted / len(records)

        calibrated = raw_confidence * 0.5 + calibration_factor * 0.5

        return ExtractorConfidenceCalibration(
            extractor=extractor,
            provider=provider,
            raw_confidence=raw_confidence,
            calibrated_confidence=calibrated,
        )
