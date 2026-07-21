"""
Tests for executive summary generation.
"""

from datetime import datetime
from pathlib import Path

from meridianforge.product.investor_package import (
    InvestorPackage,
    InvestorPackageArtifact,
)
from meridianforge.reporting.executive_summary import (
    ExecutiveSummaryBuilder,
)


def test_build_executive_summary() -> None:
    """
    Executive summary should contain core package information.
    """

    package = InvestorPackage(
        package_id="PKG-001",
        property_name="123 Main Street",
        recommendation="buy",
        confidence=0.92,
        created_at=datetime(2026, 7, 21),
    )

    package.add_artifact(
        InvestorPackageArtifact(
            name="Investor Report",
            location=Path("reports/investor_report.md"),
            artifact_type="markdown",
        )
    )

    summary = ExecutiveSummaryBuilder().build(package)

    assert "123 Main Street" in summary
    assert "BUY" in summary
    assert "92.0%" in summary
    assert "Artifacts Included: 1" in summary
