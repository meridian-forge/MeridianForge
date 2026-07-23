"""
Risk summary model.

MF-336.3.3

Structured investor-facing risk classification.
"""

from dataclasses import dataclass, field


@dataclass(slots=True)
class RiskSummary:
    """
    Categorized acquisition risks.
    """

    high: list[str] = field(
        default_factory=list,
    )

    medium: list[str] = field(
        default_factory=list,
    )

    low: list[str] = field(
        default_factory=list,
    )

    @property
    def all_risks(self) -> list[str]:
        """
        Flatten all risk categories.
        """

        return (
            self.high
            + self.medium
            + self.low
        )
