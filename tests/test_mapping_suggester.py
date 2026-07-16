"""
Mapping suggester tests.
"""

from meridianforge.intelligence.mapping_suggester import (
    MappingSuggester,
)


def test_cash_needed_suggestion() -> None:
    result = MappingSuggester.suggest(
        "Cash Needed",
        [
            "Purchase Price",
            "Closing Costs",
        ],
    )

    assert result is not None
    assert result.target_field == "cash_to_close"
    assert result.confidence > 0


def test_unknown_field_returns_none() -> None:
    result = MappingSuggester.suggest(
        "Random Notes",
        [
            "Something",
        ],
    )

    assert result is None
