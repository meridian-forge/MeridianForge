"""
Unknown field memory tests.
"""

from meridianforge.intelligence.unknown_field_memory import (
    UnknownFieldMemory,
)


def test_unknown_field_is_recorded() -> None:
    memory = UnknownFieldMemory()

    memory.record(
        "Cash Needed",
        [
            "Purchase Price",
            "Closing Costs",
        ],
    )

    result = memory.get("Cash Needed")

    assert result is not None
    assert result.occurrences == 1
    assert "Purchase Price" in result.related_fields


def test_unknown_field_accumulates_history() -> None:
    memory = UnknownFieldMemory()

    memory.record("Investor Notes")
    memory.record("Investor Notes")

    result = memory.get("Investor Notes")

    assert result is not None
    assert result.occurrences == 2
