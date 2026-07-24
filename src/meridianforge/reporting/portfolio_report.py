"""
Portfolio investor report.

MF-343.1

Transforms portfolio analytics into
human-readable investor reporting.
"""

from dataclasses import dataclass, field

from meridianforge.portfolio.analytics import (
    PortfolioAnalytics,
)
from meridianforge.portfolio.portfolio import (
    Portfolio,
)
from meridianforge.reporting.report_section import (
    ReportSection,
)


@dataclass(slots=True)
class PortfolioReport:
    """
    Investor-facing portfolio report.
    """

    title: str

    portfolio_name: str

    strategy: str

    sections: list[ReportSection] = field(
        default_factory=list,
    )

    def render(self) -> str:
        """
        Render report as text.
        """

        lines: list[str] = [
            self.title,
            "=" * len(self.title),
            "",
            f"Portfolio: {self.portfolio_name}",
            f"Strategy: {self.strategy}",
            "",
        ]

        for section in self.sections:
            lines.append(
                section.title,
            )

            lines.append(
                "-" * len(section.title),
            )

            for metric in section.metrics:
                lines.append(
                    f"{metric.name}: {metric.value}",
                )

            lines.append("")

        return "\n".join(lines)


class PortfolioReportBuilder:
    """
    Builds investor reports from portfolio analytics.
    """

    @staticmethod
    def build(
        portfolio: Portfolio,
        analytics: PortfolioAnalytics,
    ) -> PortfolioReport:
        """
        Convert portfolio analytics into report.
        """

        from meridianforge.reporting.report_metric import (
            ReportMetric,
        )

        performance = ReportSection(
            title="Portfolio Performance",
        )

        performance.add_metric(
            ReportMetric(
                name="Assets",
                value=str(
                    analytics.asset_count,
                ),
            )
        )

        performance.add_metric(
            ReportMetric(
                name="Total Investment",
                value=f"${analytics.total_purchase_price:,.0f}",
            )
        )

        performance.add_metric(
            ReportMetric(
                name="Monthly Rent",
                value=f"${analytics.total_monthly_rent:,.0f}",
            )
        )

        performance.add_metric(
            ReportMetric(
                name="Annual Cash Flow",
                value=f"${analytics.annual_cash_flow:,.0f}",
            )
        )

        returns = ReportSection(
            title="Investment Returns",
        )

        returns.add_metric(
            ReportMetric(
                name="Average Cap Rate",
                value=f"{analytics.average_cap_rate:.2%}",
            )
        )

        returns.add_metric(
            ReportMetric(
                name="Average DSCR",
                value=f"{analytics.average_dscr:.2f}",
            )
        )

        returns.add_metric(
            ReportMetric(
                name="Portfolio Score",
                value=f"{analytics.portfolio_score:.1f}",
            )
        )

        return PortfolioReport(
            title="Meridian Forge Portfolio Report",
            portfolio_name=portfolio.name,
            strategy=portfolio.strategy,
            sections=[
                performance,
                returns,
            ],
        )
