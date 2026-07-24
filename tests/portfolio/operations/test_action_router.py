from meridianforge.portfolio.operations.action import (
    PortfolioAction,
)
from meridianforge.portfolio.operations.action_router import (
    PortfolioActionRouter,
)


def test_action_router_maps_refinance():

    router = PortfolioActionRouter()

    action = PortfolioAction(
        action_type="REFINANCE_REVIEW",
        description="Review refinance",
        priority="HIGH",
    )

    category = router.route(
        action,
    )

    assert category == "FINANCE"
