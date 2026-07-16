#!/bin/bash

set -e

echo "======================================"
echo "Meridian Forge D000.2"
echo "Update Deployment Engine"
echo "======================================"

mkdir -p updates/backups
mkdir -p updates/packages


echo
echo "Updating apply_update.sh..."

cat > scripts/apply_update.sh <<'EOF'
#!/bin/bash

set -e

PACKAGE="$1"
MODE="${2:-apply}"

if [ -z "$PACKAGE" ]; then
    echo "Usage:"
    echo "./scripts/apply_update.sh <package_name> [apply|dry-run]"
    exit 1
fi


UPDATE_DIR="updates/packages/$PACKAGE"

if [ ! -d "$UPDATE_DIR" ]; then
    echo "ERROR:"
    echo "Update package not found:"
    echo "$UPDATE_DIR"
    exit 1
fi


if [ ! -f "$UPDATE_DIR/manifest.txt" ]; then
    echo "ERROR:"
    echo "Missing manifest.txt"
    exit 1
fi


if [ ! -d "$UPDATE_DIR/files" ]; then
    echo "ERROR:"
    echo "Missing files directory"
    exit 1
fi


echo
echo "======================================"
echo "Meridian Forge Update Engine"
echo "======================================"

echo
echo "Package:"
echo "$PACKAGE"

echo
echo "Mode:"
echo "$MODE"


if [ "$MODE" = "dry-run" ]; then

    echo
    echo "Files that would be deployed:"
    find "$UPDATE_DIR/files" -type f

    exit 0

fi


BACKUP_DIR="updates/backups/$(date +"%Y%m%d_%H%M%S")"

echo
echo "Creating backup:"
echo "$BACKUP_DIR"

mkdir -p "$BACKUP_DIR"


echo
echo "Deploying files..."


while IFS= read -r FILE
do

    RELATIVE="${FILE#$UPDATE_DIR/files/}"

    TARGET="$RELATIVE"

    if [ -f "$TARGET" ]; then

        mkdir -p "$BACKUP_DIR/$(dirname "$RELATIVE")"

        cp "$TARGET" \
        "$BACKUP_DIR/$RELATIVE"

    fi


    mkdir -p "$(dirname "$TARGET")"

    cp "$FILE" "$TARGET"


done < <(find "$UPDATE_DIR/files" -type f)


echo
echo "Deployment complete."

echo
echo "Running Meridian Forge Quality Gate..."

./scripts/quality_gate.sh


echo
echo "======================================"
echo "Update completed successfully"
echo "Backup:"
echo "$BACKUP_DIR"
echo "======================================"

EOF


chmod +x scripts/apply_update.sh


echo
echo "Updating package creator..."

cat > scripts/create_update_package.sh <<'EOF'
#!/bin/bash

set -e

PACKAGE_NAME="$1"

if [ -z "$PACKAGE_NAME" ]; then
    echo "Usage:"
    echo "./scripts/create_update_package.sh <package>"
    exit 1
fi


PACKAGE="updates/packages/$PACKAGE_NAME"

mkdir -p "$PACKAGE/files"


cat > "$PACKAGE/manifest.txt" <<MANIFEST
Meridian Forge Update Package

Name:
$PACKAGE_NAME

Created:
$(date)

MANIFEST


cat > "$PACKAGE/apply.sh" <<EOF2
#!/bin/bash

echo "Package: $PACKAGE_NAME"
echo "Deployment handled by apply_update.sh"
EOF2


chmod +x "$PACKAGE/apply.sh"


echo
echo "Created:"
echo "$PACKAGE"

EOF


chmod +x scripts/create_update_package.sh


echo
echo "Running quality gate..."

./scripts/quality_gate.sh


echo
echo "======================================"
echo "D000.2 completed successfully"
echo "======================================"

