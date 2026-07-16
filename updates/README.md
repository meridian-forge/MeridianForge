# Meridian Forge Update Framework

## Purpose

Provides a controlled mechanism for applying Meridian Forge upgrades.

## Structure

updates/

packages/
    Individual update packages.

manifests/
    Update metadata.

backups/
    Automatic backups before changes.

## Future Workflow

1. Create update package.
2. Validate manifest.
3. Backup affected files.
4. Apply changes.
5. Run quality gate.
6. Commit and tag release.
