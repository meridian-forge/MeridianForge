"""
Opportunity metrics domain models.

Separates source-provided investment claims from
MeridianForge calculated validation metrics and
final decision metrics.
"""

from dataclasses import dataclass
from decimal import Decimal


@dataclass(slots=True)
class SourceMetrics:
    """
    Metrics extracted from source documents.

    These represent sponsor/provider claims and
    are not considered validated by MeridianForge.
    """

    claimed_purchase_price: Decimal | None = None
    claimed_rent: Decimal | None = None
    claimed_cashflow: Decimal | None = None
    claimed_roi: Decimal | None = None
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
    Metrics used by the decision engine.

    These represent MeridianForge investment
    decision signals rather than source claims.
    """

    risk_score: Decimal | None = None
    confidence_score: Decimal | None = None
    recommendation_score: Decimal | None = None


@dataclass(slots=True)
class OpportunityMetrics:
    """
    Complete investment metrics view.

    Maintains separation between:
    - what the source claims
    - what MeridianForge calculates
    - how MeridianForge decides
    """

    source: SourceMetrics
    verified: VerifiedMetrics
    decision: DecisionMetrics
