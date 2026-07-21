"""
Investor package builder service.

Creates investor decision packages from generated artifacts.
"""

from datetime import datetime
from pathlib import Path

from meridianforge.product.investor_package import (
    InvestorPackage,
    InvestorPackageArtifact,
)


class InvestorPackageBuilder:
    """
    Build investor decision packages.
    """

    def create_package(
        self,
        package_id: str,
        property_name: str,
        recommendation: str,
        confidence: float,
        output_directory: Path,
    ) -> InvestorPackage:
        """
        Create a new investor package container.
        """

        package_directory = (
            output_directory
            / f"MeridianForge_Deal_Package_{package_id}"
        )

        package_directory.mkdir(
            parents=True,
            exist_ok=True,
        )

        package = InvestorPackage(
            package_id=package_id,
            property_name=property_name,
            recommendation=recommendation,
            confidence=confidence,
            created_at=datetime.utcnow(),
        )

        package.add_artifact(
            InvestorPackageArtifact(
                name="package_directory",
                location=package_directory,
                artifact_type="directory",
            )
        )

        return package
