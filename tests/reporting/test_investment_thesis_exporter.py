"""
Tests for investment thesis exporter.
"""

from pathlib import Path

from meridianforge.intelligence.investment_thesis import (
    InvestmentThesis,
)
from meridianforge.reporting.investment_thesis_exporter import (
    InvestmentThesisExporter,
)


def test_investment_thesis_exporter_creates_file(
    tmp_path: Path,
) -> None:
    """
    Validate thesis artifact generation.
    """

    thesis = InvestmentThesis(
        recommendation="BUY",
        confidence=0.90,
        rationale="Strong acquisition opportunity",
        investor_fit="Cash flow investor",
    )

    thesis.add_strength(
        "Strong rental economics",
    )

    thesis.add_risk(
        "Market volatility",
    )

    file_path = InvestmentThesisExporter().export(
        thesis,
        tmp_path,
    )

    assert file_path.exists()
    assert file_path.name == "Investment_Thesis.md"

    content = file_path.read_text()

    assert "BUY" in content
    assert "Strong rental economics" in content
