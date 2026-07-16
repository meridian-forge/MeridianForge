from meridianforge.models.domain.source_document import (
    SourceDocument,
)


def test_source_document_creation() -> None:

    document = SourceDocument(
        source_type="EMAIL",
        provider="JWB Capital",
        content="Property opportunity",
    )

    assert document.source_type == "EMAIL"
    assert document.provider == "JWB Capital"
