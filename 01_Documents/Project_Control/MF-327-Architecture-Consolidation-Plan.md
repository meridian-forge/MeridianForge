# MF-327 Architecture Consolidation Plan

## Purpose

This document defines the controlled consolidation strategy for MeridianForge architecture after completion of MF-326.

The objective is to reduce duplicate implementations, establish canonical ownership boundaries, and simplify long-term maintenance without reducing existing functionality.

Current system status:

- Production modules: 297
- Test functions: 234
- Test coverage baseline: ~89%
- Architecture guardrails: active

---

# 1. Consolidation Principles

## Rule 1 — One Capability, One Owner

Each major business capability must have one canonical implementation.

Duplicate implementations may temporarily exist during migration but must have:

- documented owner
- migration path
- removal criteria

---

## Rule 2 — Preserve Behavior Before Refactoring

No consolidation change may:

- alter business calculations
- remove supported workflows
- reduce test coverage
- break existing CLI behavior

All migrations must pass:

```bash
pytest
