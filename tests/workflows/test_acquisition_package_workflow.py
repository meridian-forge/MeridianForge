from pathlib import Path

from meridianforge.workflows.acquisition_input import (
    AcquisitionInput,
)
from meridianforge.workflows.acquisition_package_workflow import (
    AcquisitionPackageWorkflow,
)


def test_acquisition_package_workflow_creates_package(
    tmp_path: Path,
):

    opportunity = AcquisitionInput(
        property_address="123 Main St",
        purchase_price=250000,
        market="Jacksonville",
        source="Zillow",
    )

    package_location = (
        AcquisitionPackageWorkflow().execute(
            opportunity,
            tmp_path / "exports",
            tmp_path / "archive",
        )
    )

    assert package_location.exists()
