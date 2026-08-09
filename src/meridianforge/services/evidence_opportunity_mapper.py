"""
Evidence opportunity mapper.

Converts normalized evidence extracted from any source
(OCR, PDF, spreadsheet, API, etc.) into the canonical
NormalizedRentalOpportunity model.
"""

from __future__ import annotations

from decimal import Decimal

from meridianforge.models.domain.acquisition import Acquisition
from meridianforge.models.domain.evidence_payload import (
    EvidencePayload,
)
from meridianforge.models.domain.opportunity_metrics import (
    DecisionMetrics,
    OpportunityMetrics,
    SourceMetrics,
    VerifiedMetrics,
)
from meridianforge.services.opportunity_mapper import (
    NormalizedRentalOpportunity,
)


class EvidenceOpportunityMapper:
    DEFAULT_CLOSING_COST_RATE = 0.03

    @classmethod
    def map(
        cls,
        evidence: EvidencePayload,
    ) -> NormalizedRentalOpportunity:
        purchase_price = evidence.get_float("purchase_price")

        monthly_rent = evidence.get_float("monthly_rent")

        acquisition = Acquisition(
            purchase_price=purchase_price,
            closing_costs=evidence.get_float(
                "closing_costs",
                purchase_price * cls.DEFAULT_CLOSING_COST_RATE,
            ),
            rehab_cost=evidence.get_float("rehab_cost"),
        )

        def dec(name: str) -> Decimal | None:
            return evidence.get_decimal(name)

        metrics = OpportunityMetrics(
            source=SourceMetrics(
                claimed_purchase_price=dec("purchase_price"),
                claimed_rent=dec("monthly_rent"),
                claimed_cashflow=dec("monthly_cash_flow"),
                claimed_roi=dec("cash_on_cash_return"),
                claimed_cash_investment=dec("cash_investment"),
                claimed_interest_rate=dec("interest_rate"),
                claimed_cap_rate=dec("cap_rate"),
                claimed_cash_on_cash_return=dec("cash_on_cash_return"),
                claimed_annual_rent=dec("annual_rent"),
                claimed_noi=dec("annual_noi"),
                claimed_property_tax=dec("property_tax"),
                claimed_insurance=dec("insurance"),
                claimed_vacancy_rate=dec("vacancy_rate"),
                claimed_management_rate=dec("management_rate"),
                source_document=evidence.source_file,
            ),
            verified=VerifiedMetrics(),
            decision=DecisionMetrics(),
        )

        return NormalizedRentalOpportunity(
            city=evidence.identity.city or "UNKNOWN",
            state=evidence.identity.state or "NA",
            acquisition=acquisition,
            monthly_rent=monthly_rent,
            metrics=metrics,
        )
