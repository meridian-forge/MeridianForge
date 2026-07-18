from meridianforge.intake.pdf_adapter import PDFAdapter
from meridianforge.intake.router import IntakeRouter
from meridianforge.intake.url_adapter import URLAdapter


def test_router_url():

    assert isinstance(
        IntakeRouter().select("https://example.com"),
        URLAdapter,
    )


def test_router_pdf():

    assert isinstance(
        IntakeRouter().select("property.pdf"),
        PDFAdapter,
    )
