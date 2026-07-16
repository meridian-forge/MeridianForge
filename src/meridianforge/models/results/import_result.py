"""
Import result model.

Represents the outcome of reading external property data.
"""

from dataclasses import dataclass, field


@dataclass(slots=True)
class ImportResult:
    """
    Result from a property data import operation.
    """

    rows_processed: int

    rows_loaded: int

    rows_failed: int

    records: list[dict[str, object]] = field(
        default_factory=list,
    )

    warnings: list[str] = field(
        default_factory=list,
    )
