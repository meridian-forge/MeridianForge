"""
Acquisition intelligence pipeline.

MF-335.3

Coordinates acquisition analysis.

Opportunity
    ->
Canonical Property
    ->
Underwriting Engine
    ->
Decision Engine
    ->
Investment Thesis
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

from meridianforge.acquisition.thesis_generator import (
    InvestmentThesisGenerator,
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

        self.criteria = criteria if criteria is not None else AcquisitionCriteria()

        self.engine = UnderwritingEngine()
        self.adapter = AcquisitionPropertyAdapter()
        self.decision_engine = AcquisitionDecisionEngine()

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

        result = AcquisitionResult(
            opportunity=opportunity,
            analysis=analysis,
            score=decision.score,
            ranking=0,
            recommendation=decision.status,
            confidence=score / 100,
            warnings=[risk.message for risk in decision.risks],
        )

        return AcquisitionResult(
            opportunity=result.opportunity,
            analysis=result.analysis,
            score=result.score,
            ranking=result.ranking,
            recommendation=result.recommendation,
            confidence=result.confidence,
            warnings=result.warnings,
            thesis=InvestmentThesisGenerator.generate(
                result,
            ),
        )
