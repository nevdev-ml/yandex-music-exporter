#!/usr/bin/env bash
set -e

# Detect python command

if command -v python >/dev/null 2>&1; then
PYTHON=python
elif command -v python3 >/dev/null 2>&1; then
PYTHON=python3
elif command -v py >/dev/null 2>&1; then
PYTHON="py -3"
else
echo "Python not found. Please install Python."
exit 1
fi

echo "Using Python: $PYTHON"

VENV=".venv"

if [ ! -d "$VENV" ]; then
echo "Creating virtual environment..."
$PYTHON -m venv $VENV
fi

# Activate venv (Windows / Linux compatibility)

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
python main.py
