"""
Portfolio intelligence service integration tests.

MF-502
"""

from datetime import datetime

from meridianforge.acquisition.opportunity import Opportunity
from meridianforge.portfolio.analysis import (
    PortfolioAnalysisResult,
    PortfolioDealResult,
)
from meridianforge.product.decision_card import InvestorDecisionCard
from meridianforge.product.weekly_review import WeeklyInvestorReview
from meridianforge.services.portfolio_intelligence_service import (
    PortfolioIntelligenceService,
)


def create_opportunity() -> Opportunity:
    return Opportunity(
        address="123 Main Street",
        city="Philadelphia",
        state="PA",
        zip_code="19143",
        purchase_price=200000,
        monthly_rent=2200,
        monthly_expenses=800,
        market="Philadelphia",
        source="test",
        created_at=datetime.now(),
    )


def create_review() -> WeeklyInvestorReview:
    return WeeklyInvestorReview(
        cards=[
            InvestorDecisionCard(
                rank=1,
                property_address="123 Main Street",
                recommendation="BUY",
                confidence=0.90,
                strengths=[
                    "Strong cash flow",
                ],
                risks=[],
            )
        ]
    )


def test_portfolio_intelligence_creates_package():

    analysis = PortfolioAnalysisResult(
        deals=[
            PortfolioDealResult(
                row_number=2,
                opportunity=create_opportunity(),
                review=create_review(),
            )
        ]
    )

    service = PortfolioIntelligenceService()

    package = service.analyze(
        analysis,
    )

    summary = package.summary()

    assert summary["recommendation"] is not None

    assert summary["decision"] is not None

    assert summary["action"] is not None
