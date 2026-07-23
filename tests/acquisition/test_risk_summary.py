from meridianforge.acquisition.risk_summary import (
    RiskSummary,
)


def test_risk_summary_creation():

    summary = RiskSummary(
        high=[
            "Negative cash flow",
        ],
        medium=[
            "Low DSCR",
        ],
        low=[
            "Minor maintenance",
        ],
    )

    assert len(summary.high) == 1
    assert len(summary.medium) == 1
    assert len(summary.low) == 1

    assert len(summary.all_risks) == 3
