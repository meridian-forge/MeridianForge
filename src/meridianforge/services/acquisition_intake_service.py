"""
Acquisition intake service.

Transforms raw acquisition data into Opportunity objects.
"""

from datetime import datetime
from typing import Any

from meridianforge.acquisition.opportunity import (
    Opportunity,
)


class AcquisitionIntakeService:
    """
    Converts incoming acquisition records into domain models.
    """

    def create_opportunity(
        self,
        data: dict[str, Any],
    ) -> Opportunity:
        """
        Create opportunity from input record.
        """

        return Opportunity(
            address=str(data["address"]),
            city=str(data["city"]),
            state=str(data["state"]),
            zip_code=str(data["zip_code"]),
            purchase_price=float(
                data["purchase_price"],
            ),
            monthly_rent=float(
                data["monthly_rent"],
            ),
            monthly_expenses=float(
                data["monthly_expenses"],
            ),
            market=str(data["market"]),
            source=str(data["source"]),
            created_at=datetime.now(),
        )
