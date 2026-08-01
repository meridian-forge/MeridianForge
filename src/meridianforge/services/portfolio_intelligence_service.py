from __future__ import annotations

from meridianforge.portfolio.analysis import (
    PortfolioAnalysisResult,
)
from meridianforge.portfolio.analytics import (
    PortfolioAnalytics,
)
from meridianforge.portfolio.intelligence.action import (
    PortfolioActionEngine,
)
from meridianforge.portfolio.intelligence.decision import (
    PortfolioDecisionEngine,
)
from meridianforge.portfolio.intelligence.health import (
    PortfolioHealthEngine,
)
from meridianforge.portfolio.intelligence.package import (
    InvestorDecisionPackage,
    InvestorDecisionPackageBuilder,
)
from meridianforge.portfolio.intelligence.ranking import (
    PortfolioRankingEngine,
)
from meridianforge.portfolio.intelligence.recommendation import (
    PortfolioRecommendationEngine,
)


class PortfolioIntelligenceService:
    """
    Converts acquisition portfolio analysis into
    investor intelligence.
    """

    def analyze(
        self,
        analysis: PortfolioAnalysisResult,
    ) -> InvestorDecisionPackage:

        analytics = self._build_analytics(
            analysis,
        )

        health = PortfolioHealthEngine.analyze(
            analytics,
        )

        recommendation = PortfolioRecommendationEngine.analyze(
            analytics,
        )

        ranking = PortfolioRankingEngine.rank(
            analytics,
        )

        decision = PortfolioDecisionEngine.evaluate(
            analytics,
        )

        action = PortfolioActionEngine.generate(
            decision,
            recommendation,
        )

        return InvestorDecisionPackageBuilder.build(
            health,
            recommendation,
            ranking,
            decision,
            action,
        )

    @staticmethod
    def _build_analytics(
        analysis: PortfolioAnalysisResult,
    ) -> PortfolioAnalytics:

        deals = analysis.deals

        if not deals:
            return PortfolioAnalytics(
                asset_count=0,
                total_purchase_price=0.0,
                total_monthly_rent=0.0,
                total_monthly_cash_flow=0.0,
                annual_cash_flow=0.0,
                average_cap_rate=0.0,
                average_dscr=0.0,
                portfolio_score=0.0,
            )

        count = len(deals)

        return PortfolioAnalytics(
            asset_count=count,
            total_purchase_price=sum(d.opportunity.purchase_price for d in deals),
            total_monthly_rent=sum(d.opportunity.monthly_rent for d in deals),
            total_monthly_cash_flow=sum(d.opportunity.monthly_cash_flow for d in deals),
            annual_cash_flow=sum(d.opportunity.annual_cash_flow for d in deals),
            average_cap_rate=sum(d.opportunity.cap_rate for d in deals) / count,
            average_dscr=1.5,
            portfolio_score=(analysis.buy_count / count) * 100,
        )
