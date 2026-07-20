"""
Acquisition package workflow.

Creates investor-ready acquisition packages.
"""

from pathlib import Path

from meridianforge.operations.investor_package_service import (
    InvestorPackageService,
)
from meridianforge.product.weekly_review import (
    WeeklyInvestorReview,
)
from meridianforge.workflows.acquisition_decision_workflow import (
    AcquisitionDecisionWorkflow,
)
from meridianforge.workflows.acquisition_input import (
    AcquisitionInput,
)


class AcquisitionPackageWorkflow:
    """
    Coordinates decision generation and package creation.
    """

    def __init__(
        self,
        decision_workflow: AcquisitionDecisionWorkflow | None = None,
        package_service: InvestorPackageService | None = None,
    ) -> None:

        self.decision_workflow = (
            decision_workflow
            or AcquisitionDecisionWorkflow()
        )

        self.package_service = (
            package_service
            or InvestorPackageService()
        )

    def execute(
        self,
        opportunity: AcquisitionInput,
        export_path: Path,
        archive_path: Path,
    ):
        """
        Generate investor package.
        """

        review: WeeklyInvestorReview = (
            self.decision_workflow.execute(
                opportunity,
            )
        )

        return self.package_service.create_package(
            review,
            export_path,
            archive_path,
        )
