"""
Acquisition intelligence pipeline.

MF-333.3

Coordinates acquisition analysis.
"""

from meridianforge.acquisition.criteria import (
    AcquisitionCriteria,
)

from meridianforge.acquisition.decision import (
    AcquisitionDecision,
)

from meridianforge.acquisition.opportunity import (
    Opportunity,
)

from meridianforge.acquisition.property_adapter import (
    AcquisitionPropertyAdapter,
)

from meridianforge.acquisition.result import (
    AcquisitionResult,
)

from meridianforge.acquisition.score import (
    calculate_score,
)

from meridianforge.engine.underwriting_engine import (
    UnderwritingEngine,
)


class AcquisitionPipeline:
    """
    Executes end-to-end acquisition analysis.
    """

    def __init__(
        self,
        criteria: AcquisitionCriteria | None = None,
    ) -> None:

        self.criteria = (
            criteria
            if criteria is not None
            else AcquisitionCriteria()
        )

        self.engine = UnderwritingEngine()
        self.adapter = AcquisitionPropertyAdapter()

    def run(
        self,
        opportunity: Opportunity,
    ) -> AcquisitionResult:
        """
        Analyze one acquisition opportunity.
        """

        property_data = self.adapter.convert(
            opportunity,
        )

        analysis = self.engine.analyze(
            property_data,
        )

        score = calculate_score(
            analysis,
            self.criteria,
        )

        decision = AcquisitionDecision(
            status=(
                "BUY"
                if score >= 70
                else "REVIEW"
            ),
            score=score,
            reasons=[],
        )

        return AcquisitionResult(
            opportunity=opportunity,
            analysis=analysis,
            score=decision.score,
            ranking=0,
            recommendation=decision.status,
            confidence=score / 100,
        )
