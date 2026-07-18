from meridianforge.intelligence.decision import (
    DecisionEngine,
    DecisionType,
    RiskLevel,
)


def test_buy_decision():
    engine = DecisionEngine()

    result = engine.evaluate(
        property_id="PROP-001",
        score=85,
        risk_level=RiskLevel.MEDIUM,
    )

    assert result.decision == DecisionType.BUY
    assert result.confidence == "HIGH"


def test_pass_decision():
    engine = DecisionEngine()

    result = engine.evaluate(
        property_id="PROP-002",
        score=40,
        risk_level=RiskLevel.HIGH,
    )

    assert result.decision == DecisionType.PASS
    assert result.confidence == "LOW"
