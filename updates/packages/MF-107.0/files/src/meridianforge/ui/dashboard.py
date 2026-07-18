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
