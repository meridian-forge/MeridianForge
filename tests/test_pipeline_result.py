"""
Pipeline result model tests.
"""

import pytest

from meridianforge.models.results.import_warning import (
    ImportWarning,
)
from meridianforge.models.results.pipeline_result import (
    PipelineResult,
)


def test_pipeline_result_defaults() -> None:
    result = PipelineResult()

    assert result.assets == []
    assert result.confidence == 0.0
    assert result.warnings == []


def test_import_warning_accepts_valid_confidence() -> None:
    warning = ImportWarning(
        field_name="Unknown Field",
        message="Field not recognized",
        confidence=0.50,
    )

    assert warning.confidence == 0.50


def test_invalid_confidence_fails() -> None:
    with pytest.raises(ValueError):
        ImportWarning(
            field_name="Test",
            message="Bad",
            confidence=2.0,
        )
