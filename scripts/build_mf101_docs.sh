#!/bin/bash

set -e

echo
echo "======================================"
echo "MF-101 DOCUMENTATION BUILD"
echo "======================================"
echo

ROOT="$(pwd)"

DOC_ROOT="$ROOT/Documentation"

ARCH="$DOC_ROOT/Architecture"
DECISIONS="$DOC_ROOT/Decisions"
RELEASES="$DOC_ROOT/Releases"

echo "Creating documentation structure..."

mkdir -p "$ARCH"
mkdir -p "$DECISIONS"
mkdir -p "$RELEASES"


echo
echo "Checking MF-101 documentation files..."
echo


FILES=(
"Architecture/MF-101-Operational-MVP-Architecture.md"
"Architecture/MF-101.2-Domain-Model.md"
"Architecture/MF-101.3-CLI-Design.md"
"Architecture/MF-101.4-Repository-Structure.md"
"Architecture/MF-101.5-Data-Model.md"
"Architecture/MF-101.6-Build-Sequence.md"
"Decisions/ADR-001-Opportunity-Core-Entity.md"
"Decisions/ADR-002-JSON-Storage-First.md"
"Decisions/ADR-003-Separate-Engine-and-Workflow.md"
"Releases/MVP-v1.0.0.md"
)


MISSING=0


for FILE in "${FILES[@]}"
do

    if [ -f "$DOC_ROOT/$FILE" ]
    then
        echo "FOUND: $FILE"
    else
        echo "MISSING: $FILE"
        MISSING=$((MISSING+1))
    fi

done


echo

if [ "$MISSING" -gt 0 ]
then

    echo "======================================"
    echo "MF-101 DOCUMENTATION INCOMPLETE"
    echo "Missing files: $MISSING"
    echo "======================================"
    exit 1

fi


echo "======================================"
echo "MF-101 DOCUMENTATION COMPLETE"
echo "======================================"

echo
echo "Next recommended commands:"
echo
echo "git add Documentation"
echo "git commit -m \"Add MF-101 operational MVP architecture documentation\""
echo
