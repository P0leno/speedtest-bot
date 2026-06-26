#!/bin/bash
set -e

echo "=== SpeedTest Bot Installer ==="

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 not found. Install it first."
    exit 1
fi

# Install deps
python3 -m pip install -q -r requirements.txt

echo "✅ Dependencies installed."
echo "🚀 Starting bot..."
python3 bot.py
