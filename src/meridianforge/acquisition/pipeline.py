"""
Acquisition intelligence pipeline.

MF-334.2

Coordinates:

Opportunity
    ->
Property Adapter
    ->
Underwriting Engine
    ->
Score Engine
    ->
Decision Engine
    ->
Acquisition Result
"""

from meridianforge.acquisition.criteria import (
    AcquisitionCriteria,
)

from meridianforge.acquisition.decision_engine import (
    AcquisitionDecisionEngine,
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

        self.decision_engine = (
            AcquisitionDecisionEngine()
        )

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

        decision = self.decision_engine.evaluate(
            analysis,
            score,
            self.criteria,
        )

        return AcquisitionResult(
            opportunity=opportunity,
            analysis=analysis,
            score=decision.score,
            ranking=0,
            recommendation=decision.status,
            confidence=score / 100,
            warnings=[
                risk.message
                for risk in decision.risks
            ],
        )
