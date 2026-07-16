"""
Analysis workflow result model.

Represents the complete output of an investment analysis run.
"""

from dataclasses import dataclass, field

from meridianforge.models.results.import_quality_report import (
    ImportQualityReport,
)


@dataclass(slots=True)
class AnalysisWorkflowResult:
    """
    Complete analysis workflow output.
    """

    assets_analyzed: int

    ranked_results: list[dict[str, object]] = field(
        default_factory=list,
    )

    import_quality: ImportQualityReport | None = None
