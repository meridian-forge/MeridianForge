from meridianforge.intake.manual_adapter import ManualAdapter
from meridianforge.domain.source import SourceType


def test_manual_adapter():

    source = ManualAdapter().ingest("manual-entry")

    assert source.source_type == SourceType.MANUAL
