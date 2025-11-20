# Setup Guide

Get your development environment ready for the CI/CD workshop.

---

## Prerequisites

### Required Software

1. **Python 3.8+**
   ```bash
   python3 --version  # Should show 3.8 or higher
   ```
   
   **Don't have it?** Download from [python.org](https://www.python.org/downloads/)

2. **Git**
   ```bash
   git --version
   ```
   
   **Don't have it?** Download from [git-scm.com](https://git-scm.com/downloads)

3. **GitHub Account**
   
   **Don't have one?** Sign up at [github.com](https://github.com/signup)

### Optional (but recommended)

4. **Docker** (for Hour 1, Step 4)
   ```bash
   docker --version
   ```
   
   **Don't have it?** Download from [docker.com](https://www.docker.com/get-started)
   
   *Note: You can skip Docker parts and still complete the workshop*

5. **Code Editor**
   - VS Code (recommended)
   - PyCharm
   - Sublime Text
   - Or any editor you prefer

---

## Quick Setup

### Option 1: Automated Setup (Recommended)

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/cicd_starter_kit.git
cd cicd_starter_kit

# Run setup script
./setup.sh

# You're ready! Start Hour 1
```

The setup script will:
- ✅ Check Python version
- ✅ Create virtual environment
- ✅ Install dependencies
- ✅ Verify installation

---

### Option 2: Manual Setup

```bash
# 1. Clone repository
git clone https://github.com/YOUR_USERNAME/cicd_starter_kit.git
cd cicd_starter_kit

# 2. Create virtual environment
python3 -m venv venv

# 3. Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Verify installation
python3 -c "import flask; import pytest; print('✅ All good!')"
```

---

## Verify Your Setup

Run these commands to make sure everything works:

```bash
# 1. Check Python
python3 --version
# Expected: Python 3.8.0 or higher

# 2. Check Flask
python3 -c "import flask; print(flask.__version__)"
# Expected: 2.x.x or higher

# 3. Check pytest
python3 -c "import pytest; print(pytest.__version__)"
# Expected: 7.x.x or higher

# 4. Check Docker (optional)
docker --version
# Expected: Docker version 20.x.x or higher
```

If all commands work, you're ready! 🎉

---

## Troubleshooting

### "python3: command not found"

**Solution:** Install Python from [python.org](https://www.python.org/downloads/)

On macOS with Homebrew:
```bash
brew install python3
```

---

### "Permission denied: ./setup.sh"

**Solution:** Make the script executable
```bash
chmod +x setup.sh
./setup.sh
```

---

### "pip: command not found"

**Solution:** Use python3 -m pip instead
```bash
python3 -m pip install -r requirements.txt
```

---

### Virtual environment issues

**Solution:** Delete and recreate
```bash
rm -rf venv
python3 -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

---

### Docker not working

**Don't worry!** Docker is optional. You can:
- Skip Docker parts (Hour 1, Step 4)
- Continue with the rest of the workshop
- Come back to Docker later

---

## What's Installed?

The setup installs these Python packages:

```
Flask==2.3.0          # Web framework
pytest==7.4.0         # Testing framework
pytest-cov==4.1.0     # Test coverage
requests==2.31.0      # HTTP library
```

All lightweight, standard tools. Total size: ~50MB

---

## Next Steps

✅ Setup complete? **[Start Hour 1 →](hour-1/README.md)**

Still having issues? [Open an issue](https://github.com/anugurthi/cicd_starter_kit/issues) and we'll help!

---

## System Requirements

- **OS:** macOS, Linux, or Windows
- **RAM:** 2GB minimum, 4GB recommended
- **Disk:** 500MB free space
- **Internet:** Required for initial setup and Hour 2

---

**Ready?** [Begin the workshop →](hour-1/README.md)
