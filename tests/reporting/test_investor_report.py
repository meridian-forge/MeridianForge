from meridianforge.reporting.investor_report import (
    InvestorReportBuilder,
)


class Brief:

    total_analyzed = 3
    buy_candidates = ["Property A"]
    watch_candidates = ["Property B"]
    rejected_candidates = ["Property C"]


def test_investor_report_builder():

    builder = InvestorReportBuilder()

    report = builder.build(Brief())

    output = report.render()

    assert "Meridian Forge Weekly Opportunity Brief" in output

    assert "Property A" in output
    assert "Property B" in output
