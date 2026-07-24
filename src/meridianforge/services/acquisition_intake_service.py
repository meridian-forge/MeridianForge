from dataclasses import dataclass
from datetime import datetime
from typing import Any


@dataclass(frozen=True)
class AcquisitionOpportunity:
    """
    Normalized acquisition opportunity.
    """

    address: str
    city: str
    state: str
    zip_code: str
    purchase_price: float
    monthly_rent: float
    monthly_expenses: float
    market: str
    source: str
    created_at: datetime

    @property
    def monthly_cash_flow(self) -> float:
        return self.monthly_rent - self.monthly_expenses

    @property
    def cap_rate(self) -> float:
        if self.purchase_price <= 0:
            return 0.0

        annual_noi = self.monthly_cash_flow * 12

        return annual_noi / self.purchase_price


class AcquisitionIntakeService:
    """
    Converts raw acquisition inputs
    into normalized acquisition opportunities.
    """

    def create_opportunity(
        self,
        data: dict[str, Any],
    ) -> AcquisitionOpportunity:
        """
        Create normalized opportunity from raw input.
        """

        address = str(
            data.get(
                "address",
                data.get(
                    "property_address",
                    "Unknown Address",
                ),
            )
        )

        city = str(
            data.get(
                "city",
                data.get(
                    "market",
                    "Unknown",
                ),
            )
        )

        state_value = data.get(
            "state",
        )

        if state_value:
            state = str(state_value)
        else:
            market = str(
                data.get(
                    "market",
                    "",
                )
            ).lower()

            state_lookup = {
                "jacksonville": "FL",
            }

            state = state_lookup.get(
                market,
                "NA",
            )

        zip_code = str(
            data.get(
                "zip_code",
                "00000",
            )
        )

        return AcquisitionOpportunity(
            address=address,
            city=city,
            state=state,
            zip_code=zip_code,
            purchase_price=float(
                data.get(
                    "purchase_price",
                    0,
                )
            ),
            monthly_rent=float(
                data.get(
                    "monthly_rent",
                    data.get(
                        "rent",
                        0,
                    ),
                )
            ),
            monthly_expenses=float(
                data.get(
                    "monthly_expenses",
                    0,
                )
            ),
            market=str(
                data.get(
                    "market",
                    city,
                )
            ),
            source=str(
                data.get(
                    "source",
                    "import",
                )
            ),
            created_at=datetime.now(),
        )
