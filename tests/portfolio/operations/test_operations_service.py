from meridianforge.portfolio.operations.action import (
    PortfolioAction,
)
from meridianforge.portfolio.operations.operations_service import (
    PortfolioOperationsService,
)


def test_operations_service_submits_action():

    service = PortfolioOperationsService()

    action = PortfolioAction(
        action_type="DSCR_WARNING",
        description="Review debt coverage",
        priority="HIGH",
    )

    category = service.submit(
        action,
    )

    assert category == "RISK"

    assert service.queue.count == 1


def test_operations_service_completes_action():

    service = PortfolioOperationsService()

    action = PortfolioAction(
        action_type="ACQUISITION_REVIEW",
        description="Review property",
        priority="HIGH",
    )

    service.submit(
        action,
    )

    service.complete(
        action,
    )

    assert action.status == "COMPLETED"
