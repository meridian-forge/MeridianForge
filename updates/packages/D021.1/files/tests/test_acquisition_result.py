import pytest

from meridianforge.models.results.acquisition_result import (
    AcquisitionResult,
)


def test_acquisition_result_defaults() -> None:

    result = AcquisitionResult()

    assert result.recommendation == "MANUAL_REVIEW"
    assert result.confidence == 0.0


def test_acquisition_result_confidence_validation() -> None:

    with pytest.raises(ValueError):

        AcquisitionResult(
            confidence=1.5,
        )
