# MF-301.1 Integration Map

## Purpose

Define how the first investor workflow integrates with the existing MeridianForge platform.

MF-301 does not create a second analysis engine.

It creates a product layer above existing capabilities.

---

# Existing Capabilities

## Intake Layer

Responsibility:

Convert external sources into internal opportunity records.

Existing:

* CSV intake
* Excel intake
* manual intake
* adapters
* normalization

Output:

Normalized opportunity.

---

## Analysis Layer

Responsibility:

Calculate investment metrics.

Existing:

* cash flow analysis
* mortgage calculations
* return metrics
* underwriting logic

Output:

Analysis result.

---

## Ranking Layer

Responsibility:

Compare opportunities.

Existing:

* scoring
* ranking pipeline
* acquisition ranking

Output:

Ranked opportunity.

---

## Intelligence Layer

Responsibility:

Convert metrics into decisions.

Existing:

* decision models
* recommendation logic
* confidence scoring

Output:

Investment decision.

---

# New MF-301 Product Layer

Location:

```
src/meridianforge/product/
```

Purpose:

Provide investor workflow orchestration.

---

# New Components

## workflow.py

Role:

Coordinate the complete investor journey.

Flow:

```
Opportunity
      |
      v
Analysis
      |
      v
Decision
      |
      v
Investment Review
```

---

## investment_review.py

Role:

Create investor-facing summary object.

Contains:

* property information
* financial metrics
* recommendation
* confidence
* risks

---

## recommendation.py

Role:

Translate analysis into:

* BUY
* WATCH
* PASS

Initial version uses deterministic rules.

---

# Integration Rule

MF-301 must reuse:

* existing models
* existing calculation engines
* existing analysis services

No duplicate:

* calculators
* scoring engines
* recommendation systems

---

# Definition of Done

MF-301.1 is successful when:

A property opportunity can move through:

```
Input
 |
Analysis
 |
Recommendation
 |
Investor Review
```

using existing MeridianForge components.

---

# Deferred

Not part of MF-301:

* database changes
* UI redesign
* cloud deployment
* AI agents
* external APIs

```
```

