"""
Import mapping result tests.
"""

import pytest

from meridianforge.models.results.import_mapping_result import (
    ImportMappingResult,
)


def test_valid_mapping_confidence() -> None:
    result = ImportMappingResult(
        source_field="Purchase Cost",
        mapped_field="purchase_price",
        confidence=0.98,
    )

    assert result.confidence == 0.98


def test_invalid_mapping_confidence() -> None:
    with pytest.raises(ValueError):
        ImportMappingResult(
            source_field="Unknown",
            mapped_field=None,
            confidence=2.0,
        )
