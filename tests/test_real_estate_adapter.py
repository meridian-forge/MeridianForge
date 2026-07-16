"""
Real estate adapter tests.
"""

from meridianforge.models.domain.normalized_asset import (
    NormalizedAsset,
)
from meridianforge.normalization.real_estate_adapter import (
    RealEstateAdapter,
)


def test_normalized_asset_converts_to_property() -> None:
    """
    Verify normalized data becomes a Property object.
    """

    asset = NormalizedAsset(
        asset_type="REAL_ESTATE",
        attributes={
            "street": "123 Main St",
            "city": "Jacksonville",
            "state": "FL",
            "zip_code": "32201",
            "purchase_price": "$250,000",
            "monthly_rent": "$2,200",
            "property_tax": "$3,500",
            "insurance": "$1,200",
        },
    )

    property_obj = RealEstateAdapter.convert(asset)

    assert property_obj.acquisition.purchase_price == 250000

    assert property_obj.income.monthly_rent == 2200

    assert property_obj.expenses.taxes == 3500


def test_missing_optional_fields_do_not_crash() -> None:
    """
    Verify incomplete imports are handled safely.
    """

    asset = NormalizedAsset(
        asset_type="REAL_ESTATE",
        attributes={
            "purchase_price": "200000",
            "monthly_rent": "1800",
            "state": "TX",
        },
    )

    property_obj = RealEstateAdapter.convert(asset)

    assert property_obj.acquisition.purchase_price == 200000

    assert property_obj.expenses.hoa == 0
