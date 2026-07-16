"""
Analysis workflow tests.
"""

from meridianforge.services.analysis_workflow import (
    AnalysisWorkflow,
)


def test_analysis_workflow_processes_records() -> None:

    workflow = AnalysisWorkflow()

    result = workflow.analyze_records(
        [
            {
                "Purchase Price": 250000,
                "Monthly Rent": 2200,
            }
        ],
        asset_type="REAL_ESTATE",
    )

    assert result.assets_analyzed == 1

    assert result.import_quality is not None

    assert len(result.ranked_results) == 1
