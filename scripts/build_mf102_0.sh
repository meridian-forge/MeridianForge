#!/bin/bash

set -e

PACKAGE="updates/packages/MF-102.0"

echo
echo "======================================"
echo "MF-102.0 PACKAGE BUILDER"
echo "======================================"
echo

rm -rf "$PACKAGE"

mkdir -p \
"$PACKAGE/files/src/meridianforge/domain" \
"$PACKAGE/files/src/meridianforge/repositories" \
"$PACKAGE/files/tests/domain"


cat > "$PACKAGE/manifest.txt" <<EOF
MF-102.0
Operational Foundation

Files:
- Opportunity domain
- Source domain
- Provider domain
- Opportunity status
- Repository abstraction
- Domain tests
EOF


cat > "$PACKAGE/release_notes.md" <<EOF
# MF-102.0 Operational Foundation

Adds the foundation for Meridian Forge operational workflows.

Included:

- Opportunity lifecycle model
- Source tracking model
- Provider model
- JSON repository abstraction
- Domain tests
EOF


cat > "$PACKAGE/apply.sh" <<EOF
#!/bin/bash

echo "MF-102.0 package ready for installation"
EOF

chmod +x "$PACKAGE/apply.sh"


echo
echo "======================================"
echo "MF-102.0 PACKAGE CREATED"
echo "======================================"
echo "$PACKAGE"