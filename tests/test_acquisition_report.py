from meridianforge.models.results.acquisition_assessment import (
    AcquisitionAssessment,
)
from meridianforge.models.results.acquisition_result import (
    AcquisitionResult,
)
from meridianforge.reports.acquisition_report import (
    AcquisitionReport,
)


def test_report_generation() -> None:

    assessment = AcquisitionAssessment(
        purchase_price=215000,
        dscr=1.35,
        cap_rate=0.07,
        monthly_cash_flow=350,
    )

    result = AcquisitionResult(
        confidence=0.90,
        recommendation="BUY",
        assets_analyzed=1,
        metadata={
            "assessment": assessment,
        },
    )

    report = AcquisitionReport.generate(
        result,
    )

    assert "BUY" in report
    assert "215,000" in report
    assert "1.35" in report
