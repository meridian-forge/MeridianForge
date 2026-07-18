from meridianforge.reports.generator import (
    ReportGenerator,
)
from meridianforge.reports.models import (
    InvestmentReport,
)


def test_report():

    report = InvestmentReport(
        address="123 Main",
        decision="BUY",
        score=90,
        cap_rate=0.06,
        dscr=1.5,
        cash_flow=500,
    )

    result = ReportGenerator().create_summary(report)

    assert result["decision"] == "BUY"
    assert result["score"] == 90
