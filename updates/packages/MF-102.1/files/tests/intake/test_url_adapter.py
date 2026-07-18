from meridianforge.intake.url_adapter import URLAdapter
from meridianforge.domain.source import SourceType


def test_url_adapter():

    source = URLAdapter().ingest(
        "https://example.com/property"
    )

    assert source.source_type == SourceType.URL
