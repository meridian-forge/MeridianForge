# MF-331 Underwriting Consolidation Plan

## Objective

Consolidate duplicate underwriting implementations into one canonical engine.

## Current State

Duplicate engines exist:

- meridianforge.analysis.underwriting_engine
- meridianforge.engine.underwriting_engine

## Canonical Owner

meridianforge.engine.underwriting_engine

## Canonical Result

meridianforge.models.results.analysis_result.AnalysisResult

## Migration Rules

1. Preserve all existing behavior.
2. Maintain test coverage.
3. Convert legacy modules into adapters before removal.
4. Remove duplicates only after validation.

## Target Architecture

engine
 |
 v
UnderwritingEngine
 |
 v
models.results.AnalysisResult

services, workflows, reporting consume canonical outputs.
