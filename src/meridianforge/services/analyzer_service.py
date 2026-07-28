"""
End-to-end analyzer service.

Coordinates acquisition execution and
investor package generation.

MF-354.1
"""

from pathlib import Path

from meridianforge.models.domain.investor_profile import (
    InvestorProfile,
)
from meridianforge.models.results.acquisition_orchestration_result import (
    AcquisitionOrchestrationResult,
)
from meridianforge.services.acquisition_execution_service import (
    AcquisitionExecutionService,
)
from meridianforge.services.acquisition_file_service import (
    AcquisitionFileService,
)


class AnalyzerService:
    """
    Public application service.

    Executes the complete MeridianForge investment
    analysis workflow from a user-supplied file.
    """

    def __init__(
        self,
        file_service: AcquisitionFileService | None = None,
        execution_service: AcquisitionExecutionService | None = None,
    ) -> None:
        self.file_service = file_service or AcquisitionFileService()
        self.execution_service = execution_service or AcquisitionExecutionService()

    def analyze(
        self,
        input_file: Path,
        investor_profile: InvestorProfile,
        export_path: Path | None = None,
        archive_path: Path | None = None,
    ) -> AcquisitionOrchestrationResult:
        """
        Execute the complete investment analysis workflow.

        Parameters
        ----------
        input_file:
            Excel/CSV/property file to analyze.

        investor_profile:
            Investor preferences used during analysis.

        export_path:
            Optional report output directory.

        archive_path:
            Optional archive directory.
        """

        if not input_file.exists():
            raise FileNotFoundError(f"Input file does not exist: {input_file}")

        opportunity = self.file_service.load(
            str(input_file),
        )

        return self.execution_service.execute(
            opportunity,
            investor_profile,
            export_path=export_path,
            archive_path=archive_path,
        )
