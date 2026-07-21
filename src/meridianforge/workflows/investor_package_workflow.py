"""
Investor package workflow.

Orchestrates creation of investor-ready decision packages.
"""

from pathlib import Path

from meridianforge.product.investor_package import InvestorPackage
from meridianforge.reporting.executive_summary import (
    ExecutiveSummaryBuilder,
)
from meridianforge.reporting.package_exporter import (
    PackageExporter,
)
from meridianforge.services.investor_package_builder import (
    InvestorPackageBuilder,
)


class InvestorPackageWorkflow:
    """
    Coordinates investor package generation.
    """

    def __init__(
        self,
        builder: InvestorPackageBuilder | None = None,
        exporter: PackageExporter | None = None,
    ) -> None:
        self.builder = builder or InvestorPackageBuilder()
        self.exporter = exporter or PackageExporter()
        self.summary_builder = ExecutiveSummaryBuilder()

    def generate(
        self,
        package_id: str,
        property_name: str,
        recommendation: str,
        confidence: float,
        output_directory: Path,
    ) -> InvestorPackage:
        """
        Generate a complete investor package.
        """

        package = self.builder.create_package(
            package_id=package_id,
            property_name=property_name,
            recommendation=recommendation,
            confidence=confidence,
            output_directory=output_directory,
        )

        self.summary_builder.build(
            package,
        )

        self.exporter.export(
            package,
            output_directory,
        )

        return package
