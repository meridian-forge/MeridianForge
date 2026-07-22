"""
Tests for acquisition package workflow.
"""

from datetime import datetime
from pathlib import Path

from meridianforge.acquisition.opportunity import Opportunity
from meridianforge.intelligence.investor_profile import (
    InvestorProfile,
)
from meridianforge.workflows.acquisition_package_workflow import (
    AcquisitionPackageWorkflow,
)


def test_acquisition_package_workflow_generates_package(
    tmp_path: Path,
) -> None:
    """
    Validate end-to-end acquisition package generation.
    """

    opportunity = Opportunity(
        address="123 Main Street",
        city="Jacksonville",
        state="FL",
        zip_code="32210",
        purchase_price=200000,
        monthly_rent=1800,
        monthly_expenses=700,
        market="Jacksonville",
        source="CSV",
        created_at=datetime(2026, 7, 22),
    )

    investor = InvestorProfile(
        name="Cash Flow Investor",
        strategy="CASH_FLOW",
        risk_tolerance="MODERATE",
        target_cash_flow=0.50,
        appreciation_priority=0.20,
        tax_focus=0.20,
    )

    package = AcquisitionPackageWorkflow().generate(
        opportunity=opportunity,
        investor=investor,
        output_directory=tmp_path,
    )

    assert package.property_name == "123 Main Street"
    assert package.recommendation == "BUY"

    assert (tmp_path / "Decision_Brief.md").exists()
    assert (tmp_path / "Investment_Thesis.md").exists()
    assert (tmp_path / "Archive_Metadata.json").exists()
