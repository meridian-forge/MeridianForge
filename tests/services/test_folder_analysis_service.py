from pathlib import Path
from unittest.mock import Mock

from meridianforge.opportunity.inbox_record import OpportunityInboxRecord
from meridianforge.opportunity.inbox_status import OpportunityInboxStatus
from meridianforge.services.folder_analysis_service import (
    FolderAnalysisService,
)


def test_folder_analysis_service_analyzes_ready_records() -> None:
    connector = Mock()

    record1 = OpportunityInboxRecord(
        source="FOLDER",
        source_reference="deal1.xlsx",
        duplicate_hash="1",
    )
    record1.status = OpportunityInboxStatus.READY

    record2 = OpportunityInboxRecord(
        source="FOLDER",
        source_reference="deal2.xlsx",
        duplicate_hash="2",
    )
    record2.status = OpportunityInboxStatus.READY

    connector.import_folder.return_value = [
        record1,
        record2,
    ]

    analyzer = Mock()
    analyzer.analyze.side_effect = [
        "result1",
        "result2",
    ]

    service = FolderAnalysisService(
        connector=connector,
        analyzer=analyzer,
    )

    profile = Mock()

    results = service.analyze_folder(
        folder=Path("/tmp"),
        investor_profile=profile,
    )

    assert results == [
        "result1",
        "result2",
    ]

    assert analyzer.analyze.call_count == 2
