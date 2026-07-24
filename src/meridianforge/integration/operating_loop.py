"""
MeridianForge operating loop.

MF-346.3

Coordinates acquisition decisions,
portfolio updates, analytics, and
investor lifecycle evaluation.
"""

from dataclasses import dataclass

from meridianforge.acquisition.result import (
    AcquisitionResult,
)
from meridianforge.integration.acquisition_portfolio_bridge import (
    AcquisitionPortfolioBridge,
)
from meridianforge.integration.lifecycle import (
    InvestorLifecycleEngine,
    InvestorLifecycleState,
)
from meridianforge.portfolio.analytics import (
    PortfolioAnalyticsEngine,
)
from meridianforge.portfolio.portfolio import (
    Portfolio,
)


@dataclass(slots=True)
class InvestorOperatingState:
    """
    Complete investor operating state.
    """

    portfolio_name: str

    asset_count: int

    lifecycle: InvestorLifecycleState


class MeridianForgeOperatingLoop:
    """
    End-to-end investor workflow coordinator.
    """

    @staticmethod
    def process_acquisition(
        portfolio: Portfolio,
        result: AcquisitionResult,
    ) -> InvestorOperatingState:
        """
        Process approved acquisition through
        the investor operating loop.
        """

        AcquisitionPortfolioBridge.add_to_portfolio(
            portfolio,
            result,
        )

        analytics = PortfolioAnalyticsEngine.analyze(
            portfolio,
        )

        lifecycle = InvestorLifecycleEngine.evaluate(
            portfolio,
            analytics,
        )

        return InvestorOperatingState(
            portfolio_name=portfolio.name,
            asset_count=portfolio.asset_count,
            lifecycle=lifecycle,
        )
