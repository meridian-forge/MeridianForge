"""
Investor report formatting.

Transforms InvestmentReport objects into
human-readable output.
"""

from meridianforge.models.results.report import InvestmentReport


class ReportFormatter:
    """
    Formats investment reports.
    """

    @staticmethod
    def format(
        report: InvestmentReport,
    ) -> str:
        """
        Create investor-facing text report.
        """

        analysis = report.analysis
        property_data = report.property

        location = (
            f"{property_data.address.city}, "
            f"{property_data.address.state} "
            f"{property_data.address.zip_code}"
        )

        return f"""
====================================================
Meridian Forge Property Analyzer
====================================================

PROPERTY
----------------------------------------------------
{property_data.address.street}
{location}

FINANCIAL SUMMARY
----------------------------------------------------
Purchase Price        ${analysis.purchase_price:,.0f}
Monthly Rent          ${analysis.monthly_rent:,.0f}

Cap Rate              {analysis.cap_rate:.2f}%

DSCR                  {analysis.dscr:.2f}

Monthly Cash Flow     ${analysis.monthly_cash_flow:,.2f}

Cash on Cash          {analysis.cash_on_cash_return:.2f}%


RISK ASSESSMENT
----------------------------------------------------
Risk Rating           {report.risk_rating.value}


INVESTMENT DECISION
----------------------------------------------------
Recommendation        {report.recommendation}

{report.summary}

====================================================
"""
