"""
Field detection engine.

Maps unknown external field names to
Meridian Forge canonical fields.
"""

from meridianforge.intelligence.field_dictionary import (
    FIELD_ALIASES,
)
from meridianforge.models.results.field_mapping import (
    FieldMapping,
)


class FieldDetector:
    """
    Detects probable meanings of external fields.
    """

    @staticmethod
    def detect(
        fields: list[str],
    ) -> list[FieldMapping]:
        """
        Detect possible mappings.
        """

        mappings: list[FieldMapping] = []

        for field in fields:

            normalized = field.lower().strip()

            best_match: str | None = None

            for target, aliases in FIELD_ALIASES.items():

                if normalized in aliases:
                    best_match = target
                    break

                for alias in aliases:
                    if alias in normalized:
                        best_match = target
                        break

                if best_match:
                    break

            if best_match:
                mappings.append(
                    FieldMapping(
                        source_field=field,
                        target_field=best_match,
                        confidence=0.90,
                    )
                )

        return mappings
