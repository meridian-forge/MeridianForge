from __future__ import annotations

from pathlib import Path

from meridianforge.models.domain.investor_profile import InvestorProfile
from meridianforge.services.acquisition_execution_service import (
    AcquisitionExecutionService,
)
from meridianforge.services.evidence_coordinator import EvidenceCoordinator
from meridianforge.services.evidence_opportunity_mapper import (
    EvidenceOpportunityMapper,
)


class MondayEvidenceService:
    """
    SP-490

    Canonical artifact analysis path used by Monday automation.

    Artifact
      ↓
    EvidenceCoordinator
      ↓
    EvidenceOpportunityMapper
      ↓
    AcquisitionExecutionService
    """

    def __init__(
        self,
        execution: AcquisitionExecutionService | None = None,
    ) -> None:
        self.execution = execution or AcquisitionExecutionService()

    def analyze_artifact(
        self,
        artifact: Path,
        investor_profile: InvestorProfile,
    ):
        payload = EvidenceCoordinator.extract(artifact)

        opportunity = EvidenceOpportunityMapper.map(payload)

        return self.execution.execute(
            opportunity,
            investor_profile,
        )
