from meridianforge.acquisition.thesis import (
    InvestmentThesis,
)


def test_investment_thesis_creation():

    thesis = InvestmentThesis(
        property_address="123 Main, Philadelphia PA",
        recommendation="BUY",
        score=95,
        confidence=0.95,
        summary="Strong acquisition candidate.",
        highlights=[
            "DSCR exceeds target",
        ],
        risks=[],
    )

    assert thesis.recommendation == "BUY"
    assert thesis.score == 95
    assert len(thesis.highlights) == 1
