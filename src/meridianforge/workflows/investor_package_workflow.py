"""
Investor package workflow.

Orchestrates creation of investor-ready decision packages.
"""

from pathlib import Path

from meridianforge.intelligence.investor_fit_engine import (
    InvestorFitEngine,
)
from meridianforge.intelligence.investor_profile import (
    InvestorProfile,
)
from meridianforge.product.investor_package import (
    InvestorPackage,
)
from meridianforge.reporting.executive_summary import (
    ExecutiveSummaryBuilder,
)
from meridianforge.reporting.investment_thesis_exporter import (
    InvestmentThesisExporter,
)
from meridianforge.reporting.package_exporter import (
    PackageExporter,
)
from meridianforge.services.investment_thesis_builder import (
    InvestmentThesisBuilder,
)
from meridianforge.services.investor_package_builder import (
    InvestorPackageBuilder,
)
from meridianforge.services.personalized_thesis_builder import (
    PersonalizedThesisBuilder,
)


class InvestorPackageWorkflow:
    """
    Coordinates investor package generation.
    """

    def __init__(
        self,
        builder: InvestorPackageBuilder | None = None,
        exporter: PackageExporter | None = None,
        thesis_builder: InvestmentThesisBuilder | None = None,
        thesis_exporter: InvestmentThesisExporter | None = None,
    ) -> None:
        self.builder = builder or InvestorPackageBuilder()
        self.exporter = exporter or PackageExporter()
        self.thesis_builder = thesis_builder or InvestmentThesisBuilder()
        self.thesis_exporter = thesis_exporter or InvestmentThesisExporter()
        self.summary_builder = ExecutiveSummaryBuilder()
        self.fit_engine = InvestorFitEngine()
        self.personalized_builder = PersonalizedThesisBuilder()

    def generate(
        self,
        package_id: str,
        property_name: str,
        recommendation: str,
        confidence: float,
        output_directory: Path,
        investor_profile: InvestorProfile | None = None,
        cash_flow_score: float = 0.0,
        appreciation_score: float = 0.0,
        tax_score: float = 0.0,
        risk_score: float = 0.0,
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

        package.investment_thesis = self.thesis_builder.build(
            package,
        )

        if investor_profile:

            fit_score = self.fit_engine.evaluate(
                profile=investor_profile,
                cash_flow_score=cash_flow_score,
                appreciation_score=appreciation_score,
                tax_score=tax_score,
                risk_score=risk_score,
            )

            package.personalized_thesis = self.personalized_builder.build(
                profile=investor_profile,
                fit_score=fit_score,
                property_name=property_name,
                recommendation=recommendation,
            )

        self.thesis_exporter.export(
            package.investment_thesis,
            output_directory,
        )

        package.executive_summary = self.summary_builder.build(
            package,
        )

        self.exporter.export(
            package,
            output_directory,
        )

        return package
