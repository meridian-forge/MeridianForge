"""
Extractor confidence calibration.

MF-440.7.1

Represents calibrated confidence derived from extractor history.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ExtractorConfidenceCalibration:
    """
    Calibrated confidence score for extractor decisions.
    """

    extractor: str

    provider: str | None = None

    raw_confidence: float = 0.0

    historical_accuracy: float = 0.0

    calibrated_confidence: float = 0.0

    sample_size: int = 0
