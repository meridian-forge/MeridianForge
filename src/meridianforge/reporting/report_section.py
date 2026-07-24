"""
Report section domain model.

MF-343.1

Groups related investor report metrics.
"""

from dataclasses import dataclass, field

from meridianforge.reporting.report_metric import (
    ReportMetric,
)


@dataclass(slots=True)
class ReportSection:
    """
    Logical section of an investor report.
    """

    title: str

    metrics: list[ReportMetric] = field(
        default_factory=list,
    )

    def add_metric(
        self,
        metric: ReportMetric,
    ) -> None:
        """
        Add metric to section.
        """

        self.metrics.append(
            metric,
        )
