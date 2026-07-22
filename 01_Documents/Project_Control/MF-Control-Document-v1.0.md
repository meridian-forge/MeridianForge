# MeridianForge Control Document

## Product Vision, Architecture Guardrails, Sprint Control & Execution Guide

**Version:** MF-325 Control Baseline\
**Status:** Active\
**Purpose:** Prevent feature drift, maintain architecture discipline,
and ensure every sprint moves MeridianForge closer to a usable
investment analysis product.

------------------------------------------------------------------------

# 1. Product Mission

## Vision

MeridianForge is an investment intelligence platform that helps
investors evaluate opportunities, make decisions, and manage investment
workflows.

The platform is designed to be:

- Asset-class agnostic at the core
- Specialized through modular asset adapters
- AI-enhanced over time
- Automation-first
- Decision-oriented

------------------------------------------------------------------------

# 2. MVP Focus

## Current MVP: Real Estate Investment Analyzer

The first usable product must allow an investor to:

1.  Upload property information
2.  Normalize the data
3.  Analyze investment performance
4.  Compare against investor goals
5.  Receive an investment recommendation

Primary user journey:

    Property Spreadsheet
            |
            v
    File Intake
            |
            v
    Opportunity Extraction
            |
            v
    Real Estate Adapter
            |
            v
    Underwriting Engine
            |
            v
    Investor Criteria
            |
            v
    Decision Card
            |
            v
    Investor Report

------------------------------------------------------------------------

# 3. MVP User Promise

A user should be able to answer:

## "Should I buy this property?"

MeridianForge should provide:

- Purchase price analysis
- Rental income analysis
- Expense analysis
- Cash flow
- DSCR
- Cap rate
- Cash-on-cash return
- Risk factors
- Recommendation

Output:

    BUY
    WATCH
    PASS

with explanation.

------------------------------------------------------------------------

# 4. Architecture Principles

## Principle 1 --- Core First, Assets Second

MeridianForge core should not know about specific investments.

Correct:

    Core Platform
          |
          |
    Asset Adapter
          |
          |
    Real Estate Module

Incorrect:

    Core Platform
          |
          |
    Real Estate Logic Everywhere

------------------------------------------------------------------------

## Principle 2 --- Preserve Existing Contracts

Before modifying an existing service:

Check:

- Existing tests
- Existing callers
- Existing data contracts

Preferred approach:

Add capability.

Avoid:

Replacing APIs without migration.

------------------------------------------------------------------------

## Principle 3 --- Every Workflow Must Be Testable End-to-End

Unit tests are necessary but not sufficient.

Primary MVP test:

    Excel File
        |
        v
    Opportunity
        |
        v
    Pipeline
        |
        v
    Underwriting
        |
        v
    Decision Card
        |
        v
    Report

------------------------------------------------------------------------

# 5. Current Technical Baseline

## MF-324 Completion

Status:

✅ Complete

Achievements:

- Acquisition execution workflow stabilized
- Intake compatibility restored
- Pipeline integration repaired
- Normalization behavior clarified
- Regression suite passing

Current test baseline:

    230 tests passing
    0 failures

------------------------------------------------------------------------

# 6. Current MVP Capability

## Completed

### Data Intake

✅ Excel processing\
✅ CSV processing\
✅ Field detection\
✅ Field normalization\
✅ Unknown field handling

### Investment Analysis

✅ Property modeling\
✅ Underwriting engine\
✅ Mortgage calculations\
✅ DSCR\
✅ Cap rate\
✅ Cash-on-cash return

### Decision Intelligence

✅ Investor profile matching\
✅ Deal scoring\
✅ Ranking\
✅ Decision cards

### Reporting

✅ Text reports\
✅ Investor review objects\
✅ Package generation foundation

------------------------------------------------------------------------

# 7. MF-325 Objective

## Real Estate Analyzer MVP

Goal:

Transform MeridianForge from a tested backend into a usable investor
tool.

------------------------------------------------------------------------

## MF-325 Deliverables

### User Experience

Build:

- Upload workflow
- Analysis status
- Results dashboard
- Recommendation display

------------------------------------------------------------------------

### Reporting

Build:

- Executive summary
- Deal score explanation
- Key risks
- Key advantages
- Exportable report

------------------------------------------------------------------------

### Reliability

Add:

- Workflow diagnostics
- Better error messages
- Input validation
- Missing data warnings

------------------------------------------------------------------------

# 8. Deferred Features

These remain part of the long-term vision but are NOT MVP priorities.

## Deferred

- Crypto analysis
- Stock analysis
- Options analysis
- AI investment agents
- Automated acquisition sourcing
- Market prediction models
- Portfolio optimization

Reason:

The platform must first prove one complete investment workflow.

------------------------------------------------------------------------

# 9. Sprint Decision Checklist

Before starting any development task:

## Product Check

Does this improve:

☐ Uploading data\
☐ Understanding investment performance\
☐ Making a decision\
☐ Receiving a report

If no:

Defer.

------------------------------------------------------------------------

## Architecture Check

Does this:

☐ Maintain asset separation?\
☐ Preserve existing contracts?\
☐ Improve modularity?

If no:

Redesign first.

------------------------------------------------------------------------

## Testing Check

Every feature requires:

☐ Unit test\
☐ Integration test if workflow changes\
☐ End-to-end user journey validation

------------------------------------------------------------------------

# 10. Definition of MVP Complete

MeridianForge MVP is complete when:

A real investor can:

1.  Upload a property spreadsheet
2.  Receive calculated returns
3.  See investment risks
4.  Understand recommendation
5.  Export a report
6.  Use the output to make a purchase decision

------------------------------------------------------------------------

# 11. Current Next Milestone

## MF-325

Theme:

**"From Engine to Investor Product"**

Primary outcome:

A working Real Estate Investment Analyzer MVP.
