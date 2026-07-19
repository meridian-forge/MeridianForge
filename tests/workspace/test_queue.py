from datetime import datetime
from decimal import Decimal

from meridianforge.workspace.models import OpportunityRecord
from meridianforge.workspace.queue import OpportunityQueue


def create_opportunity() -> OpportunityRecord:
    return OpportunityRecord(
        address="456 Oak Ave",
        market="Jacksonville FL",
        purchase_price=Decimal("275000"),
        monthly_rent=Decimal("2400"),
        source="manual",
        created_at=datetime.now(),
    )


def test_queue_add_and_count():

    queue = OpportunityQueue()

    queue.add(create_opportunity())

    assert queue.count() == 1


def test_queue_returns_items():

    queue = OpportunityQueue()

    opportunity = create_opportunity()

    queue.add(opportunity)

    items = queue.all()

    assert items[0] == opportunity


def test_queue_clear():

    queue = OpportunityQueue()

    queue.add(create_opportunity())

    queue.clear()

    assert queue.count() == 0
