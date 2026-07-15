"""
Core underwriting engine.

Coordinates property analysis using:
- Mortgage calculations
- Financial metrics
"""

from meridianforge.engine.metrics import Metrics
from meridianforge.engine.mortgage import Mortgage
from meridianforge.models.domain.property import Property
from meridianforge.models.results.analysis_result import AnalysisResult


class UnderwritingEngine:
    """
    Performs complete real estate underwriting analysis.
    """

    @staticmethod
    def analyze(property_data: Property) -> AnalysisResult:
        """
        Analyze a property investment.
        """

        gross_income = property_data.income.gross_monthly_income

        operating_expenses = (
            property_data.expenses.taxes / 12
            + property_data.expenses.insurance / 12
            + property_data.expenses.hoa / 12
            + property_data.expenses.management
            + property_data.expenses.maintenance
        )

        monthly_noi = Metrics.calculate_noi(
            gross_income,
            operating_expenses,
        )

        annual_noi = monthly_noi * 12

        mortgage = Mortgage(
            loan_amount=(
                property_data.acquisition.purchase_price
                - property_data.financing.down_payment
            ),
            interest_rate=property_data.financing.interest_rate,
            term_years=property_data.financing.loan_term_years,
        )

        annual_debt_service = mortgage.annual_payment

        annual_cash_flow = Metrics.calculate_cash_flow(
            annual_noi,
            annual_debt_service,
        )

        dscr = Metrics.calculate_dscr(
            annual_noi,
            annual_debt_service,
        )

        cap_rate = Metrics.calculate_cap_rate(
            annual_noi,
            property_data.acquisition.purchase_price,
        )

        cash_on_cash = Metrics.calculate_cash_on_cash(
            annual_cash_flow,
            property_data.financing.down_payment,
        )

        return AnalysisResult(
            purchase_price=property_data.acquisition.purchase_price,
            monthly_rent=property_data.income.monthly_rent,
            gross_monthly_income=gross_income,
            operating_expenses_monthly=operating_expenses,
            net_operating_income_monthly=monthly_noi,
            mortgage_payment_monthly=mortgage.monthly_payment,
            monthly_cash_flow=annual_cash_flow / 12,
            annual_cash_flow=annual_cash_flow,
            cap_rate=cap_rate,
            cash_on_cash_return=cash_on_cash,
            dscr=dscr,
            debt_service_annual=annual_debt_service,
            total_cash_required=property_data.acquisition.total_project_cost,
            passed=dscr >= 1.20,
        )
