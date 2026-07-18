from dataclasses import dataclass


@dataclass
class AcquisitionDecision:

    status: str
    score: float
    reasons: list[str]
