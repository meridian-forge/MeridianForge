"""
Tests for investment thesis builder.
"""

from datetime import datetime

from meridianforge.product.investor_package import (
    InvestorPackage,
)
from meridianforge.services.investment_thesis_builder import (
    InvestmentThesisBuilder,
)


def test_builder_creates_investment_thesis() -> None:
    """
    Validate thesis generation.
    """

    package = InvestorPackage(
        package_id="TEST-001",
        property_name="Sample Property",
        recommendation="BUY",
        confidence=0.90,
        created_at=datetime.utcnow(),
    )

    thesis = InvestmentThesisBuilder().build(
        package,
    )

    assert thesis.recommendation == "BUY"
    assert thesis.confidence == 0.90
    assert len(thesis.strengths) == 2
    assert thesis.investor_fit != ""
