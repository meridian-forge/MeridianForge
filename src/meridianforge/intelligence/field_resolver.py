"""
Field intelligence resolver.

Maps unknown external labels into
MeridianForge canonical fields.
"""

from __future__ import annotations

from meridianforge.intelligence.field_dictionary import (
    FIELD_ALIASES,
)


class FieldResolver:
    """
    Resolve external field names.
    """

    @staticmethod
    def resolve(
        field_name: str,
    ) -> str:

        normalized = field_name.strip().lower().replace("_", " ")

        for canonical, aliases in FIELD_ALIASES.items():

            for alias in aliases:

                if normalized == alias.lower():
                    return canonical

        return field_name.strip()
