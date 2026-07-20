from pathlib import Path

from meridianforge.services.acquisition_orchestrator import (
    AcquisitionOrchestrator,
)


def test_acquisition_orchestrator_contract():

    orchestrator = AcquisitionOrchestrator()

    assert orchestrator.pipeline is not None
    assert orchestrator.intelligence is not None
    assert orchestrator.package_service is not None
