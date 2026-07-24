from meridianforge.dashboard.command.summary import (
    CommandCenterSummary,
)


def test_summary_model():

    summary = CommandCenterSummary(
        health_status="STRONG",
        portfolio_score=95,
        cash_flow_summary="$5,000/month",
        alert_count=1,
        action_count=2,
    )

    assert summary.health_status == "STRONG"

    assert summary.alert_count == 1
