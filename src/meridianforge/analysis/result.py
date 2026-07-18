from dataclasses import dataclass


@dataclass
class AnalysisResult:
    cash_flow_monthly: float
    cap_rate: float
    cash_on_cash_return: float
    dscr: float
    score: float
