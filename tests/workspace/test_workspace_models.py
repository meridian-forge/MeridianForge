from datetime import datetime
from decimal import Decimal

from meridianforge.workspace.models import OpportunityRecord


def test_opportunity_record_creation():

    opportunity = OpportunityRecord(
        address="123 Main St",
        market="Jacksonville FL",
        purchase_price=Decimal("250000"),
        monthly_rent=Decimal("2200"),
        source="manual",
        created_at=datetime.now(),
    )

    assert opportunity.address == "123 Main St"
    assert opportunity.market == "Jacksonville FL"
    assert opportunity.purchase_price == Decimal("250000")
