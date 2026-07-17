"""
Acquisition assessment model.

Stores underwriting outputs connected
to an acquisition workflow.
"""

from dataclasses import dataclass, field


@dataclass(slots=True)
class AcquisitionAssessment:
    """
    Financial assessment result.
    """

    purchase_price: float = 0.0

    monthly_cash_flow: float = 0.0

    cap_rate: float = 0.0

    cash_on_cash_return: float = 0.0

    dscr: float = 0.0

    metrics: dict[str, float] = field(
        default_factory=dict,
    )
