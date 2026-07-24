"""
Portfolio action routing engine.

MF-347.3
"""

from meridianforge.portfolio.operations.action import (
    PortfolioAction,
)


class PortfolioActionRouter:
    """
    Routes actions into operating categories.
    """

    def route(
        self,
        action: PortfolioAction,
    ) -> str:
        """
        Determine operational category.
        """

        mapping = {
            "REFINANCE_REVIEW": "FINANCE",
            "DSCR_WARNING": "RISK",
            "ACQUISITION_REVIEW": "ACQUISITION",
            "PORTFOLIO_REVIEW": "STRATEGY",
        }

        return mapping.get(
            action.action_type,
            "GENERAL",
        )
