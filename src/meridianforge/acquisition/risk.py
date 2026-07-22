"""
Acquisition risk models.

MF-334.1

Defines standardized risk flags used
during acquisition decisions.
"""

from dataclasses import dataclass
from enum import StrEnum


class RiskSeverity(StrEnum):
    """
    Risk impact level.
    """

    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"


@dataclass(slots=True)
class RiskFlag:
    """
    Represents an acquisition risk.
    """

    code: str
    message: str
    severity: RiskSeverity
