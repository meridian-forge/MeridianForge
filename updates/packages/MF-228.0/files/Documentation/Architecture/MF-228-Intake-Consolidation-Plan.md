# MF-228.0 Intake Architecture Consolidation Plan

## Objective

Establish a single, maintainable intake architecture for Meridian Forge.

The platform currently supports:

- CSV property intake
- Excel property intake
- Manual intake
- External structured data imports

As capabilities expanded, multiple modules evolved with overlapping responsibilities.

This milestone creates clear ownership boundaries.

---

# Current Architecture Review

## File Readers

Current locations:

exit
exit()

