import json
from pathlib import Path

from meridianforge.product.decision_card import (
    InvestorDecisionCard,
)
from meridianforge.product.weekly_review import (
    WeeklyInvestorReview,
)
from meridianforge.reporting.monday_dashboard_builder import (
    MondayDashboardBuilder,
)
from meridianforge.reporting.monday_dashboard_json import (
    MondayDashboardJSONExporter,
)


def test_dashboard_json_export(
    tmp_path: Path,
):

    review = WeeklyInvestorReview(
        cards=[
            InvestorDecisionCard(
                rank=1,
                property_address="123 Main St",
                recommendation="BUY",
                confidence=0.92,
            )
        ]
    )

    dashboard = MondayDashboardBuilder.build(review)

    output = tmp_path / "Dashboard.json"

    MondayDashboardJSONExporter.export(
        dashboard,
        output,
    )

    assert output.exists()

    data = json.loads(output.read_text())

    assert data["summary"]["buy_count"] == 1
    assert data["top_opportunity"]["address"] == "123 Main St"
