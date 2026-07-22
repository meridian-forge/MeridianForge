"""
Acquisition intake service.

Supports:
- Raw acquisition data -> Opportunity
- Opportunity -> pipeline record
"""

from datetime import datetime
from typing import Any

from meridianforge.acquisition.opportunity import Opportunity as AcquisitionOpportunity
from meridianforge.opportunity.models import Opportunity


class AcquisitionIntakeService:
    """
    Converts acquisition inputs into domain objects
    and pipeline-ready records.
    """

    def create_opportunity(
        self,
        data: dict[str, Any],
    ) -> AcquisitionOpportunity:
        """
        Create opportunity from raw input record.
        """

        return AcquisitionOpportunity(
            address=str(data["address"]),
            city=str(data["city"]),
            state=str(data["state"]),
            zip_code=str(data["zip_code"]),
            purchase_price=float(data["purchase_price"]),
            monthly_rent=float(data["monthly_rent"]),
            monthly_expenses=float(data["monthly_expenses"]),
            market=str(data["market"]),
            source=str(data["source"]),
            created_at=datetime.now(),
        )

    def convert(
        self,
        opportunity: Opportunity,
    ) -> dict[str, Any]:
        """
        Convert intake Opportunity into
        real estate pipeline record.
        """

        fields = opportunity.fields

        return {
            "address": fields.get(
                "address",
                fields.get(
                    "property_address",
                    "UNKNOWN",
                ),
            ),
            "purchase_price": fields.get(
                "purchase_price",
                0,
            ),
            "monthly_rent": fields.get(
                "monthly_rent",
                fields.get(
                    "rent",
                    0,
                ),
            ),
            "market": fields.get(
                "market",
                "UNKNOWN",
            ),
            "noi": fields.get(
                "noi",
                0,
            ),
        }
