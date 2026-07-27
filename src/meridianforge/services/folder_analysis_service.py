"""
Folder analysis service.

SP-411.1

Coordinates batch analysis of investment
artifacts discovered within a folder.

This service bridges the Folder Connector
to the existing AnalyzerService without
duplicating the intake pipeline.
"""

from pathlib import Path

from meridianforge.connectors.folder_connector import FolderConnector
from meridianforge.models.domain.investor_profile import InvestorProfile
from meridianforge.models.results.acquisition_orchestration_result import (
    AcquisitionOrchestrationResult,
)
from meridianforge.opportunity.inbox_status import (
    OpportunityInboxStatus,
)
from meridianforge.services.analyzer_service import AnalyzerService


class FolderAnalysisService:
    """
    Analyze every supported artifact
    within a folder.
    """

    def __init__(
        self,
        connector: FolderConnector | None = None,
        analyzer: AnalyzerService | None = None,
    ) -> None:
        self._connector = connector or FolderConnector()
        self._analyzer = analyzer or AnalyzerService()

    def analyze_folder(
        self,
        folder: str | Path,
        investor_profile: InvestorProfile,
        export_path: Path | None = None,
        archive_path: Path | None = None,
    ) -> list[AcquisitionOrchestrationResult]:
        """
        Analyze all accepted artifacts
        within a folder.
        """

        results: list[AcquisitionOrchestrationResult] = []

        inbox_records = self._connector.import_folder(
            folder,
        )

        for record in inbox_records:

            if record.status != OpportunityInboxStatus.READY:
                continue

            results.append(
                self._analyzer.analyze(
                    input_file=Path(
                        record.source_reference,
                    ),
                    investor_profile=investor_profile,
                    export_path=export_path,
                    archive_path=archive_path,
                )
            )

        return results
