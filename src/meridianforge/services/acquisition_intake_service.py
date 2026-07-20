"""
Acquisition intake service.

Transforms generic opportunities
into acquisition workflow inputs.
"""

from meridianforge.opportunity.models import Opportunity
from meridianforge.workflows.acquisition_input import (
    AcquisitionInput,
)


class AcquisitionIntakeService:
    """
    Converts normalized opportunities
    into acquisition inputs.
    """

    def convert(
        self,
        opportunity: Opportunity,
    ) -> AcquisitionInput:
        """
        Build acquisition workflow input.
        """

        fields = opportunity.fields

        return AcquisitionInput(
            property_address=fields.get(
                "property_address",
                opportunity.source_file,
            ),
            purchase_price=float(
                fields.get(
                    "purchase_price",
                    0,
                )
            ),
            market=fields.get(
                "market",
                "UNKNOWN",
            ),
            source=opportunity.source_file,
        )
