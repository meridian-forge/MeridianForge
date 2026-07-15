"""
JSON importer for Meridian Forge properties.
"""

from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path

from meridianforge.models.domain import (
    Acquisition,
    Address,
    Assumptions,
    Expenses,
    Financing,
    Income,
    Metadata,
    Property,
)


class PropertyJsonImporter:
    """
    Import Property objects from JSON.
    """

    @staticmethod
    def load(file_path: str) -> Property:
        path = Path(file_path)

        data = json.loads(path.read_text())

        return Property(
            metadata=Metadata(
                provider=data.get("provider", "Manual Import"),
                imported_at=data.get(
                    "imported_at",
                    datetime.now().isoformat(),
                ),
            ),
            address=Address(
                street=data["street"],
                city=data["city"],
                state=data["state"],
                zip_code=data["zip_code"],
            ),
            acquisition=Acquisition(
                purchase_price=data["purchase_price"],
                closing_costs=data["closing_costs"],
                rehab_cost=data.get("rehab_cost", 0.0),
            ),
            income=Income(
                monthly_rent=data["monthly_rent"],
                other_monthly_income=data.get(
                    "other_monthly_income",
                    0.0,
                ),
            ),
            expenses=Expenses(
                taxes=data["taxes"],
                insurance=data["insurance"],
                hoa=data.get("hoa", 0.0),
                maintenance=data.get("maintenance", 0.0),
                management=data.get("management", 0.0),
            ),
            financing=Financing(
                down_payment=data["down_payment"],
                interest_rate=data["interest_rate"],
                loan_term_years=data["loan_term_years"],
            ),
            assumptions=Assumptions(),
        )
