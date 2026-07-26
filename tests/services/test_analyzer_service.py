from pathlib import Path
from unittest.mock import Mock

from meridianforge.models.domain.investor_profile import InvestorProfile
from meridianforge.services.analyzer_service import AnalyzerService


def test_analyzer_service_delegates_workflow(tmp_path: Path) -> None:
    input_file = tmp_path / "deal.xlsx"
    input_file.write_text("placeholder")

    opportunity = object()
    expected_result = object()

    file_service = Mock()
    file_service.load.return_value = opportunity

    execution_service = Mock()
    execution_service.execute.return_value = expected_result

    service = AnalyzerService(
        file_service=file_service,
        execution_service=execution_service,
    )

    profile = Mock(spec=InvestorProfile)

    result = service.analyze(
        input_file=input_file,
        investor_profile=profile,
    )

    assert result is expected_result

    file_service.load.assert_called_once_with(str(input_file))

    execution_service.execute.assert_called_once()
