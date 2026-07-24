"""
Investor package export layer.

MF-345.3

Builds complete investor-facing packages
from dashboard reports.
"""

from dataclasses import dataclass, field
from pathlib import Path

from meridianforge.reporting.investor_dashboard_report import (
    InvestorDashboardReport,
)


@dataclass(slots=True)
class InvestorPackage:
    """
    Investor package artifact.
    """

    title: str

    report: InvestorDashboardReport

    metadata: dict[str, str] = field(
        default_factory=dict,
    )

    def render(self) -> str:
        """
        Render complete investor package.
        """

        lines: list[str] = []

        lines.append(
            self.title,
        )

        lines.append(
            "=" * len(self.title),
        )

        lines.append(
            self.report.render(),
        )

        if self.metadata:
            lines.append(
                "",
            )

            lines.append(
                "Metadata:",
            )

            for key, value in self.metadata.items():
                lines.append(
                    f"{key}: {value}",
                )

        return "\n".join(lines)


class InvestorPackageBuilder:
    """
    Creates investor packages.
    """

    @staticmethod
    def build(
        report: InvestorDashboardReport,
        metadata: dict[str, str] | None = None,
    ) -> InvestorPackage:
        """
        Assemble investor package.
        """

        return InvestorPackage(
            title="Meridian Forge Investor Package",
            report=report,
            metadata=metadata or {},
        )


class InvestorPackageExporter:
    """
    Exports investor packages.
    """

    @staticmethod
    def export_text(
        package: InvestorPackage,
        output_path: Path,
    ) -> Path:
        """
        Export investor package as text.
        """

        output_path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        output_path.write_text(
            package.render(),
            encoding="utf-8",
        )

        return output_path
