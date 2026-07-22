from meridianforge.acquisition.report import (
    AcquisitionReport,
)

from meridianforge.acquisition.thesis import (
    InvestmentThesis,
)


def test_acquisition_report_creation():

    thesis = InvestmentThesis(
        property_address="123 Main",
        recommendation="BUY",
        score=95,
        confidence=0.95,
        summary="Strong candidate",
        highlights=[
            "Good DSCR",
        ],
        risks=[],
    )

    report = AcquisitionReport(
        property_address="123 Main",
        recommendation="BUY",
        score=95,
        confidence=0.95,
        purchase_price=200000,
        monthly_rent=2000,
        annual_cash_flow=6000,
        cap_rate=0.06,
        cash_on_cash_return=0.10,
        dscr=1.5,
        thesis=thesis,
    )

    assert report.recommendation == "BUY"
    assert report.cap_rate == 0.06
    assert report.thesis.summary == "Strong candidate"
