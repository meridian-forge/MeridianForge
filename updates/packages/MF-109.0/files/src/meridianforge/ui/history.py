from dataclasses import dataclass


@dataclass
class AnalysisHistory:

    address: str
    decision: str
    score: float


class HistoryStore:

    def __init__(self) -> None:

        self.items: list[AnalysisHistory] = []


    def add(
        self,
        item: AnalysisHistory,
    ) -> None:

        self.items.append(
            item
        )


    def all(
        self,
    ) -> list[AnalysisHistory]:

        return self.items
