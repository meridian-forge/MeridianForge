# MF-328 Duplicate Implementation Inventory

## Purpose

This document inventories duplicate implementations identified during MF-326 architecture analysis.

The objective is to classify duplicates before consolidation while preserving:

- business behavior
- calculation consistency
- workflow compatibility
- test coverage

---

# Baseline

| Metric | Value |
|---|---:|
| Production modules | 297 |
| Test functions | 234 |
| Test coverage | ~89% |
| Architecture guardrails | Active |

---

# Duplicate Classification

## Category A — Safe Duplicate

Examples:

- __init__.py files
- package exports
- namespace helpers

Action:

No consolidation required.

---

## Category B — Compatibility Duplicate

Examples:

- wrappers
- legacy import paths
- adapters

Action:

Maintain temporarily.

Requirements:

- canonical owner identified
- migration path documented
- removal criteria defined

---

## Category C — Risk Duplicate

Examples:

- financial calculations
- engines
- business workflows

Action:

Prioritize consolidation.

---

# Inventory

## 1. Underwriting

Canonical:
src/meridianforge/engine/underwriting_engine.py

Related:
src/meridianforge/analysis/underwriting_engine.py
src/meridianforge/decision/pipeline.py
src/meridianforge/reporting/builder.py

Classification:

Category B — Compatibility Duplicate

Decision:

Engine owns underwriting calculations.

---

## 2. Investment Pipeline

Canonical:
src/meridianforge/services/investment_pipeline.py

Classification:

Category B — Compatibility Duplicate

Decision:

Services layer owns pipeline orchestration.

---

## 3. Normalization

Locations:
src/meridianforge/normalization/
src/meridianforge/opportunity/
src/meridianforge/data/

Classification:

Category C — Risk Duplicate

Decision:

Normalization layer becomes canonical owner.

Reason:

Imported property data must produce consistent downstream analysis.

---

## 4. Mortgage Calculations

Locations:
src/meridianforge/engine/mortgage.py
src/meridianforge/finance/mortgage.py

Classification:

Category C — Risk Duplicate

Decision:

Engine calculation layer becomes canonical owner.

Reason:

Mortgage calculations directly affect underwriting outputs.

---

## 5. Metrics

Locations:
src/meridianforge/engine/metrics.py
src/meridianforge/analysis/metrics.py

Classification:

Category C — Risk Duplicate

Decision:

Engine owns investment metric calculations.

---

# Consolidation Priority

| Priority | Capability | Risk |
|---|---|---|
| 1 | Mortgage calculations | High |
| 2 | Metrics | High |
| 3 | Normalization | High |
| 4 | Underwriting wrappers | Medium |
| 5 | Pipeline wrappers | Medium |

---

# Consolidation Rules

Before removing any duplicate:

1. Add migration tests
2. Redirect imports
3. Run full pytest suite
4. Confirm coverage remains stable
5. Remove deprecated implementation

---

# Completion Criteria

MF-328 is complete when:

- duplicate inventory is documented
- ownership decisions are recorded
- migration order is established
- no production behavior changes occur

