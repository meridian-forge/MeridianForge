from meridianforge.portfolio.operations.action import (
    PortfolioAction,
)
from meridianforge.portfolio.operations.queue import (
    PortfolioActionQueue,
)


def test_action_queue_tracks_pending_actions():

    queue = PortfolioActionQueue()

    queue.add(
        PortfolioAction(
            action_type="DSCR_WARNING",
            description="Review debt coverage",
            priority="HIGH",
        )
    )

    assert queue.count == 1
    assert len(queue.pending()) == 1
