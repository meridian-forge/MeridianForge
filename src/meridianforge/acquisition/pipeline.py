"""
Acquisition intelligence pipeline.

MF-333.2

Coordinates:

Opportunity
    ->
Canonical Property
    ->
Underwriting Engine
    ->
Acquisition Result
"""

from meridianforge.acquisition.criteria import (
    AcquisitionCriteria,
)

from meridianforge.acquisition.decision import (
    AcquisitionDecision,
)

from meridianforge.acquisition.opportunity import (
    Opportunity,
)

from meridianforge.acquisition.result import (
    AcquisitionResult,
)

from meridianforge.acquisition.score import (
    calculate_score,
)

from meridianforge.engine.underwriting_engine import (
    UnderwritingEngine,
)

from meridianforge.models.domain.acquisition import (
    Acquisition,
)

from meridianforge.models.domain.address import (
    Address,
)

from meridianforge.models.domain.assumptions import (
    Assumptions,
)

from meridianforge.models.domain.expenses import (
    Expenses,
)

from meridianforge.models.domain.financing import (
    Financing,
)

from meridianforge.models.domain.income import (
    Income,
)

from meridianforge.models.domain.metadata import (
    Metadata,
)

from meridianforge.models.domain.property import (
    Property,
)


class AcquisitionPipeline:
    """
    Executes end-to-end acquisition analysis.
    """

    def __init__(
        self,
        criteria: AcquisitionCriteria | None = None,
    ) -> None:

        self.criteria = (
            criteria
            if criteria is not None
            else AcquisitionCriteria()
        )

        self.engine = UnderwritingEngine()

    def run(
        self,
        opportunity: Opportunity,
    ) -> AcquisitionResult:
        """
        Analyze one acquisition opportunity.
        """

        property_data = self._to_property(
            opportunity,
        )

        analysis = self.engine.analyze(
            property_data,
        )

        score = calculate_score(
            analysis,
            self.criteria,
        )

        decision = AcquisitionDecision(
            status=(
                "BUY"
                if score >= 70
                else "REVIEW"
            ),
            score=score,
            reasons=[],
        )

        return AcquisitionResult(
            opportunity=opportunity,
            analysis=analysis,
            score=decision.score,
            ranking=0,
            recommendation=decision.status,
            confidence=score / 100,
        )

    def _to_property(
        self,
        opportunity: Opportunity,
    ) -> Property:
        """
        Convert acquisition opportunity
        into canonical underwriting property.
        """

        monthly_total_expenses = (
            opportunity.monthly_expenses
        )

        return Property(
            address=Address(
                street=opportunity.address,
                city=opportunity.city,
                state=opportunity.state,
                zip_code=opportunity.zip_code,
            ),
            acquisition=Acquisition(
                purchase_price=(
                    opportunity.purchase_price
                ),
                closing_costs=0,
            ),
            financing=Financing(
                down_payment=(
                    opportunity.purchase_price
                    * 0.20
                ),
                interest_rate=7.0,
                loan_term_years=30,
            ),
            income=Income(
                monthly_rent=(
                    opportunity.monthly_rent
                ),
            ),
            expenses=Expenses(
            taxes=(
                monthly_total_expenses
                * 12
                * 0.60
                ),
            insurance=(
                monthly_total_expenses
                * 12
                * 0.40
                ),
            ),
            assumptions=Assumptions(),
            metadata=Metadata(
                provider=opportunity.source,
                imported_at=(
                    opportunity.created_at.isoformat()
                ),
            ),
        )
