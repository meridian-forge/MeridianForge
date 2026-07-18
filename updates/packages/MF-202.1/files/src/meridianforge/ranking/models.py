from dataclasses import dataclass


@dataclass
class RankingResult:

    opportunity_file: str

    score: float

    rank: int = 0
