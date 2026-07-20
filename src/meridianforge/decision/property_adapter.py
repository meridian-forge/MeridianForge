"""
Decision property adapter.

Converts acquisition workflow inputs
into underwriting domain properties.
"""

from datetime import datetime

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
from meridianforge.workflows.acquisition_input import (
    AcquisitionInput,
)


class AcquisitionPropertyAdapter:
    """
    Converts AcquisitionInput into Property.
    """

    def build(
        self,
        opportunity: AcquisitionInput,
    ) -> Property:
        """
        Build underwriting property model.
        """

        return Property(
            address=Address(
                street=opportunity.property_address,
                city=opportunity.market,
                state="FL",
                zip_code="00000",
            ),
            acquisition=Acquisition(
                purchase_price=opportunity.purchase_price,
                closing_costs=0.0,
            ),
            financing=Financing(
                down_payment=(
                    opportunity.purchase_price * 0.20
                ),
                interest_rate=7.0,
                loan_term_years=30,
            ),
            income=Income(
                monthly_rent=0.0,
            ),
            expenses=Expenses(
                taxes=0.0,
                insurance=0.0,
            ),
            assumptions=Assumptions(),
            metadata=Metadata(
                provider=opportunity.source,
                imported_at=datetime.utcnow().isoformat(),
            ),
        )
