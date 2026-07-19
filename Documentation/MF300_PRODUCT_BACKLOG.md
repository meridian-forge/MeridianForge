# MeridianForge MF-300 Product Backlog

## Phase 3 — Productization

## Objective

Convert MeridianForge from a development platform into a usable weekly investment decision tool.

The goal is not to build a generalized software product.

The goal is:

> Help an investor consistently evaluate opportunities, compare alternatives, and make better acquisition decisions.

---

# Product User

Primary User:

Mahi — Real Estate Investor

Primary Workflow:

Weekly investment review.

---

# MF-301 — First Usable Investor Workflow

## Objective

Enable a complete end-to-end investment evaluation workflow.

## User Story

As an investor, I can provide a property opportunity and receive an investment recommendation.

---

## Deliverables

### Input

Support:

* CSV property files
* Excel property files
* Manual opportunity entry

Example sources:

* Zillow exports
* Realtor listings
* Turnkey provider packages
* Builder proformas

---

### Analysis Engine

Calculate:

* Purchase price
* Rental income
* Expenses
* Financing assumptions
* Monthly cash flow
* DSCR
* Cash-on-cash return
* Appreciation assumptions
* Risk indicators

---

### Decision Output

Generate:

Investment Review Report

Including:

* Property summary
* Financial metrics
* Risk assessment
* Recommendation

Recommendation:

* BUY
* WATCH
* PASS

---

## MF-301 Acceptance Criteria

Complete when:

A user can execute:

```bash
meridianforge analyze property.xlsx
```

and receive a decision report.

---

# MF-302 — Underwriting Enhancement

## Objective

Improve investment decision accuracy.

## Deliverables

Add:

* Financing scenarios
* DSCR optimization
* Interest rate sensitivity
* Vacancy stress testing
* Repair assumptions
* Expense inflation
* Appreciation scenarios

---

## Acceptance Criteria

Investor can understand:

"How does this deal perform under different future conditions?"

---

# MF-303 — Deal Comparison Engine

## Objective

Compare multiple opportunities.

## Deliverables

Support:

* Multiple property ranking
* Scenario comparison
* Investment scorecard
* Portfolio fit analysis

---

## Acceptance Criteria

Investor can answer:

"Which property should I buy first?"

---

# MF-304 — Investor Dashboard

## Objective

Create a personal investment command center.

## Deliverables

Track:

* Acquisition pipeline
* Owned properties
* Investment performance
* Upcoming decisions

---

# Explicitly Deferred

The following are intentionally NOT part of MF-300:

## Cloud Platform

Deferred.

Reason:
No external users yet.

---

## Mobile Application

Deferred.

Reason:
Desktop workflow is sufficient.

---

## Multi-user SaaS Architecture

Deferred.

Reason:
Product-market validation comes first.

---

## Database Migration

Deferred.

Reason:
Current file-based architecture is sufficient.

---

## Advanced AI Agents

Deferred.

Reason:
Automation should solve proven workflow problems.

---

# Product Success Definition

MeridianForge succeeds when:

1. Investment opportunities can be imported.
2. Financial outcomes can be calculated.
3. Risks can be evaluated.
4. Alternatives can be compared.
5. The investor can confidently decide:

BUY / WATCH / PASS

---

# Development Rule

Every sprint must answer:

"Does this move MeridianForge closer to a weekly investor decision workflow?"

If not:

Move it to backlog.

