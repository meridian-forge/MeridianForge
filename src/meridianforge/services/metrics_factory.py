from __future__ import annotations

from decimal import Decimal

from meridianforge.models.domain.opportunity_metrics import (
    DecisionMetrics,
    OpportunityMetrics,
    SourceMetrics,
    VerifiedMetrics,
)


class MetricsFactory:
    """
    Canonical OpportunityMetrics construction helpers.
    """

    @staticmethod
    def from_source_claims(
        *,
        purchase_price: object | None = None,
        rent: object | None = None,
        cashflow: object | None = None,
        roi: object | None = None,
        cash_investment: object | None = None,
        interest_rate: object | None = None,
        cap_rate: object | None = None,
        annual_rent: object | None = None,
        noi: object | None = None,
        property_tax: object | None = None,
        insurance: object | None = None,
        vacancy_rate: object | None = None,
        management_rate: object | None = None,
        source_document: str | None = None,
    ) -> OpportunityMetrics:
        def dec(value: object | None) -> Decimal | None:
            if value is None:
                return None
            return Decimal(str(value))

        return OpportunityMetrics(
            source=SourceMetrics(
                claimed_purchase_price=dec(purchase_price),
                claimed_rent=dec(rent),
                claimed_cashflow=dec(cashflow),
                claimed_roi=dec(roi),
                claimed_cash_investment=dec(cash_investment),
                claimed_interest_rate=dec(interest_rate),
                claimed_cap_rate=dec(cap_rate),
                claimed_cash_on_cash_return=dec(roi),
                claimed_annual_rent=dec(annual_rent),
                claimed_noi=dec(noi),
                claimed_property_tax=dec(property_tax),
                claimed_insurance=dec(insurance),
                claimed_vacancy_rate=dec(vacancy_rate),
                claimed_management_rate=dec(management_rate),
                source_document=source_document,
            ),
            verified=VerifiedMetrics(),
            decision=DecisionMetrics(),
        )
