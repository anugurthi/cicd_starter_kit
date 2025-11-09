# CI/CD Starter Kit - Quick Reference Cheat Sheet

## 🚀 Essential Commands

### Local Development
```bash
# Setup
python3 -m venv venv                    # Create virtual environment
source venv/bin/activate                # Activate (macOS/Linux)
venv\Scripts\activate                   # Activate (Windows)
python3 -m pip install --upgrade pip    # Upgrade pip
python3 -m pip install -r requirements.txt  # Install dependencies

# Run Application
python3 app.py                          # Start Flask server
# Visit: http://localhost:5000

# Testing
python3 -m pytest test_app.py           # Run all tests
python3 -m pytest test_app.py -v        # Verbose output
python3 -m pytest test_app.py -v --cov=app  # With coverage
python3 -m pytest test_app.py::TestFlaskApp::test_home_endpoint  # Single test
```

### Docker Commands
```bash
# Build & Run
docker build -t cicd-app .              # Build image
docker run -p 5000:5000 cicd-app        # Run container
docker run -d -p 5000:5000 --name my-app cicd-app  # Run detached

# Management
docker ps                               # List running containers
docker ps -a                            # List all containers
docker logs my-app                      # View logs
docker stop my-app                      # Stop container
docker rm my-app                        # Remove container
docker images                           # List images
docker rmi cicd-app                     # Remove image

# Docker Compose
docker-compose up                       # Start services
docker-compose up -d                    # Start detached
docker-compose down                     # Stop services
docker-compose logs -f                  # Follow logs
```

### Git Commands
```bash
# Initial Setup
git init                                # Initialize repository
git add .                               # Stage all files
git commit -m "Initial commit"          # Commit changes
git branch -M main                      # Rename to main
git remote add origin <url>             # Add remote
git push -u origin main                 # Push to GitHub

# Regular Workflow
git status                              # Check status
git add .                               # Stage changes
git commit -m "message"                 # Commit
git push                                # Push to remote
git pull                                # Pull from remote
git log --oneline                       # View history
```

### API Testing with curl
```bash
# GET Requests
curl http://localhost:5000/                        # Home
curl http://localhost:5000/health                  # Health check
curl http://localhost:5000/tasks                   # Get all tasks
curl http://localhost:5000/tasks/1                 # Get task by ID

# POST Request (Create Task)
curl -X POST http://localhost:5000/tasks \
  -H "Content-Type: application/json" \
  -d '{"title": "Learn CI/CD", "completed": false}'

# PUT Request (Update Task)
curl -X PUT http://localhost:5000/tasks/1 \
  -H "Content-Type: application/json" \
  -d '{"title": "Master CI/CD", "completed": true}'

# DELETE Request
curl -X DELETE http://localhost:5000/tasks/1

# Pretty print JSON
curl http://localhost:5000/tasks | python -m json.tool
```

---

## 📊 CI/CD Pipeline Stages

```
┌──────────────┐
│   1. LINT    │  ← Check code quality (flake8)
└──────┬───────┘
       │
       ▼
┌──────────────┐
│   2. TEST    │  ← Run unit tests (pytest)
└──────┬───────┘    Test on Python 3.8, 3.9, 3.10
       │
       ▼
┌──────────────┐
│   3. BUILD   │  ← Build Docker image
└──────┬───────┘    Test container
       │
       ▼
┌──────────────┐
│   4. DEPLOY  │  ← Deploy to production
└──────┬───────┘    (only from main branch)
       │
       ▼
┌──────────────┐
│   5. NOTIFY  │  ← Send status notifications
└──────────────┘
```

---

## 🗂️ Project Structure
```
cicd_starter_kit/
├── app.py                   # Flask application (main code)
├── test_app.py              # Unit tests
├── requirements.txt         # Python dependencies
├── Dockerfile               # Docker configuration
├── docker-compose.yml       # Docker Compose setup
├── Procfile                 # Heroku configuration
├── .gitignore              # Git ignore rules
├── README.md               # Complete guide
├── QUICKSTART.md           # Quick start guide
├── ROADMAP.md              # 2-hour learning plan
├── DEPLOYMENT.md           # Deployment guides
├── CHEATSHEET.md           # This file
├── setup.sh                # Automated setup script
└── .github/
    └── workflows/
        └── ci-cd.yml       # CI/CD pipeline definition
```

---

## 🔑 Key Concepts

### CI/CD Terms
- **CI**: Continuous Integration - Automatically test code changes
- **CD**: Continuous Delivery/Deployment - Automatically deploy tested code
- **Pipeline**: Series of automated steps (lint → test → build → deploy)
- **Job**: Independent task in pipeline
- **Step**: Individual command in a job
- **Artifact**: Output from a job (e.g., Docker image)

### GitHub Actions Syntax
```yaml
name: Pipeline Name          # Display name

on: [push, pull_request]     # Trigger events

jobs:                        # Define jobs
  test:                      # Job name
    runs-on: ubuntu-latest   # OS to run on
    steps:                   # Steps in job
      - uses: actions/checkout@v3        # Use action
      - run: pytest test_app.py          # Run command
```

### Docker Concepts
- **Image**: Blueprint for container
- **Container**: Running instance of image
- **Dockerfile**: Instructions to build image
- **Layer**: Each instruction in Dockerfile
- **Registry**: Storage for images (Docker Hub)

---

## 🎯 Common Workflows

### Workflow 1: Making Changes
```bash
# 1. Make code changes
vim app.py

# 2. Test locally
pytest test_app.py -v

# 3. Run app to verify
python app.py

# 4. Commit and push
git add .
git commit -m "Add new feature"
git push

# 5. Check GitHub Actions
# Go to: https://github.com/USERNAME/REPO/actions
```

### Workflow 2: Fixing Failed Pipeline
```bash
# 1. Check logs in GitHub Actions
# Click on failed job → Read error

# 2. Fix locally
# Edit files based on error

# 3. Test fix
pytest test_app.py -v

# 4. Push fix
git add .
git commit -m "Fix failing test"
git push
```

### Workflow 3: Adding New Feature
```bash
# 1. Create feature branch
git checkout -b feature/new-endpoint

# 2. Add code
# Edit app.py

# 3. Add test
# Edit test_app.py

# 4. Test locally
pytest test_app.py -v

# 5. Commit and push
git add .
git commit -m "Add new endpoint"
git push -u origin feature/new-endpoint

# 6. Create Pull Request on GitHub
# 7. Pipeline runs automatically
# 8. Merge when green ✅
```

---

## 🐛 Troubleshooting Quick Fixes

### Error: Port 5000 in use
```bash
# Find process
lsof -i :5000

# Kill process
kill -9 <PID>

# Or use different port in app.py
app.run(port=5001)
```

### Error: Module not found
```bash
# Ensure virtual environment is activated
source venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

### Error: Tests failing
```bash
# Run with verbose output
pytest test_app.py -vv

# Run specific test
pytest test_app.py::TestFlaskApp::test_home_endpoint -v

# Check Python version
python --version  # Should be 3.8+
```

### Error: Docker build fails
```bash
# Clear cache and rebuild
docker system prune -a
docker build --no-cache -t cicd-app .
```

### Error: GitHub Actions not triggering
```bash
# Check workflow file location
ls .github/workflows/ci-cd.yml

# Validate YAML syntax
# Visit: http://www.yamllint.com/
# Paste contents of ci-cd.yml

# Check if Actions enabled
# GitHub repo → Settings → Actions → Enabled
```

---

## 📈 Monitoring & Logs

### View Logs
```bash
# Flask app logs
python app.py  # Logs to console

# Docker logs
docker logs my-app
docker logs -f my-app  # Follow logs

# Heroku logs
heroku logs --tail

# GitHub Actions logs
# Click on workflow run → Click on job → Click on step
```

### Health Checks
```bash
# Check if app is running
curl http://localhost:5000/health

# Expected response:
# {"status": "healthy", "timestamp": "..."}

# In Docker
curl http://localhost:5000/health

# In production (replace with your URL)
curl https://your-app.herokuapp.com/health
```

---

## 🚀 Deployment Commands

### Heroku
```bash
heroku login                           # Login
heroku create app-name                 # Create app
git push heroku main                   # Deploy
heroku open                            # Open app
heroku logs --tail                     # View logs
heroku ps:scale web=1                  # Scale dynos
heroku config:set KEY=value            # Set env var
```

### Docker Hub
```bash
docker login                           # Login
docker tag cicd-app user/cicd-app     # Tag image
docker push user/cicd-app             # Push image
docker pull user/cicd-app             # Pull image
```

### AWS Elastic Beanstalk
```bash
eb init                                # Initialize
eb create prod-env                     # Create environment
eb deploy                              # Deploy
eb open                                # Open app
eb logs                                # View logs
```

---

## 💡 Pro Tips

1. **Always test locally before pushing**
   ```bash
   pytest test_app.py -v && git push
   ```

2. **Use Git aliases for faster workflow**
   ```bash
   git config --global alias.cm "commit -m"
   git config --global alias.st "status"
   # Now use: git cm "message" instead of git commit -m "message"
   ```

3. **Watch file changes during development**
   ```bash
   # Install watchdog
   pip install watchdog
   
   # Run with auto-reload
   FLASK_ENV=development python app.py
   ```

4. **Quick Docker cleanup**
   ```bash
   docker system prune -a  # Remove all unused images
   ```

5. **Test specific functionality**
   ```bash
   pytest test_app.py -k "health"  # Run tests with "health" in name
   ```

---

## 📚 Learning Path

### Beginner (You are here!)
- [x] Understand CI/CD concepts
- [x] Run application locally
- [x] Run tests
- [x] Set up GitHub Actions

### Intermediate (Next)
- [ ] Add database (PostgreSQL)
- [ ] Add authentication
- [ ] Add more tests
- [ ] Deploy to production

### Advanced (Future)
- [ ] Kubernetes deployment
- [ ] Blue-green deployment
- [ ] Monitoring with Prometheus
- [ ] Infrastructure as Code (Terraform)

---

## 🔗 Useful Links

- **GitHub Actions Docs**: https://docs.github.com/en/actions
- **Flask Docs**: https://flask.palletsprojects.com/
- **Docker Docs**: https://docs.docker.com/
- **Pytest Docs**: https://docs.pytest.org/
- **Heroku Docs**: https://devcenter.heroku.com/

---

## 📞 Getting Help

1. **Check documentation**: README.md, ROADMAP.md, DEPLOYMENT.md
2. **Search GitHub Issues**: Might be already answered
3. **Create new issue**: Describe problem with logs
4. **Stack Overflow**: Tag with `flask`, `github-actions`, `docker`

---

**Last Updated**: November 2025  
**Keep this handy while learning!** 📌
