"""
Decision context builder.

Transforms investment pipeline output
into normalized decision intelligence input.
"""

from meridianforge.decision.intelligence.decision_context import (
    DecisionContext,
)
from meridianforge.models.results.investment_pipeline_result import (
    InvestmentPipelineResult,
)


class DecisionContextBuilder:
    """
    Creates decision context from ranked investment results.
    """

    @staticmethod
    def build(
        pipeline_result: InvestmentPipelineResult,
        investor_strategy: str,
    ) -> DecisionContext:
        """
        Build decision context from top ranked deal.
        """

        if not pipeline_result.ranked_deals:
            raise ValueError("Cannot create decision context without ranked deals.")

        ranked_deal = pipeline_result.ranked_deals[0]

        property_data = ranked_deal.property
        evaluation = ranked_deal.evaluation

        monthly_expenses = (
            property_data.expenses.taxes
            + property_data.expenses.insurance
            + property_data.expenses.hoa
            + property_data.expenses.maintenance
            + property_data.expenses.management
        )

        monthly_rent = property_data.income.monthly_rent

        monthly_cash_flow = monthly_rent - monthly_expenses

        noi = monthly_cash_flow * 12

        return DecisionContext(
            property_address=property_data.address.street,
            market=property_data.address.city,
            purchase_price=property_data.acquisition.purchase_price,
            monthly_rent=monthly_rent,
            monthly_expenses=monthly_expenses,
            noi=noi,
            cap_rate=evaluation.score,
            monthly_cash_flow=monthly_cash_flow,
            investor_strategy=investor_strategy,
            risk_flags=evaluation.failed_criteria,
            strengths=evaluation.reasons,
        )
