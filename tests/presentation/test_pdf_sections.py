from meridianforge.decision.intelligence.decision_recommendation import (
    DecisionRecommendation,
    RecommendationAction,
)
from meridianforge.models.results.investor_package import (
    InvestorPackage,
)
from meridianforge.presentation.pdf_sections import (
    PDFSectionBuilder,
)
from meridianforge.product.weekly_review import (
    WeeklyInvestorReview,
)


def test_pdf_sections_include_recommendation_content():

    review = WeeklyInvestorReview(
        cards=[],
    )

    recommendation = DecisionRecommendation(
        action=RecommendationAction.BUY,
        confidence=0.90,
        reasons=[
            "Strong cash flow",
        ],
        risks=[
            "Market volatility",
        ],
        next_steps=[
            "Confirm financing",
        ],
    )

    package = InvestorPackage(
        review=review,
        recommendation=recommendation,
    )

    sections = PDFSectionBuilder.build(
        package,
    )

    titles = [section[0] for section in sections]

    content = "\n".join(section[1] for section in sections)

    assert "Executive Summary" in titles
    assert "Investment Recommendation" in titles
    assert "Strengths" in titles
    assert "Risks" in titles
    assert "Next Steps" in titles

    assert "BUY" in content
    assert "Strong cash flow" in content
    assert "Market volatility" in content
