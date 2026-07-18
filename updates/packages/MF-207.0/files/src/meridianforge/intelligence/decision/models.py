from dataclasses import dataclass
from enum import StrEnum


class DecisionType(StrEnum):
    BUY = "BUY"
    WATCH = "WATCH"
    PASS = "PASS"


class RiskLevel(StrEnum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"


@dataclass
class InvestmentDecision:
    property_id: str
    decision: DecisionType
    score: float
    confidence: str
    risk_level: RiskLevel
    rationale: str
    recommended_action: str
