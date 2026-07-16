"""
Batch analysis result tests.
"""

from meridianforge.models.results.batch_analysis_result import (
    BatchAnalysisResult,
)


def test_batch_analysis_result_creation() -> None:
    """
    Verify batch result stores summary values.
    """

    result = BatchAnalysisResult(
        ranked_deals=[],
        total_analyzed=10,
        qualified_count=4,
        rejected_count=6,
        average_score=78.5,
        average_dscr=1.32,
    )

    assert result.total_analyzed == 10
    assert result.qualified_count == 4
    assert result.rejected_count == 6
    assert result.average_score == 78.5
    assert result.average_dscr == 1.32
