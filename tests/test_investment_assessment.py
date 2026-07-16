"""
Investment assessment engine tests.
"""

from meridianforge.engine.investment_assessment import (
    InvestmentAssessmentEngine,
)


def test_investment_assessment_imports() -> None:
    assert InvestmentAssessmentEngine is not None
