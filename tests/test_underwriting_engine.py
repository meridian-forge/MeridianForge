from meridianforge.engine import UnderwritingEngine
from meridianforge.models.domain.acquisition import Acquisition
from meridianforge.models.domain.address import Address
from meridianforge.models.domain.assumptions import Assumptions
from meridianforge.models.domain.expenses import Expenses
from meridianforge.models.domain.financing import Financing
from meridianforge.models.domain.income import Income
from meridianforge.models.domain.metadata import Metadata
from meridianforge.models.domain.property import Property


def create_sample_property() -> Property:
    """
    Creates a known investment scenario
    for underwriting verification.
    """

    return Property(
        address=Address(
            street="123 Main",
            city="Jacksonville",
            state="FL",
            zip_code="32218",
        ),
        acquisition=Acquisition(
            purchase_price=200000,
            closing_costs=5000,
        ),
        financing=Financing(
            down_payment=50000,
            interest_rate=6.5,
            loan_term_years=30,
        ),
        income=Income(
            monthly_rent=2000,
        ),
        expenses=Expenses(
            taxes=2400,
            insurance=1200,
            management=200,
            maintenance=100,
        ),
        assumptions=Assumptions(),
        metadata=Metadata(
            provider="Manual",
            imported_at="2026-07-15",
        ),
    )


def test_underwriting_calculations():

    property_data = create_sample_property()

    result = UnderwritingEngine.analyze(property_data)

    assert round(result.cap_rate, 2) == 8.40

    assert round(result.dscr, 2) == 1.48

    assert (
        round(
            result.monthly_cash_flow,
            2,
        )
        == 451.90
    )

    assert (
        round(
            result.cash_on_cash_return,
            2,
        )
        == 10.85
    )
