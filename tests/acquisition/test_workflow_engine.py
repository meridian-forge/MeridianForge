from datetime import datetime

from meridianforge.acquisition.opportunity import (
    Opportunity,
)
from meridianforge.acquisition.result import (
    AcquisitionResult,
)
from meridianforge.acquisition.workflow_engine import (
    WorkflowEngine,
)


def test_workflow_engine_creates_buy_actions():

    opportunity = Opportunity(
        address="123 Main",
        city="Philadelphia",
        state="PA",
        zip_code="19143",
        purchase_price=200000,
        monthly_rent=2000,
        monthly_expenses=800,
        market="Philadelphia",
        source="test",
        created_at=datetime.now(),
    )

    result = AcquisitionResult(
        opportunity=opportunity,
        analysis="analysis",
        score=95,
        ranking=1,
        recommendation="BUY",
        confidence=0.95,
    )

    actions = WorkflowEngine.generate(result)

    assert len(actions) == 3
    assert actions[0].action_type == "REVIEW_FOR_OFFER"
