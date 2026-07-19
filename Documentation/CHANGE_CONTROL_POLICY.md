# MeridianForge Change Control Policy

## Purpose

MeridianForge is being developed as an investor decision platform, not
as a software engineering exercise.

This policy exists to prevent scope creep, unnecessary architecture
expansion, and delays to usable product delivery.

The primary objective is:

> Deliver a working investor workflow as quickly as possible while
> maintaining enough technical quality to support future growth.

------------------------------------------------------------------------

# Core Principle

## Product Before Platform

No engineering improvement should delay a user-facing capability unless
there is a clear justification.

A feature is prioritized based on:

1.  Does it improve investment decision quality?
2.  Does it enable a required user workflow?
3.  Does delaying it create future rework that is more expensive than
    doing it now?

------------------------------------------------------------------------

# Change Request Requirements

Any proposed work item outside the current roadmap must document:

## 1. Business Justification

What investor problem does this solve?

Example:

"Enable Excel proforma ingestion from turnkey providers."

Approved.

Example:

"Refactor module naming for cleaner architecture."

Deferred.

------------------------------------------------------------------------

## 2. Timing Justification

Why must this happen before the current product milestone?

The request must explain:

- What breaks without it?
- Which milestone is blocked?
- Why cannot it wait?

------------------------------------------------------------------------

## 3. Product Impact

Classify the request:

### P0 --- Product Blocker

Required before usable product.

Examples:

- Cannot import property data
- Cannot calculate returns
- Cannot generate recommendation

Action: Do immediately.

------------------------------------------------------------------------

### P1 --- Investor Value Improvement

Directly improves decisions.

Examples:

- Better stress testing
- Better comparison reports
- More accurate assumptions

Action: Schedule into upcoming sprint.

------------------------------------------------------------------------

### P2 --- Engineering Improvement

Improves maintainability but does not affect users.

Examples:

- Refactoring
- Renaming modules
- Internal cleanup

Action: Defer unless blocking.

------------------------------------------------------------------------

### P3 --- Engineering Preference

Improves elegance only.

Examples:

- New framework
- New architecture pattern
- Technology migration

Action: Reject until justified.

------------------------------------------------------------------------

# Scope Freeze Rule

Once a sprint begins:

- No additional features are added without review.
- New ideas go into the backlog.
- Existing commitments are protected.

------------------------------------------------------------------------

# Roadmap Protection

Current priority order:

1.  MF-300 Productization
2.  MF-301 First Usable Investor Workflow
3.  MF-302 Underwriting Enhancement
4.  MF-303 Deal Comparison
5.  MF-304 Investor Dashboard
6.  MF-400 Intelligence Layer

Any change delaying MF-301 requires explicit approval.

------------------------------------------------------------------------

# Definition of Success

MeridianForge succeeds when:

A real investor can:

1.  Import an opportunity.
2.  Analyze financial outcomes.
3.  Understand risks.
4.  Receive a recommendation.
5.  Make a better investment decision.

Software quality supports this mission.

Software development itself is not the mission.
