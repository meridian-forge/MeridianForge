"""
Batch import result model.

Represents the outcome of processing
multiple investment records.
"""

from dataclasses import dataclass, field


@dataclass(slots=True)
class BatchImportResult:
    """
    Summary result for a batch import operation.
    """

    records_received: int

    records_processed: int

    records_failed: int

    assets: list[dict[str, object]] = field(
        default_factory=list,
    )

    warnings: list[str] = field(
        default_factory=list,
    )

    confidence: float = 0.0

    learned_mappings: int = 0

    unknown_fields: list[str] = field(
        default_factory=list,
    )

    @property
    def success_rate(self) -> float:
        """
        Percentage of successfully processed records.
        """

        if self.records_received == 0:
            return 0.0

        return self.records_processed / self.records_received
