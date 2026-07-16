"""
Unknown field memory engine.

Learns from unidentified fields over time.
"""

from meridianforge.models.results.unknown_field import (
    UnknownField,
)


class UnknownFieldMemory:
    """
    Stores unknown field observations.
    """

    def __init__(self) -> None:
        self._memory: dict[str, UnknownField] = {}

    def record(
        self,
        field_name: str,
        related_fields: list[str] | None = None,
    ) -> None:
        """
        Record an unknown field occurrence.
        """

        key = field_name.lower()

        item = self._memory.get(key)

        if item is None:
            item = UnknownField(
                field_name=field_name,
            )

            self._memory[key] = item

        item.record_occurrence()

        if related_fields:
            for field in related_fields:
                if field not in item.related_fields:
                    item.related_fields.append(field)

    def get(
        self,
        field_name: str,
    ) -> UnknownField | None:
        """
        Retrieve unknown field history.
        """

        return self._memory.get(
            field_name.lower(),
        )
