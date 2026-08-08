from __future__ import annotations

from pathlib import Path

from meridianforge.cli.monday_gmail import MondayGmailCommand
from meridianforge.models.domain.investment_strategy import InvestmentStrategy
from meridianforge.models.domain.investor_profile import InvestorProfile


class StubCommand(MondayGmailCommand):
    def run(
        self,
        investor_profile: InvestorProfile,
        output_directory: Path,
    ) -> str:
        return (
            "# MeridianForge Monday Gmail Execution\n\n"
            "Analyzed opportunities: 1\n"
            f"Package: {output_directory / 'package'}\n"
        )


def test_run_production_monday_gmail_command(tmp_path: Path) -> None:
    command = StubCommand()

    profile = InvestorProfile(
        name="MeridianForge Test Investor",
        strategy=InvestmentStrategy.CASH_FLOW,
    )

    dashboard = command.run(
        profile,
        tmp_path,
    )

    assert "Analyzed opportunities: 1" in dashboard
    assert "MeridianForge Monday Gmail Execution" in dashboard
