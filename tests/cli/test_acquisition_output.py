from argparse import Namespace

from meridianforge.cli.acquisition import (
    run_acquisition,
)


def test_acquisition_cli_outputs_report(
    capsys,
    monkeypatch,
):

    class FakeResult:

        class Review:

            cards = []

        review = Review()

    class FakeExecution:

        def execute(
            self,
            opportunity,
            investor,
        ):
            return FakeResult()

    monkeypatch.setattr(
        "meridianforge.cli.acquisition.AcquisitionExecutionService",
        lambda: FakeExecution(),
    )

    class FakeFileService:

        def load(
            self,
            file,
        ):
            return object()

    monkeypatch.setattr(
        "meridianforge.cli.acquisition.AcquisitionFileService",
        lambda: FakeFileService(),
    )

    run_acquisition(
        Namespace(
            file="property.xlsx",
        )
    )

    output = capsys.readouterr().out

    assert "MERIDIAN FORGE ACQUISITION REVIEW" in output
