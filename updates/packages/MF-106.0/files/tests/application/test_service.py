from meridianforge.application.models import (
    PropertyInput,
)

from meridianforge.application.service import (
    MeridianForgeService,
)


def test_service():

    result = MeridianForgeService().analyze_property(
        PropertyInput(
            address="123 Main",
            purchase_price=200000,
            monthly_rent=2000,
            noi=12000,
            annual_cash_flow=6000,
            cash_invested=50000,
            annual_debt=8000,
        )
    )

    assert result["cap_rate"] == 0.06
    assert result["dscr"] == 1.5
