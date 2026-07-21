"""
End-to-end validation for investor package workflow.
"""

from pathlib import Path

from meridianforge.workflows.investor_package_workflow import (
    InvestorPackageWorkflow,
)


def test_investor_package_workflow_generates_complete_package(
    tmp_path: Path,
) -> None:
    """
    Validate full investor package generation flow.
    """

    workflow = InvestorPackageWorkflow()

    package = workflow.generate(
        package_id="TEST-001",
        property_name="123 Main Street",
        recommendation="BUY",
        confidence=0.92,
        output_directory=tmp_path,
    )

    assert package.package_id == "TEST-001"
    assert package.property_name == "123 Main Street"
    assert package.recommendation == "BUY"
    assert package.confidence == 0.92

    decision_brief = tmp_path / "Decision_Brief.md"
    metadata = tmp_path / "Archive_Metadata.json"

    assert decision_brief.exists()
    assert metadata.exists()
