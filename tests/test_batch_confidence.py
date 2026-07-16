"""
Batch confidence tests.
"""

from meridianforge.intelligence.batch_confidence import (
    BatchConfidence,
)


def test_batch_confidence_average() -> None:
    confidence = BatchConfidence.calculate(
        [
            0.90,
            0.80,
        ]
    )

    assert round(confidence, 2) == 0.85


def test_batch_confidence_penalizes_failures() -> None:
    confidence = BatchConfidence.calculate(
        [
            0.90,
            0.90,
        ],
        failed_records=10,
        total_records=100,
    )

    assert confidence < 0.90


def test_empty_batch_confidence() -> None:
    assert BatchConfidence.calculate([]) == 0.0
