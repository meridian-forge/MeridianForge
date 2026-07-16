"""
Investment pipeline result.

Represents complete investment decision output.
"""

from dataclasses import dataclass, field

from meridianforge.models.results.import_quality_report import (
    ImportQualityReport,
)
from meridianforge.models.results.ranked_deal import (
    RankedDeal,
)


@dataclass(slots=True)
class InvestmentPipelineResult:
    """
    Complete investment pipeline output.
    """

    ranked_deals: list[RankedDeal] = field(
        default_factory=list,
    )

    import_quality: ImportQualityReport | None = None
