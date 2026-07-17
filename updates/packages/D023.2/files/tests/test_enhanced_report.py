from meridianforge.models.results.acquisition_assessment import (
    AcquisitionAssessment,
)

from meridianforge.models.results.acquisition_result import (
    AcquisitionResult,
)

from meridianforge.reports.acquisition_report import (
    AcquisitionReport,
)


def test_enhanced_report_content() -> None:

    assessment = AcquisitionAssessment(
        purchase_price=215000,
        monthly_cash_flow=300,
        dscr=1.25,
        cap_rate=0.065,
    )

    result = AcquisitionResult(
        recommendation="BUY",
        confidence=0.90,
        metadata={
            "assessment": assessment,
        },
    )

    report = AcquisitionReport.generate(
        result
    )

    assert "INVESTMENT ANALYSIS REPORT" in report
    assert "FINANCIAL PERFORMANCE" in report
    assert "BUY" in report
