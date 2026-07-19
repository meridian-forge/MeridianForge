# MF-226 Repository Architecture Stabilization

Version:
MF-226.0

Date:
2026-07-19

## Purpose

This document records the architecture review performed after MVP stabilization.

The objective was to identify duplicate modules, remove unnecessary duplication concerns, and document intentional domain boundaries.

---

# Python Module Boundary Decisions

## File Readers

MeridianForge contains two FileReader implementations.

### importers.FileReader

Location:

src/meridianforge/importers/file_reader.py

Purpose:

Low-level source extraction.

Responsibilities:

- CSV reading
- XLSX reading
- XLSM reading
- Raw record extraction

Output:

list[dict]

---

### imports.FileReader

Location:

src/meridianforge/imports/file_reader.py

Purpose:

Application import workflow.

Responsibilities:

- Supported file validation
- Import execution tracking
- ImportResult generation

Output:

ImportResult

---

Decision:

Both implementations remain.

They represent different architectural layers.

Future rename may improve clarity.

---

# Normalization Boundaries

MeridianForge intentionally separates three normalization responsibilities.

---

## data.PropertyNormalizer

Purpose:

Source-specific property cleanup.

Responsibilities:

- Convert price fields
- Convert rent fields
- Normalize basic property attributes

---

## normalization.Normalizer

Purpose:

Generic schema normalization.

Responsibilities:

- Apply field mappings
- Convert external schemas into canonical assets

---

## opportunity.normalizer

Purpose:

Business classification.

Responsibilities:

- Convert extracted data into opportunities
- Determine opportunity type
- Assign confidence

---

Decision:

No consolidation required.

The layers represent different responsibilities.

---

# General Architecture Principles

MeridianForge follows a layered architecture:

External Sources

↓

Import / Extraction

↓

Normalization

↓

Domain Models

↓

Analysis

↓

Ranking

↓

Reporting

↓

User Interface

---

# Future Cleanup Candidates

Post-MVP improvements:

1. Rename data.PropertyNormalizer to PropertyAdapter.
2. Improve FileReader naming clarity.
3. Organize historical build scripts.

These changes are deferred to avoid unnecessary MVP regression risk.

---

# Status

MF-226 audit completed.

No functional refactoring performed.

Test baseline preserved:

178 passing tests.
