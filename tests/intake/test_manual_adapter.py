from meridianforge.domain.source import SourceType
from meridianforge.intake.manual_adapter import ManualAdapter


def test_manual_adapter():

    source = ManualAdapter().ingest("manual-entry")

    assert source.source_type == SourceType.MANUAL
