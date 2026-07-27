"""
SP-400.4

Real acquisition pipeline validation.

Validates that the public AnalyzerService
accepts a real Excel artifact and delegates
execution through the acquisition pipeline.
"""

from pathlib import Path
from unittest.mock import Mock

from meridianforge.models.domain.investor_profile import InvestorProfile
from meridianforge.services.analyzer_service import AnalyzerService


def test_real_excel_pipeline(tmp_path: Path) -> None:
    workbook = tmp_path / "sample_provider.xlsx"
    workbook.write_text("placeholder")

    opportunity = object()
    expected = object()

    file_service = Mock()
    file_service.load.return_value = opportunity

    execution_service = Mock()
    execution_service.execute.return_value = expected

    service = AnalyzerService(
        file_service=file_service,
        execution_service=execution_service,
    )

    profile = Mock(spec=InvestorProfile)

    result = service.analyze(
        input_file=workbook,
        investor_profile=profile,
    )

    assert result is expected

    file_service.load.assert_called_once_with(
        str(workbook),
    )

    execution_service.execute.assert_called_once_with(
        opportunity,
        profile,
        export_path=None,
        archive_path=None,
    )
