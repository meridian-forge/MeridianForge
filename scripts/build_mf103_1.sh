#!/bin/bash

set -e

PACKAGE="updates/packages/MF-103.1"

echo "======================================"
echo "BUILD MF-103.1 FINANCIAL MODEL"
echo "======================================"

rm -rf "$PACKAGE"

mkdir -p \
"$PACKAGE/files/src/meridianforge/finance" \
"$PACKAGE/files/tests/finance"


cat > "$PACKAGE/manifest.txt" <<'EOF'
MF-103.1
Financial Assumption Model

Adds:
- Financing assumptions
- Mortgage calculation
- Expense model
- Cash flow model
EOF


cat > "$PACKAGE/release_notes.md" <<'EOF'
# MF-103.1 Financial Assumption Model

Introduces assumption-driven underwriting.

Includes:
- Mortgage payment
- Operating expenses
- NOI
- Monthly cash flow
EOF


cat > "$PACKAGE/files/src/meridianforge/finance/assumptions.py" <<'PY'
from dataclasses import dataclass


@dataclass
class FinancialAssumptions:

    purchase_price: float

    down_payment_percent: float
    interest_rate: float
    loan_years: int

    monthly_rent: float

    vacancy_percent: float
    repairs_percent: float
    management_percent: float

    insurance_monthly: float
    taxes_monthly: float
PY


cat > "$PACKAGE/files/src/meridianforge/finance/mortgage.py" <<'PY'
def monthly_payment(
    loan_amount: float,
    annual_rate: float,
    years: int,
) -> float:

    if loan_amount <= 0:
        raise ValueError(
            "Loan amount must be positive"
        )

    monthly_rate = annual_rate / 12
    payments = years * 12

    if monthly_rate == 0:
        return loan_amount / payments

    return (
        loan_amount
        * monthly_rate
        * (1 + monthly_rate) ** payments
        /
        ((1 + monthly_rate) ** payments - 1)
    )
PY


cat > "$PACKAGE/files/src/meridianforge/finance/expenses.py" <<'PY'
def monthly_expenses(
    rent: float,
    vacancy: float,
    repairs: float,
    management: float,
    insurance: float,
    taxes: float,
) -> float:

    return (
        rent * vacancy
        + rent * repairs
        + rent * management
        + insurance
        + taxes
    )
PY


cat > "$PACKAGE/files/src/meridianforge/finance/cashflow.py" <<'PY'
def monthly_cash_flow(
    rent: float,
    expenses: float,
    mortgage: float,
) -> float:

    return rent - expenses - mortgage
PY


cat > "$PACKAGE/files/src/meridianforge/finance/__init__.py" <<'PY'
PY


cat > "$PACKAGE/files/tests/finance/test_mortgage.py" <<'PY'
from meridianforge.finance.mortgage import monthly_payment


def test_mortgage():

    payment = monthly_payment(
        200000,
        0.06,
        30,
    )

    assert round(payment, 2) == 1199.10
PY


cat > "$PACKAGE/files/tests/finance/test_cashflow.py" <<'PY'
from meridianforge.finance.cashflow import monthly_cash_flow


def test_cashflow():

    result = monthly_cash_flow(
        2000,
        400,
        900,
    )

    assert result == 700
PY


echo
echo "MF-103.1 PACKAGE CREATED"