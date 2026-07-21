"""
End-to-end investor package generation tests.
"""

from pathlib import Path

from meridianforge.reporting.package_exporter import (
    PackageExporter,
)
from meridianforge.services.investor_package_builder import (
    InvestorPackageBuilder,
)


def test_investor_package_generation(
    tmp_path: Path,
) -> None:
    """
    Verify investor package creation workflow.
    """

    package = InvestorPackageBuilder().create_package(
        package_id="TEST001",
        property_name="Sample Rental Property",
        recommendation="BUY",
        confidence=0.92,
        output_directory=tmp_path,
    )

    package_directory = tmp_path / "MeridianForge_Deal_Package_TEST001"

    files = PackageExporter().export(
        package,
        package_directory,
    )

    assert len(files) == 2

    assert (package_directory / "Decision_Brief.md").exists()

    assert (package_directory / "Archive_Metadata.json").exists()
