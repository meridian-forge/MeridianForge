from dataclasses import dataclass


@dataclass
class InvestmentReport:

    address: str

    decision: str

    score: float

    cap_rate: float

    dscr: float

    cash_flow: float
