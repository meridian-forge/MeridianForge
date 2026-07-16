"""
Unknown field model.

Stores fields that could not be automatically mapped.
"""

from dataclasses import dataclass, field


@dataclass(slots=True)
class UnknownField:
    """
    Represents an unidentified source field.
    """

    field_name: str

    occurrences: int = 0

    suggested_target: str | None = None

    confidence: float = 0.0

    related_fields: list[str] = field(
        default_factory=list,
    )

    def record_occurrence(self) -> None:
        """
        Increment field observation count.
        """

        self.occurrences += 1
