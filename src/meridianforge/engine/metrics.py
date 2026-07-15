"""
Financial metrics calculations.

All functions are deterministic and independent
of data sources.
"""


class Metrics:
    """
    Real estate investment metric calculations.
    """

    @staticmethod
    def calculate_noi(
        gross_income: float,
        operating_expenses: float,
    ) -> float:
        """
        Calculate Net Operating Income.

        NOI = Gross Income - Operating Expenses
        """

        return gross_income - operating_expenses

    @staticmethod
    def calculate_cap_rate(
        annual_noi: float,
        purchase_price: float,
    ) -> float:
        """
        Calculate capitalization rate.

        Cap Rate = Annual NOI / Purchase Price * 100
        """

        if purchase_price <= 0:
            raise ValueError("Purchase price must be positive.")

        return annual_noi / purchase_price * 100

    @staticmethod
    def calculate_dscr(
        annual_noi: float,
        annual_debt_service: float,
    ) -> float:
        """
        Calculate Debt Service Coverage Ratio.

        DSCR = NOI / Debt Service
        """

        if annual_debt_service <= 0:
            raise ValueError("Debt service must be positive.")

        return annual_noi / annual_debt_service

    @staticmethod
    def calculate_cash_flow(
        annual_noi: float,
        annual_debt_service: float,
    ) -> float:
        """
        Calculate annual cash flow.

        Cash Flow = NOI - Debt Service
        """

        return annual_noi - annual_debt_service

    @staticmethod
    def calculate_cash_on_cash(
        annual_cash_flow: float,
        cash_invested: float,
    ) -> float:
        """
        Calculate cash-on-cash return.

        CoC = Annual Cash Flow / Cash Invested * 100
        """

        if cash_invested <= 0:
            raise ValueError("Cash invested must be positive.")

        return annual_cash_flow / cash_invested * 100
