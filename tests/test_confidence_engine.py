"""
Confidence engine tests.
"""

from meridianforge.intelligence.confidence_engine import (
    ConfidenceEngine,
)
from meridianforge.intelligence.mapping_memory import (
    MappingMemory,
)
from meridianforge.models.results.field_mapping import (
    FieldMapping,
)


def test_confidence_without_history() -> None:
    memory = MappingMemory()

    mappings = [
        FieldMapping(
            source_field="Price",
            target_field="purchase_price",
            confidence=0.90,
        )
    ]

    confidence = ConfidenceEngine.calculate(
        mappings,
        memory,
    )

    assert confidence == 0.90


def test_confidence_uses_mapping_history() -> None:
    memory = MappingMemory()

    memory.record_success(
        "Price",
        "purchase_price",
    )

    mappings = [
        FieldMapping(
            source_field="Price",
            target_field="purchase_price",
            confidence=0.90,
        )
    ]

    confidence = ConfidenceEngine.calculate(
        mappings,
        memory,
    )

    assert confidence > 0.90
