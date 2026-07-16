"""
Mapping suggestion engine.

Uses historical field context to suggest
possible normalized targets.
"""

from meridianforge.models.results.suggested_mapping import (
    SuggestedMapping,
)


class MappingSuggester:
    """
    Suggests mappings for unknown fields.
    """

    FIELD_PATTERNS: dict[str, list[str]] = {
        "cash_to_close": [
            "cash",
            "closing",
            "down payment",
            "capital required",
        ],
        "monthly_rent": [
            "rent",
            "income",
        ],
        "purchase_price": [
            "price",
            "purchase",
            "cost",
        ],
    }

    @classmethod
    def suggest(
        cls,
        field_name: str,
        related_fields: list[str] | None = None,
    ) -> SuggestedMapping | None:
        """
        Generate a mapping suggestion.
        """

        searchable = field_name.lower() + " " + " ".join(related_fields or []).lower()

        for target, keywords in cls.FIELD_PATTERNS.items():

            matches = [keyword for keyword in keywords if keyword in searchable]

            if matches:
                confidence = min(
                    0.95,
                    0.50 + (len(matches) * 0.15),
                )

                return SuggestedMapping(
                    source_field=field_name,
                    target_field=target,
                    confidence=round(
                        confidence,
                        2,
                    ),
                    reason=(
                        "Matched historical " "field patterns: " + ", ".join(matches)
                    ),
                )

        return None
