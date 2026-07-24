"""
Portfolio architecture boundary tests.

MF-342.3

Validates:
- portfolio domain isolation
- analytics layering
- dashboard dependency direction
"""

from pathlib import Path

SRC = Path("src/meridianforge")


def test_portfolio_module_exists():
    """
    Portfolio domain package exists.
    """

    assert (SRC / "portfolio").exists()


def test_portfolio_domain_model_exists():
    """
    Portfolio aggregate exists.
    """

    assert (SRC / "portfolio" / "portfolio.py").exists()


def test_portfolio_analytics_exists():
    """
    Portfolio analytics layer exists.
    """

    assert (SRC / "portfolio" / "analytics.py").exists()


def test_portfolio_dashboard_exists():
    """
    Portfolio dashboard layer exists.
    """

    assert (SRC / "portfolio" / "dashboard.py").exists()
