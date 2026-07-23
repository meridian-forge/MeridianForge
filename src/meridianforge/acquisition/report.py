"""
Acquisition report model.

MF-336.3.3

Canonical investor-facing acquisition report.
"""

from dataclasses import dataclass, field
from datetime import datetime

from meridianforge.acquisition.risk_summary import (
    RiskSummary,
)

from meridianforge.acquisition.snapshot import (
    UnderwritingSnapshot,
)

from meridianforge.acquisition.thesis import (
    InvestmentThesis,
)


@dataclass(slots=True)
class AcquisitionReport:
    """
    Investor-facing acquisition report.
    """

    property_address: str

    recommendation: str

    score: float

    confidence: float

    purchase_price: float

    monthly_rent: float

    annual_cash_flow: float

    cap_rate: float

    cash_on_cash_return: float

    dscr: float

    thesis: InvestmentThesis

    snapshot: UnderwritingSnapshot | None = None

    risks: list[str] = field(
        default_factory=list,
    )

    risk_summary: RiskSummary | None = None

    generated_at: datetime = field(
        default_factory=datetime.now,
    )

    def __post_init__(self) -> None:
        """
        Maintain backward compatibility.
        """

        if self.snapshot is None:
            self.snapshot = UnderwritingSnapshot(
                purchase_price=self.purchase_price,
                monthly_rent=self.monthly_rent,
                annual_cash_flow=(
                    self.annual_cash_flow
                ),
                cap_rate=self.cap_rate,
                cash_on_cash_return=(
                    self.cash_on_cash_return
                ),
                dscr=self.dscr,
                monthly_cash_flow=(
                    self.annual_cash_flow / 12
                ),
            )

        if self.risk_summary is None:
            self.risk_summary = RiskSummary(
                medium=self.risks.copy(),
            )

        if not self.risks:
            self.risks = (
                self.risk_summary.all_risks
            )
