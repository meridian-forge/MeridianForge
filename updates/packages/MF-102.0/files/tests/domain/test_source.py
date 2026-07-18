from meridianforge.domain.source import Source, SourceType


def test_source():

    source = Source(
        SourceType.URL,
        "https://example.com"
    )

    assert source.validate()
