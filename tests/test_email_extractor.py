from meridianforge.extractors.email_extractor import (
    EmailExtractor,
)


def test_email_extractor() -> None:

    document = EmailExtractor.extract(
        sender="JWB Capital",
        subject="Featured Property",
        body="<html>Rental $1850</html>",
    )

    assert document.source_type == "EMAIL"
    assert document.provider == "JWB Capital"
    assert "Rental" in document.content
