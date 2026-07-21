"""
Tests for investor package exporting.
"""

import json
from datetime import datetime
from pathlib import Path

from meridianforge.product.investor_package import (
    InvestorPackage,
)
from meridianforge.reporting.package_exporter import (
    PackageExporter,
)


def test_package_export_creates_files(
    tmp_path: Path,
) -> None:
    """
    Exporter should create investor package files.
    """

    package = InvestorPackage(
        package_id="PKG-100",
        property_name="456 Oak Avenue",
        recommendation="buy",
        confidence=0.85,
        created_at=datetime(2026, 7, 21),
    )

    files = PackageExporter().export(
        package,
        tmp_path,
    )

    assert len(files) == 2

    decision_brief = tmp_path / "Decision_Brief.md"
    metadata = tmp_path / "Archive_Metadata.json"

    assert decision_brief.exists()
    assert metadata.exists()

    content = decision_brief.read_text(
        encoding="utf-8",
    )

    assert "456 Oak Avenue" in content
    assert "BUY" in content

    data = json.loads(
        metadata.read_text(
            encoding="utf-8",
        )
    )

    assert data["package_id"] == "PKG-100"
    assert data["property_name"] == "456 Oak Avenue"
