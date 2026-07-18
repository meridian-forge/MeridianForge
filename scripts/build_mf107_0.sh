#!/bin/bash

set -e

PACKAGE="updates/packages/MF-107.0"

echo "======================================"
echo "BUILD MF-107.0 STREAMLIT MVP UI"
echo "======================================"

rm -rf "$PACKAGE"

mkdir -p \
"$PACKAGE/files/src/meridianforge/ui" \
"$PACKAGE/files/tests/ui"


cat > "$PACKAGE/manifest.txt" <<'EOF'
MF-107.0
Streamlit MVP User Interface

Adds:
- Browser application
- Property input screen
- Analysis dashboard
EOF


cat > "$PACKAGE/release_notes.md" <<'EOF'
# MF-107.0 Streamlit MVP Interface

Introduces first user-facing application.

Features:
- Property input
- Analysis execution
- Decision dashboard
EOF


cat > "$PACKAGE/files/src/meridianforge/ui/__init__.py" <<'PY'
PY


cat > "$PACKAGE/files/src/meridianforge/ui/dashboard.py" <<'PY'
from typing import Any


def render_dashboard(
    result: dict[str, Any],
) -> None:

    import streamlit as st

    st.subheader("Investment Analysis")

    st.metric(
        "Decision Score",
        result["score"],
    )

    st.metric(
        "Cap Rate",
        f'{result["cap_rate"]:.2%}',
    )

    st.metric(
        "DSCR",
        f'{result["dscr"]:.2f}',
    )

    st.success(
        "Analysis Complete"
    )
PY


cat > "$PACKAGE/files/src/meridianforge/ui/app.py" <<'PY'
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
PY


cat > "$PACKAGE/files/tests/ui/test_ui_import.py" <<'PY'
def test_ui_import():

    import meridianforge.ui.app

    assert True
PY


echo
echo "MF-107.0 PACKAGE CREATED"