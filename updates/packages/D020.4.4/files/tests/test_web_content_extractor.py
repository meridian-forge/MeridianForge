from meridianforge.extractors.web_content_extractor import (
    WebContentExtractor,
)


def test_web_content_extractor() -> None:

    document = WebContentExtractor.extract(
        "https://jwb.com/property/123",
        "Jacksonville rental $215000",
    )

    assert document.source_type == "WEB"
    assert document.provider == "jwb.com"
