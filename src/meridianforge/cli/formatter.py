"""
CLI output formatting.
"""

from meridianforge.cli.analyzer import CLIAnalysis


def format_header(
    title: str,
) -> str:
    """
    Format CLI section header.
    """

    return (
        "\n"
        "====================================================\n"
        f"{title}\n"
        "===================================================="
    )


def format_metric(
    label: str,
    value: str,
) -> str:
    """
    Format a single metric line.
    """

    return f"{label:<22}{value}"


class CLIFormatter:
    """
    Formats analysis results for terminal output.
    """

    @staticmethod
    def format_report(
        data: CLIAnalysis,
    ) -> str:
        """
        Build human-readable report.
        """

        property_data = data.property
        analysis = data.analysis
        risk = data.risk

        address_line = (
            f"{property_data.address.city}, "
            f"{property_data.address.state} "
            f"{property_data.address.zip_code}"
        )

        return f"""
====================================================
Meridian Forge Property Analyzer
====================================================

Property
----------------------------------------------------
{property_data.address.street}
{address_line}

Purchase Price      ${analysis.purchase_price:,.0f}
Monthly Rent        ${analysis.monthly_rent:,.0f}

Financial Metrics
----------------------------------------------------
Cap Rate            {analysis.cap_rate:.2f}%

Cash Flow           ${analysis.monthly_cash_flow:,.2f}/mo

DSCR                {analysis.dscr:.2f}

Cash on Cash        {analysis.cash_on_cash_return:.2f}%

Risk Rating         {risk.value}

Recommendation      {"PASS" if analysis.passed else "REVIEW"}

====================================================
"""
