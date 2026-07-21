"""
Tests for investor package workflow.
"""

from pathlib import Path

from meridianforge.workflows.investor_package_workflow import (
    InvestorPackageWorkflow,
)


def test_investor_package_workflow_generates_package(
    tmp_path: Path,
) -> None:
    """
    Workflow creates investor package artifacts.
    """

    workflow = InvestorPackageWorkflow()

    package = workflow.generate(
        package_id="TEST001",
        property_name="123 Main Street",
        recommendation="BUY",
        confidence=0.90,
        output_directory=tmp_path,
    )

    assert package.package_id == "TEST001"
    assert package.property_name == "123 Main Street"

    assert (tmp_path / "Decision_Brief.md").exists()

    assert (tmp_path / "Archive_Metadata.json").exists()
