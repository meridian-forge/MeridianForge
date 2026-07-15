"""
CLI command implementations.
"""

from meridianforge.cli.analyzer import CLIAnalyzer
from meridianforge.cli.formatter import (
    format_header,
    format_metric,
)
from meridianforge.models.results.risk_rating import RiskRating


def analyze_command(
    file_path: str = "examples/sample_property.json",
) -> str:
    """
    Run property analysis command.
    """

    result = CLIAnalyzer.analyze_file(file_path)

    analysis = result.analysis
    risk = result.risk

    recommendation = "PASS" if risk == RiskRating.SAFE else "REVIEW"

    output = []

    output.append(format_header("Meridian Forge Property Analyzer"))

    output.append(
        format_metric(
            "Purchase Price",
            f"${analysis.purchase_price:,.0f}",
        )
    )

    output.append(
        format_metric(
            "Monthly Rent",
            f"${analysis.monthly_rent:,.0f}",
        )
    )

    output.append(
        format_metric(
            "Cap Rate",
            f"{analysis.cap_rate:.2f}%",
        )
    )

    output.append(
        format_metric(
            "DSCR",
            f"{analysis.dscr:.2f}",
        )
    )

    output.append(
        format_metric(
            "Monthly Cash Flow",
            f"${analysis.monthly_cash_flow:,.2f}",
        )
    )

    output.append(
        format_metric(
            "Cash on Cash",
            f"{analysis.cash_on_cash_return:.2f}%",
        )
    )

    output.append(
        format_metric(
            "Risk Rating",
            risk.value,
        )
    )

    output.append(
        format_metric(
            "Recommendation",
            recommendation,
        )
    )

    return "\n".join(output)
