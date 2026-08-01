from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from meridianforge.artifacts.artifact_classifier import ArtifactType
from meridianforge.intake.email_intake_scanner import EmailIntakeScanner
from meridianforge.portfolio.analysis import PortfolioAnalysisResult
from meridianforge.repositories.artifact_repository import ArtifactRepository
from meridianforge.services.portfolio_analyzer_service import (
    PortfolioAnalyzerService,
)


@dataclass(slots=True)
class EmailRoutingResult:
    processed_workbooks: list[Path]
    duplicate_workbooks: list[Path]
    skipped_artifacts: list[Path]
    analyses: list[PortfolioAnalysisResult]

    @property
    def processed_count(self) -> int:
        return len(self.processed_workbooks)

    @property
    def duplicate_count(self) -> int:
        return len(self.duplicate_workbooks)

    @property
    def skipped_count(self) -> int:
        return len(self.skipped_artifacts)


class EmailIntakeRouter:
    """
    MF-507.3

    Routes classified email artifacts into the existing MeridianForge
    analysis pipeline.
    """

    def __init__(
        self,
        scanner: EmailIntakeScanner | None = None,
        repository: ArtifactRepository | None = None,
        analyzer: PortfolioAnalyzerService | None = None,
    ) -> None:
        self.scanner = scanner or EmailIntakeScanner()
        self.repository = repository or ArtifactRepository()
        self.analyzer = analyzer or PortfolioAnalyzerService()

    def route(
        self,
        inbox_directory: Path,
    ) -> EmailRoutingResult:
        scan = self.scanner.scan(
            inbox_directory,
        )

        processed: list[Path] = []
        duplicates: list[Path] = []
        skipped: list[Path] = []
        analyses: list[PortfolioAnalysisResult] = []

        for artifact in scan.artifacts:
            if artifact.artifact_type != ArtifactType.PORTFOLIO_WORKBOOK:
                skipped.append(
                    artifact.path,
                )
                continue

            before = len(self.repository.all())

            self.repository.register(
                artifact.path,
                source="email",
            )

            after = len(self.repository.all())

            if after == before:
                duplicates.append(
                    artifact.path,
                )
                continue

            processed.append(
                artifact.path,
            )

            try:
                analyses.append(
                    self.analyzer.analyze_file(
                        artifact.path,
                    )
                )
            except Exception:
                # Invalid or unreadable workbook: keep the artifact
                # processed but do not fail the intake workflow.
                skipped.append(
                    artifact.path,
                )

        return EmailRoutingResult(
            processed_workbooks=processed,
            duplicate_workbooks=duplicates,
            skipped_artifacts=skipped,
            analyses=analyses,
        )
