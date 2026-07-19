from meridianforge.workspace.models import OpportunityRecord


class OpportunityQueue:
    """
    Stores investment opportunities awaiting analysis.

    Phase 1 implementation:
    in-memory queue.

    Future:
    database-backed persistence.
    """

    def __init__(self) -> None:
        self._items: list[OpportunityRecord] = []

    def add(self, opportunity: OpportunityRecord) -> None:
        self._items.append(opportunity)

    def all(self) -> list[OpportunityRecord]:
        return list(self._items)

    def count(self) -> int:
        return len(self._items)

    def clear(self) -> None:
        self._items.clear()
