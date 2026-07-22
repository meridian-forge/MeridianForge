# MF-332 AnalysisResult Consolidation Plan

## Purpose

Establish clear ownership of analysis result models after MF-331 underwriting consolidation.

## Current State

Multiple AnalysisResult classes exist:

- meridianforge.analysis.result.AnalysisResult
- meridianforge.analysis.models.AnalysisResult
- meridianforge.workflow.result.AnalysisResult
- meridianforge.models.results.analysis_result.AnalysisResult

## Canonical Ownership

The canonical underwriting result is:

meridianforge.models.results.analysis_result.AnalysisResult

## Consolidation Rules

1. Preserve behavior before refactoring.
2. Rename ambiguous models before deletion.
3. Maintain test coverage.
4. Remove duplicate ownership only after migration.

## Target Architecture

AnalysisResult
    |
    +-- underwriting output

WorkflowResult
    |
    +-- orchestration state

RankingResult
    |
    +-- scoring and ranking output

## Migration Sequence

1. Create replacement names.
2. Update imports.
3. Run full test suite.
4. Remove obsolete classes.

