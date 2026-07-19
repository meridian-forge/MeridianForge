#!/bin/bash

set -e

echo "MF-228 Documentation Control Center"

mkdir -p Documentation

cat > Documentation/CURRENT_STATUS.md <<'DOC'
# MeridianForge Current Status

## Current Release

v1.28.0-cli-framework

## Current Sprint

MF-228.0 MVP Workflow Stabilization

## Completed

MF-221 CSV Property Intake
MF-222 Monday Workflow Integration
MF-223 CLI File Intake
MF-224 Excel Intake Foundation
MF-225 Runtime Artifact Hygiene
MF-226 Repository Architecture Stabilization
MF-227 CLI Framework Modernization

## Active Objectives

- Establish documentation control center
- Stabilize MVP workflows
- Define canonical architecture
- Prepare operational MVP release

## Next Milestone

MF-229 Operational MVP Release Candidate
DOC


cat > Documentation/MASTER_ROADMAP.md <<'DOC'
# MeridianForge Master Roadmap

## Vision

MeridianForge is an AI-assisted investment operating system.

The mission is to identify, analyze, rank, acquire, and manage investment opportunities with minimal manual effort.

---

# Phase Roadmap

## MF-100 Foundation

Foundation platform:
- repository
- domain models
- financial engine
- testing standards

Status:
COMPLETE


## MF-200 Operational MVP

Capabilities:
- intake
- normalization
- analysis
- ranking
- reporting
- CLI workflows

Status:
MF-227 COMPLETE


## MF-228 MVP Stabilization

Focus:
- architecture clarity
- documentation control
- workflow stabilization
- release readiness


## MF-229 Operational MVP Release Candidate

Goal:

First operational release.

Acceptance:
- stable workflows
- regression passing
- documented operations


## MF-300 Intelligence Layer

- recommendations
- investment memory
- learning systems


## MF-400 Automation Layer

- deal discovery
- scheduled workflows
- alerts


## MF-500 Acquisition OS

- offers
- due diligence
- closing workflows


## MF-600 Portfolio OS

- monitoring
- tax tracking
- optimization


## MF-700 Platform Evolution

- scalable platform
- integrations
- AI assistants
DOC


cat > Documentation/ARCHITECTURE_DECISIONS.md <<'DOC'
# MeridianForge Architecture Decisions

## ADR-001

Decision:
Separate intake from analysis.

Reason:
Different data sources evolve independently.

Status:
Accepted


## ADR-002

Decision:
Maintain runtime workspace separation.

Reason:
Generated artifacts should not pollute source code.

Status:
Accepted


## ADR-003

Decision:
Keep ranking separate from underwriting.

Reason:
Investment prioritization and financial analysis are different concerns.

Status:
Accepted


## ADR-004

Decision:
Delay advanced AI until operational workflows are stable.

Reason:
Reliable data and workflows are required before intelligence.

Status:
Accepted
DOC


cat > Documentation/MeridianForge_Control_Center.md <<'DOC'
# MeridianForge Control Center

## Current Sprint

MF-228 MVP Stabilization


## Current Release

v1.28.0-cli-framework


## Completed

MF-100 Foundation
MF-200 Operational MVP


## Active

Documentation control center
Architecture stabilization
Workflow review


## Next

MF-229 Operational MVP Release Candidate


## Reference Documents

- MASTER_ROADMAP.md
- CURRENT_STATUS.md
- ARCHITECTURE_DECISIONS.md
DOC


echo "MF-228 documentation created."
