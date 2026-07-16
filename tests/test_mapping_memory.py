"""
Mapping memory tests.
"""

from meridianforge.intelligence.mapping_memory import (
    MappingMemory,
)


def test_record_success_mapping() -> None:
    """
    Verify successful mappings are stored.
    """

    memory = MappingMemory()

    memory.record_success(
        "Expected Income",
        "monthly_rent",
    )

    result = memory.get(
        "Expected Income",
    )

    assert result is not None
    assert result.successful_mappings == 1
    assert result.confidence == 1.0


def test_confidence_updates_with_history() -> None:
    """
    Verify confidence changes over time.
    """

    memory = MappingMemory()

    memory.record_success(
        "Income",
        "monthly_rent",
    )

    memory.record_success(
        "Income",
        "monthly_rent",
    )

    memory.record_failure(
        "Income",
        "monthly_rent",
    )

    result = memory.get(
        "Income",
    )

    assert result is not None
    assert result.total_attempts == 3
    assert round(result.confidence, 2) == 0.67


def test_unknown_mapping_returns_none() -> None:
    """
    Verify unknown fields return nothing.
    """

    memory = MappingMemory()

    assert memory.get("Unknown") is None
