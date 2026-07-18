from meridianforge.domain.source import SourceType
from meridianforge.intake.url_adapter import URLAdapter


def test_url_adapter():

    source = URLAdapter().ingest("https://example.com/property")

    assert source.source_type == SourceType.URL
