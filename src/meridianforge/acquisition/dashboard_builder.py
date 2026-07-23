"""
Acquisition dashboard builder.

MF-339.2

Aggregates acquisition intelligence
into portfolio metrics.
"""

from collections.abc import Iterable

from meridianforge.acquisition.dashboard import (
    AcquisitionDashboard,
)

from meridianforge.acquisition.result import (
    AcquisitionResult,
)


class AcquisitionDashboardBuilder:
    """
    Builds portfolio dashboard summaries.
    """

    @staticmethod
    def build(
        results: Iterable[AcquisitionResult],
    ) -> AcquisitionDashboard:
        """
        Aggregate acquisition results.
        """

        results = list(results)

        if not results:
            return AcquisitionDashboard(
                total_deals=0,
                buy_candidates=0,
                review_candidates=0,
                average_score=0,
                average_confidence=0,
                high_risk_count=0,
            )

        total_deals = len(results)

        buy_candidates = sum(
            1
            for result in results
            if result.recommendation == "BUY"
        )

        review_candidates = sum(
            1
            for result in results
            if result.recommendation == "REVIEW"
        )

        average_score = (
            sum(result.score for result in results)
            / total_deals
        )

        average_confidence = (
            sum(result.confidence for result in results)
            / total_deals
        )

        high_risk_count = sum(
            1
            for result in results
            if len(result.warnings) > 0
        )

        return AcquisitionDashboard(
            total_deals=total_deals,
            buy_candidates=buy_candidates,
            review_candidates=review_candidates,
            average_score=average_score,
            average_confidence=average_confidence,
            high_risk_count=high_risk_count,
        )
