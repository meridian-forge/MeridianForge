from typing import Any


class OpportunityRepository:
    """
    In-memory repository for investment opportunities.

    Initial implementation provides the repository
    abstraction that later storage engines can replace.
    """

    def __init__(
        self,
        opportunities: list[Any] | None = None,
    ) -> None:
        self._opportunities: list[Any] = (
            opportunities or []
        )

    def add(
        self,
        opportunity: Any,
    ) -> None:
        self._opportunities.append(
            opportunity
        )

    def get_all(self) -> list[Any]:
        return list(
            self._opportunities
        )

    def count(self) -> int:
        return len(
            self._opportunities
        )
