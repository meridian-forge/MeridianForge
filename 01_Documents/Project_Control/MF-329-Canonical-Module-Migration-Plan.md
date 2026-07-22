# MF-329 Canonical Module Migration Plan

## Purpose

This document defines the controlled migration strategy for consolidating MeridianForge duplicate implementations.

The objective is to move toward a single canonical owner for each business capability while preserving:

- existing functionality
- investment calculations
- CLI behavior
- workflow compatibility
- test coverage

---

# Current Baseline

| Metric | Value |
|---|---:|
| Production modules | 297 |
| Test functions | 234 |
| Test coverage | ~89% |
| Architecture guardrails | Active |

---

# Migration Principles

## Rule 1 — Redirect Before Removing

No duplicate implementation will be deleted until:

- imports are migrated
- tests confirm behavior
- dependent workflows are validated

---

## Rule 2 — Calculations Have Highest Priority

Financial calculations directly impact investment decisions.

Calculation modules receive priority over structural cleanup.

---

## Rule 3 — Preserve Public Interfaces

Existing:

- CLI commands
- workflows
- reports
- analysis outputs

must continue functioning.

---

# Migration Sequence

---

# Phase 1 — Compatibility Layer Consolidation

## Objective

Remove unnecessary wrapper duplication.

Targets:


analysis/
decision/
application/
services/


Primary Capability:

Underwriting

Canonical Owner:


src/meridianforge/engine/underwriting_engine.py


Migration:

Existing consumers redirect imports to engine implementation.

Validation:


pytest


---

# Phase 2 — Financial Calculation Consolidation

## Objective

Create one source of truth for investment calculations.

Priority:

## Mortgage

Current:


src/meridianforge/engine/mortgage.py
src/meridianforge/finance/mortgage.py


Decision:

Engine layer owns mortgage calculations.

---

## Metrics

Current:


src/meridianforge/engine/metrics.py
src/meridianforge/analysis/metrics.py


Decision:

Engine layer owns investment metrics.

---

# Phase 3 — Data Normalization Consolidation

## Objective

Ensure imported property data follows one normalization path.

Current:


src/meridianforge/normalization/
src/meridianforge/opportunity/
src/meridianforge/data/


Decision:

Normalization package becomes canonical owner.

Migration:

Adapters delegate to canonical normalization.

---

# Phase 4 — Workflow Validation

Before cleanup:

Validate:

- acquisition workflow
- investor package generation
- reporting pipeline
- CLI workflows

Required:


pytest


Expected:


234 passed


---

# Migration Tracking

| Capability | Current Owner | Canonical Owner | Status |
|---|---|---|---|
| Underwriting | Multiple | engine | Planned |
| Mortgage | Multiple | engine | Planned |
| Metrics | Multiple | engine | Planned |
| Normalization | Multiple | normalization | Planned |
| Investment Pipeline | services | services | Stable |
| Reporting | reporting | reporting | Stable |
| Intake | intake | intake | Stable |

---

# Success Criteria

MF-329 completes when:

- migration order is documented
- canonical owners are confirmed
- risk areas are prioritized
- cleanup can proceed safely

---

# Next Step

MF-330 will begin controlled migration of the highest-risk duplicate:

1. Mortgage calculations
2. Metrics calculations
3. Normalization paths

No deletion before validation.

