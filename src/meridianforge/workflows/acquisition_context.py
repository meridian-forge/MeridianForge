"""
Acquisition workflow context.

Carries state through an acquisition run.
"""

from dataclasses import dataclass

from meridianforge.product.weekly_review import WeeklyInvestorReview
from meridianforge.workflows.acquisition_input import AcquisitionInput


@dataclass(slots=True)
class AcquisitionRunContext:
    """
    State container for an acquisition workflow.
    """

    opportunity: AcquisitionInput

    review: WeeklyInvestorReview
