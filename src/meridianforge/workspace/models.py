from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal


@dataclass
class OpportunityRecord:
    """
    Investor workspace record.

    Represents a property opportunity entering
    the Meridian Forge analysis workflow.
    """

    address: str
    market: str

    purchase_price: Decimal
    monthly_rent: Decimal

    source: str

    created_at: datetime

    id: str | None = None

    notes: str | None = None
