import streamlit as st

from meridianforge.application.models import (
    PropertyInput,
)

from meridianforge.application.service import (
    MeridianForgeService,
)

from meridianforge.ui.dashboard import (
    render_dashboard,
)


def main() -> None:

    st.title(
        "Meridian Forge"
    )

    st.write(
        "AI Assisted Real Estate Underwriting"
    )

    address = st.text_input(
        "Property Address"
    )

    purchase_price = st.number_input(
        "Purchase Price",
        min_value=0.0,
    )

    rent = st.number_input(
        "Monthly Rent",
        min_value=0.0,
    )

    noi = st.number_input(
        "Annual NOI",
        min_value=0.0,
    )

    cash_flow = st.number_input(
        "Annual Cash Flow",
        min_value=0.0,
    )

    cash_invested = st.number_input(
        "Cash Invested",
        min_value=0.0,
    )

    annual_debt = st.number_input(
        "Annual Debt",
        min_value=0.0,
    )


    if st.button(
        "Analyze Property"
    ):

        service = MeridianForgeService()

        result = service.analyze_property(
            PropertyInput(
                address=address,
                purchase_price=purchase_price,
                monthly_rent=rent,
                noi=noi,
                annual_cash_flow=cash_flow,
                cash_invested=cash_invested,
                annual_debt=annual_debt,
            )
        )

        render_dashboard(
            result
        )


if __name__ == "__main__":
    main()
