from meridianforge.dashboard.widgets import (
    DashboardWidgetBuilder,
)


def test_health_widget_strong():

    widget = DashboardWidgetBuilder.health(
        95,
    )

    assert widget.status == "STRONG"


def test_cash_flow_widget():

    widget = DashboardWidgetBuilder.cash_flow(
        5000,
    )

    assert "$5,000" in widget.value
