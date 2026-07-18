from pathlib import Path

from meridianforge.intake.source_classifier import classify_file
from meridianforge.intake.models import SourceCategory


def test_detect_turnkey_source() -> None:
    result = classify_file(Path("jwb_property.xlsx"))

    assert result.category == SourceCategory.TURNKEY_PROVIDER
