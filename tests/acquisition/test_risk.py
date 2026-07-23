"""
Tests for acquisition risk models.

MF-334.1
"""

from meridianforge.acquisition.risk import (
    RiskFlag,
    RiskSeverity,
)


def test_risk_flag_creation() -> None:

    risk = RiskFlag(
        code="HIGH_RATE",
        message="Interest rate assumption elevated",
        severity=RiskSeverity.MEDIUM,
    )

    assert risk.code == "HIGH_RATE"

    assert risk.severity == RiskSeverity.MEDIUM
