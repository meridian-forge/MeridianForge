"""
Portfolio operating cadence engine.

MF-348.1
"""

from dataclasses import dataclass


@dataclass(slots=True)
class OperatingCadence:
    """
    Defines recurring operating frequency.
    """

    name: str

    frequency: str

    category: str


class PortfolioCadenceEngine:
    """
    Generates portfolio operating rhythms.
    """

    def monthly(self) -> OperatingCadence:
        """
        Monthly investor cadence.
        """

        return OperatingCadence(
            name="Monthly Portfolio Review",
            frequency="MONTHLY",
            category="PERFORMANCE",
        )

    def quarterly(self) -> OperatingCadence:
        """
        Quarterly strategic cadence.
        """

        return OperatingCadence(
            name="Quarterly Portfolio Strategy Review",
            frequency="QUARTERLY",
            category="STRATEGY",
        )

    def annual(self) -> OperatingCadence:
        """
        Annual planning cadence.
        """

        return OperatingCadence(
            name="Annual Portfolio Planning",
            frequency="ANNUAL",
            category="PLANNING",
        )
