#!/bin/bash
# =============================================================================
# Veille Tech Agent — Script de lancement rapide pour MacBook
# =============================================================================

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PYTHON="$SCRIPT_DIR/venv/bin/python"

if [ ! -f "$PYTHON" ]; then
    echo "⚙️  Environnement virtuel non initialisé. Lancement de install.sh..."
    "$SCRIPT_DIR/install.sh"
fi

# Raccourcis pratiques
case "$1" in
    daily)
        shift
        exec "$PYTHON" "$SCRIPT_DIR/main.py" --mode daily "$@"
        ;;
    weekly)
        shift
        exec "$PYTHON" "$SCRIPT_DIR/main.py" --mode weekly "$@"
        ;;
    html|multilingual)
        shift
        exec "$PYTHON" "$SCRIPT_DIR/scripts/build_multilingual_page.py" "$@"
        ;;
    configure)
        shift
        exec "$PYTHON" "$SCRIPT_DIR/configure.py" "$@"
        ;;
    *)
        exec "$PYTHON" "$SCRIPT_DIR/main.py" "$@"
        ;;
esac
