from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

from meridianforge.acquisition.opportunity import Opportunity


@dataclass(slots=True)
class QuarantinedRecord:
    """
    Represents a row that could not be normalized
    into a valid opportunity.
    """

    source_file: Path
    row_number: int
    reason: str
    raw_record: dict[str, object] = field(default_factory=dict)


@dataclass(slots=True)
class PortfolioOpportunity:
    """
    A normalized opportunity with portfolio context.
    """

    source_file: Path
    row_number: int
    opportunity: Opportunity


@dataclass(slots=True)
class PortfolioIngestionResult:
    """
    Result of ingesting a portfolio workbook or CSV.
    """

    opportunities: list[PortfolioOpportunity] = field(default_factory=list)
    quarantined: list[QuarantinedRecord] = field(default_factory=list)

    @property
    def total_rows(self) -> int:
        return len(self.opportunities) + len(self.quarantined)

    @property
    def ready_count(self) -> int:
        return len(self.opportunities)

    @property
    def quarantine_count(self) -> int:
        return len(self.quarantined)

    @property
    def success_rate(self) -> float:
        if self.total_rows == 0:
            return 0.0
        return self.ready_count / self.total_rows
