from meridianforge.intelligence.scoring.engine import (
    IntelligenceScoringEngine,
)
from meridianforge.intelligence.scoring.factors import (
    ScoringFactors,
)


def test_scoring_engine_calculates_weighted_score():
    engine = IntelligenceScoringEngine()

    factors = ScoringFactors(
        cash_flow=10,
        appreciation=8,
        risk=7,
        tax_efficiency=9,
        liquidity=6,
    )

    score = engine.calculate_score(factors)

    assert score > 0
