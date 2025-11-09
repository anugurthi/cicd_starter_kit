#!/bin/bash

# CI/CD Starter Kit - Automated Setup Script
# This script helps you get started quickly

set -e  # Exit on error

echo ""
echo "╔════════════════════════════════════════════════════════════════╗"
echo "║                                                                ║"
echo "║          🚀 CI/CD STARTER KIT - AUTOMATED SETUP 🚀            ║"
echo "║                                                                ║"
echo "║              Learn CI/CD in 2 Hours! (Beginner-Friendly)      ║"
echo "║                                                                ║"
echo "╚════════════════════════════════════════════════════════════════╝"
echo ""
echo "This script will:"
echo "  ✓ Check your Python installation"
echo "  ✓ Create a virtual environment"
echo "  ✓ Install all dependencies"
echo "  ✓ Run tests to verify everything works"
echo ""
echo "Estimated time: 3-5 minutes"
echo ""
echo "════════════════════════════════════════════════════════════════"
echo ""

# Check Python installation
echo "📋 Step 1: Checking Python installation..."
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version)
    echo "✅ Found: $PYTHON_VERSION"
else
    echo "❌ Python 3 is not installed. Please install Python 3.8 or higher."
    echo "   Visit: https://www.python.org/downloads/"
    exit 1
fi

# Check Git installation
echo ""
echo "📋 Step 2: Checking Git installation..."
if command -v git &> /dev/null; then
    GIT_VERSION=$(git --version)
    echo "✅ Found: $GIT_VERSION"
else
    echo "❌ Git is not installed. Please install Git."
    echo "   Visit: https://git-scm.com/downloads"
    exit 1
fi

# Create virtual environment
echo ""
echo "📋 Step 3: Creating virtual environment..."
if [ -d "venv" ]; then
    echo "⚠️  Virtual environment already exists. Skipping..."
else
    python3 -m venv venv
    echo "✅ Virtual environment created"
fi

# Activate virtual environment
echo ""
echo "📋 Step 4: Activating virtual environment..."
source venv/bin/activate
echo "✅ Virtual environment activated"

# Upgrade pip
echo ""
echo "📋 Step 5: Upgrading pip..."
python3 -m pip install --upgrade pip
echo "✅ pip upgraded"

# Install dependencies
echo ""
echo "📋 Step 6: Installing dependencies..."
python3 -m pip install -r requirements.txt
echo "✅ Dependencies installed"

# Run tests
echo ""
echo "📋 Step 7: Running tests..."
python3 -m pytest test_app.py -v
if [ $? -eq 0 ]; then
    echo "✅ All tests passed!"
else
    echo "⚠️  Some tests failed. Please review the errors above."
fi

# Summary
echo ""
echo "======================================"
echo "🎉 Setup Complete!"
echo "======================================"
echo ""
echo "✅ Virtual environment created and activated"
echo "✅ Python packages installed"
echo "✅ Tests executed"
echo ""
echo "📚 Next steps:"
echo ""
echo "1️⃣  Start the application:"
echo "   $ python3 app.py"
echo ""
echo "2️⃣  Visit in your browser:"
echo "   http://localhost:5000"
echo ""
echo "3️⃣  Follow the 2-hour learning roadmap:"
echo "   Open README.md and scroll to '2-HOUR LEARNING ROADMAP'"
echo ""
echo "4️⃣  Need quick commands?"
echo "   Check CHEATSHEET.md"
echo ""
echo "======================================"
echo "💡 Pro Tip: Start with README.md!"
echo "======================================"
echo ""
echo "Happy learning! 🚀"
