"""
Operations layer domain models.

Contains execution-level objects used by the Monday operations workflow.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path

from meridianforge.product.weekly_review import WeeklyInvestorReview


@dataclass
class OperationsRunResult:
    """
    Summary of a MeridianForge operations execution.

    This object intentionally contains orchestration-level information only.
    Detailed underwriting and extraction results remain owned by their
    respective services.
    """

    started_at: datetime
    completed_at: datetime | None = None

    files_discovered: list[Path] = field(default_factory=list)
    files_processed: list[Path] = field(default_factory=list)
    failed_files: list[Path] = field(default_factory=list)

    analyses_completed: int = 0
    analyses_failed: int = 0

    buy_count: int = 0
    watch_count: int = 0
    pass_count: int = 0

    dashboard_path: Path | None = None
    report_paths: list[Path] = field(default_factory=list)

    review: WeeklyInvestorReview | None = None

    errors: list[str] = field(default_factory=list)

    @property
    def total_files(self) -> int:
        """Return total discovered files."""
        return len(self.files_discovered)

    @property
    def success(self) -> bool:
        """Return whether execution completed without failures."""
        return len(self.failed_files) == 0 and len(self.errors) == 0
