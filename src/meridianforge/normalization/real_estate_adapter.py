"""
Real estate normalization adapter.

Converts NormalizedAsset records into
Meridian Forge Property objects.
"""

from meridianforge.models.domain.acquisition import Acquisition
from meridianforge.models.domain.address import Address
from meridianforge.models.domain.assumptions import Assumptions
from meridianforge.models.domain.expenses import Expenses
from meridianforge.models.domain.financing import Financing
from meridianforge.models.domain.income import Income
from meridianforge.models.domain.metadata import Metadata
from meridianforge.models.domain.normalized_asset import (
    NormalizedAsset,
)
from meridianforge.models.domain.property import Property


class RealEstateAdapter:
    """
    Converts normalized data into Property objects.
    """

    @staticmethod
    def _to_float(
        value: object,
        default: float = 0.0,
    ) -> float:
        """
        Convert financial values safely.
        """

        if value is None:
            return default

        if isinstance(value, (int, float)):
            return float(value)

        cleaned = str(value).replace("$", "").replace(",", "").strip()

        multiplier = 1

        if cleaned.lower().endswith("k"):
            multiplier = 1000
            cleaned = cleaned[:-1]

        try:
            return float(cleaned) * multiplier
        except ValueError:
            return default

    @staticmethod
    def convert(
        asset: NormalizedAsset,
    ) -> Property:
        """
        Convert normalized asset into Property.
        """

        data = asset.attributes

        purchase_price = RealEstateAdapter._to_float(
            data.get("purchase_price"),
        )

        address = Address(
            street=str(
                data.get(
                    "street",
                    data.get(
                        "address",
                        data.get(
                            "property_address",
                            "UNKNOWN",
                        ),
                    ),
                )
            ),
            city=str(
                data.get(
                    "city",
                    "UNKNOWN",
                )
            ),
            state=str(
                data.get(
                    "state",
                    "NA",
                )
            ),
            zip_code=str(
                data.get(
                    "zip_code",
                    "00000",
                )
            ),
        )

        acquisition = Acquisition(
            purchase_price=purchase_price,
            closing_costs=RealEstateAdapter._to_float(
                data.get("closing_costs"),
            ),
            rehab_cost=RealEstateAdapter._to_float(
                data.get("rehab_cost"),
            ),
        )

        income = Income(
            monthly_rent=RealEstateAdapter._to_float(
                data.get(
                    "monthly_rent",
                    data.get(
                        "rent",
                    ),
                ),
            ),
        )

        expenses = Expenses(
            taxes=RealEstateAdapter._to_float(
                data.get("property_tax"),
            ),
            insurance=RealEstateAdapter._to_float(
                data.get("insurance"),
            ),
            hoa=RealEstateAdapter._to_float(
                data.get("hoa"),
            ),
            management=RealEstateAdapter._to_float(
                data.get("management"),
            ),
            maintenance=RealEstateAdapter._to_float(
                data.get("maintenance"),
            ),
        )

        default_down_payment = purchase_price * 0.20

        financing = Financing(
            down_payment=RealEstateAdapter._to_float(
                data.get(
                    "down_payment",
                    default_down_payment,
                ),
            ),
            interest_rate=RealEstateAdapter._to_float(
                data.get(
                    "interest_rate",
                    7.0,
                ),
            ),
            loan_term_years=int(
                RealEstateAdapter._to_float(
                    data.get(
                        "loan_term_years",
                        30,
                    ),
                )
            ),
        )

        metadata = Metadata(
            provider=str(
                data.get(
                    "provider",
                    "unknown",
                )
            ),
            imported_at=str(
                data.get(
                    "imported_at",
                    "unknown",
                )
            ),
        )

        return Property(
            address=address,
            acquisition=acquisition,
            financing=financing,
            income=income,
            expenses=expenses,
            assumptions=Assumptions(),
            metadata=metadata,
        )
