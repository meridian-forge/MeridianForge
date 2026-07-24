"""
Acquisition property adapter.

MF-333.3

Converts acquisition opportunities into
canonical underwriting Property models.
"""

from meridianforge.acquisition.opportunity import (
    Opportunity,
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


class AcquisitionPropertyAdapter:
    """
    Converts acquisition opportunities into
    canonical underwriting properties.
    """

    def convert(
        self,
        opportunity: Opportunity,
    ) -> Property:
        """
        Build canonical Property object.
        """

        annual_expenses = opportunity.monthly_expenses * 12

        return Property(
            address=Address(
                street=opportunity.address,
                city=opportunity.city,
                state=opportunity.state,
                zip_code=opportunity.zip_code,
            ),
            acquisition=Acquisition(
                purchase_price=(opportunity.purchase_price),
                closing_costs=0,
            ),
            financing=Financing(
                down_payment=(opportunity.purchase_price * 0.20),
                interest_rate=7.0,
                loan_term_years=30,
            ),
            income=Income(
                monthly_rent=(opportunity.monthly_rent),
            ),
            expenses=Expenses(
                taxes=annual_expenses * 0.60,
                insurance=annual_expenses * 0.40,
            ),
            assumptions=Assumptions(),
            metadata=Metadata(
                provider=opportunity.source,
                imported_at=(opportunity.created_at.isoformat()),
            ),
        )
