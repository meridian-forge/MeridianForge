# MF-301.0 First Usable Investor Workflow Specification

## Objective

Create the first complete MeridianForge investor workflow.

The user should be able to take a property opportunity from raw input to
investment decision.

------------------------------------------------------------------------

# Target Workflow

## Step 1 --- Opportunity Intake

Input sources:

- CSV property lists
- Excel proformas
- Turnkey provider spreadsheets
- Manual entries

Example:

    Property:
    Jacksonville FL SFR

    Purchase Price:
    $325,000

    Monthly Rent:
    $2,500

    Expenses:
    $900/month

    Financing:
    20% down
    7% interest
    30 years

------------------------------------------------------------------------

# Step 2 --- Data Normalization

Convert different sources into a common investment opportunity model.

Required normalized fields:

## Property

- address
- city
- state
- property type
- bedrooms
- bathrooms
- square footage

## Acquisition

- purchase price
- closing costs
- repairs
- initial investment

## Income

- monthly rent
- other income
- vacancy assumption

## Expenses

- taxes
- insurance
- HOA
- maintenance
- property management

## Financing

- loan amount
- interest rate
- term
- down payment

------------------------------------------------------------------------

# Step 3 --- Financial Analysis

Calculate:

## Cash Flow

Monthly:

Income - Expenses - Debt Service

------------------------------------------------------------------------

## Returns

Calculate:

- cash-on-cash return
- cap rate
- DSCR
- annual cash flow

------------------------------------------------------------------------

## Risk Indicators

Evaluate:

- vacancy sensitivity
- expense sensitivity
- interest rate sensitivity

------------------------------------------------------------------------

# Step 4 --- Investment Recommendation

Generate:

    MeridianForge Investment Review

    Property:
    _______________

    Recommendation:
    BUY / WATCH / PASS

    Confidence:
    HIGH / MEDIUM / LOW

    Key Reasons:

    1.
    2.
    3.

    Primary Risks:

    1.
    2.
    3.

------------------------------------------------------------------------

# MF-301.0 Deliverables

## Code

Create:

    src/meridianforge/product/

Components:

    workflow.py
    decision_report.py
    investment_review.py

------------------------------------------------------------------------

## Tests

Add:

    tests/product/

Coverage:

- workflow execution
- recommendation generation
- report creation

------------------------------------------------------------------------

## Documentation

Complete:

- workflow specification
- acceptance criteria
- sample investor report

------------------------------------------------------------------------

# Definition of Done

MF-301 is complete when:

A user can run:

    meridianforge analyze property.xlsx

and receive:

    Investment Review Report
    +
    BUY/WATCH/PASS Recommendation

without manually calculating returns.

------------------------------------------------------------------------

# Deferred

Not included:

- Web interface
- Cloud deployment
- Mobile app
- Multi-user support
- Automated property scraping
- AI agents

These come only after the core investor workflow proves useful.
