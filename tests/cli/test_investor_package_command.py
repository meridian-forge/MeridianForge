"""
Tests for investor package CLI command.
"""

from argparse import Namespace
from pathlib import Path

from meridianforge.cli.investor_package import (
    run_investor_package,
)


def test_investor_package_cli_generates_package(
    tmp_path: Path,
) -> None:
    """
    CLI command generates investor package output.
    """

    args = Namespace(
        package_id="CLI001",
        property_name="456 Oak Street",
        recommendation="BUY",
        confidence=0.95,
        output=str(tmp_path),
    )

    run_investor_package(args)

    assert (
        tmp_path / "Decision_Brief.md"
    ).exists()

    assert (
        tmp_path / "Archive_Metadata.json"
    ).exists()
