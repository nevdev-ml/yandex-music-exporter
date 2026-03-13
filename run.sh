#!/usr/bin/env bash
set -e

check_python() {
    "$@" -c "import sys" >/dev/null 2>&1
}

if command -v python >/dev/null 2>&1 && check_python python; then
    PYTHON=python
elif command -v python3 >/dev/null 2>&1 && check_python python3; then
    PYTHON=python3
elif command -v py >/dev/null 2>&1 && check_python py -3; then
    PYTHON="py -3"
else
    echo "Working Python interpreter not found."
    exit 1
fi

echo "Using Python: $PYTHON"

VENV=".venv"

if [ ! -d "$VENV" ]; then
echo "Creating virtual environment..."
$PYTHON -m venv $VENV
fi


if [ -f "$VENV/Scripts/activate" ]; then
source "$VENV/Scripts/activate"
else
source "$VENV/bin/activate"
fi

echo "Upgrading pip..."
python -m pip install --upgrade pip

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Running exporter..."
python yandex_music_export.py

echo
read -p "Press Enter to exit..."