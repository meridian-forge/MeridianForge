"""
Opportunity metrics domain models.

Separates:
- source-provided investment claims
- MeridianForge calculated validation metrics
- final decision metrics
"""

from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal


@dataclass(slots=True)
class SourceMetrics:
    """
    Metrics extracted from source documents.

    These represent provider/sponsor claims.
    They are evidence only and are NOT validated
    until MeridianForge underwriting runs.
    """

    claimed_purchase_price: Decimal | None = None
    claimed_rent: Decimal | None = None
    claimed_cashflow: Decimal | None = None
    claimed_roi: Decimal | None = None

    claimed_cash_investment: Decimal | None = None
    claimed_interest_rate: Decimal | None = None
    claimed_cap_rate: Decimal | None = None
    claimed_cash_on_cash_return: Decimal | None = None

    claimed_annual_rent: Decimal | None = None
    claimed_noi: Decimal | None = None
    claimed_property_tax: Decimal | None = None
    claimed_insurance: Decimal | None = None

    claimed_vacancy_rate: Decimal | None = None
    claimed_management_rate: Decimal | None = None

    source_document: str | None = None


@dataclass(slots=True)
class VerifiedMetrics:
    """
    Metrics calculated by MeridianForge underwriting.
    """

    calculated_cashflow: Decimal | None = None
    cap_rate: Decimal | None = None
    cash_on_cash_return: Decimal | None = None
    dscr: Decimal | None = None


@dataclass(slots=True)
class DecisionMetrics:
    """
    Metrics used by the MeridianForge decision engine.
    """

    risk_score: Decimal | None = None
    confidence_score: Decimal | None = None
    recommendation_score: Decimal | None = None


@dataclass(slots=True)
class OpportunityMetrics:
    """
    Complete investment metrics view.

    Maintains separation between:
    - source claims
    - verified underwriting
    - decision intelligence
    """

    source: SourceMetrics
    verified: VerifiedMetrics
    decision: DecisionMetrics
