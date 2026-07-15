"""
Mortgage calculation engine.

Handles residential fixed-rate amortizing loans.
"""

from dataclasses import dataclass


@dataclass(slots=True)
class Mortgage:
    """
    Residential fixed-rate mortgage model.

    All rates are expressed as percentages.

    Example:
        interest_rate=6.5 means 6.5%
    """

    loan_amount: float
    interest_rate: float
    term_years: int

    def __post_init__(self) -> None:
        if self.loan_amount <= 0:
            raise ValueError("Loan amount must be positive.")

        if self.interest_rate <= 0:
            raise ValueError("Interest rate must be positive.")

        if self.term_years <= 0:
            raise ValueError("Loan term must be positive.")

    @property
    def monthly_rate(self) -> float:
        """
        Convert annual percentage rate to monthly decimal rate.
        """

        return (self.interest_rate / 100) / 12

    @property
    def number_of_payments(self) -> int:
        """
        Total number of monthly payments.
        """

        return self.term_years * 12

    @property
    def monthly_payment(self) -> float:
        """
        Calculate monthly principal and interest payment.
        """

        rate = self.monthly_rate
        payments = self.number_of_payments

        return (
            self.loan_amount
            * (rate * (1 + rate) ** payments)
            / ((1 + rate) ** payments - 1)
        )

    @property
    def annual_payment(self) -> float:
        """
        Annual debt service.
        """

        return self.monthly_payment * 12

    @property
    def total_paid(self) -> float:
        """
        Total payments over loan life.
        """

        return self.monthly_payment * self.number_of_payments

    @property
    def total_interest(self) -> float:
        """
        Total interest paid.
        """

        return self.total_paid - self.loan_amount

    def remaining_balance(self, years: int) -> float:
        """
        Remaining loan balance after a number of years.
        """

        if years < 0:
            raise ValueError("Years cannot be negative.")

        if years > self.term_years:
            raise ValueError("Cannot exceed loan term.")

        months_elapsed = years * 12

        rate = self.monthly_rate

        balance = (
            self.loan_amount
            * (((1 + rate) ** self.number_of_payments) - ((1 + rate) ** months_elapsed))
            / (((1 + rate) ** self.number_of_payments) - 1)
        )

        return balance
