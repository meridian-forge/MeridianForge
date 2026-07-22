"""
Acquisition report model.

MF-336.1

Canonical investor-facing acquisition report.
"""

from dataclasses import dataclass, field
from datetime import datetime

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

    risks: list[str] = field(
        default_factory=list,
    )

    generated_at: datetime = field(
        default_factory=datetime.now,
    )
