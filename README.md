# 🚀 CI/CD Starter Kit - Learn CI/CD in 2 Hours

A complete hands-on project to learn Continuous Integration & Continuous Deployment with a real Flask application.

---

## 🏃 Quick Start (5 Minutes)

```bash
# 1. Run setup (installs everything)
./setup.sh

# 2. Start the app
python3 app.py

# 3. Open browser: http://localhost:5000
```

**Done!** Your task manager app is running with a beautiful UI.

---

## 📚 What You'll Learn

- ✅ What CI/CD is and why it matters
- ✅ How to write automated tests
- ✅ How to set up a CI/CD pipeline with GitHub Actions
- ✅ How to containerize apps with Docker
- ✅ How to deploy to production

---

## 🤔 What is CI/CD?

### Continuous Integration (CI)
**Automatically test your code every time you push changes**

```
You push code → GitHub Actions runs tests → Get instant feedback ✅
```

**Why?** Catch bugs early before they reach production!

### Continuous Deployment (CD)
**Automatically deploy your code after tests pass**

```
Tests pass → Build Docker image → Deploy to server → Users see changes 🎉
```

**Why?** Release features faster with confidence!

### Real Flow
```
Write code → git push → Tests run → Build → Deploy → Live! ✨
(All automatic, no manual work!)
```

---

## ⏱️ 2-Hour Learning Path

### **Hour 1: Local Development**

#### 0-15 min: Understand the project
```bash
cat app.py              # Look at the main app
cat test_app.py         # Look at tests
cat .github/workflows/ci-cd.yml  # Look at CI/CD pipeline
```

#### 15-30 min: Run locally
```bash
./setup.sh              # Install everything
python3 app.py          # Start the app
```
Visit: http://localhost:5000

#### 30-45 min: Test the app
```bash
python3 -m pytest test_app.py -v              # Run all tests
python3 -m pytest test_app.py --cov=app       # Check coverage
# You should see: 13 tests passed ✅
```

#### 45-60 min: Try the API
```bash
# Health check
curl http://localhost:5000/health

# Get all tasks
curl http://localhost:5000/tasks

# Create a task
curl -X POST http://localhost:5000/tasks \
  -H "Content-Type: application/json" \
  -d '{"title": "Learn CI/CD", "completed": false}'
```

### **Hour 2: CI/CD Pipeline**

#### 60-75 min: Push to GitHub

```bash
# Create repo on GitHub: https://github.com/new
git init
git add .
git commit -m "Initial commit: Task Manager with CI/CD"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/cicd_starter_kit.git
git push -u origin main
```

#### 75-90 min: Watch CI/CD Pipeline

1. Go to your GitHub repo
2. Click **"Actions"** tab
3. You'll see your pipeline running! 🎉

**Pipeline stages:**
- 🔍 **Lint**: Check code quality
- ✅ **Test**: Run all tests (Python 3.8, 3.9, 3.10)
- 🐳 **Build**: Create Docker image
- 🚀 **Deploy**: Send to production
- 📢 **Notify**: Report results

#### 90-105 min: Understand the Pipeline

The `.github/workflows/ci-cd.yml` file defines your automated pipeline:

```yaml
# Stage 1: Lint - Check code quality
lint:
  - runs: flake8 app.py test_app.py

# Stage 2: Test - Run all tests
test:
  - runs: pytest test_app.py -v

# Stage 3: Build - Create Docker image
build:
  - runs: docker build -t cicd-app .

# Stage 4: Deploy - Send to production
deploy:
  - runs: deploy to server

# Stage 5: Notify - Report results
notify:
  - runs: echo "✅ All good!" or "❌ Failed!"
```

#### 105-120 min: Docker

```bash
# Build Docker image
docker build -t cicd-app .

# Run in container
docker run -p 5000:5000 cicd-app

# Test: http://localhost:5000
```

---

## 🏗️ Project Structure

```
cicd_starter_kit/
├── app.py                    # Flask app with 7 endpoints
├── test_app.py               # 13 unit tests
├── templates/
│   └── index.html            # Beautiful task manager UI
├── requirements.txt          # Python packages
├── Dockerfile                # Docker config
├── docker-compose.yml        # Docker Compose
├── setup.sh                  # One-command setup
├── .github/
│   └── workflows/
│       └── ci-cd.yml        # CI/CD pipeline (5 stages)
├── CHEATSHEET.md            # Quick command reference
├── DEPLOYMENT.md            # Deployment guides (Heroku, AWS, Azure, GCP)
└── README.md                 # This file
```

---

## 🎯 CI/CD Pipeline Explained

Your `.github/workflows/ci-cd.yml` file defines a **5-stage automated pipeline** that runs on every push.

### Pipeline Flow

```
Git Push
   ↓
┌─────────────────────────────────────────────────────┐
│ Stage 1: LINT (Code Quality Check)                  │
│ ✓ Check Python code style with flake8              │
│ ✓ Ensure PEP 8 compliance                          │
└─────────────────────────────────────────────────────┘
   ↓ (only if lint passes)
┌─────────────────────────────────────────────────────┐
│ Stage 2: TEST (Automated Testing)                   │
│ ✓ Run 13 unit tests                                │
│ ✓ Test on Python 3.8, 3.9, 3.10 (matrix)          │
│ ✓ Generate coverage report                         │
└─────────────────────────────────────────────────────┘
   ↓ (only if tests pass)
┌─────────────────────────────────────────────────────┐
│ Stage 3: BUILD (Docker Image)                       │
│ ✓ Build Docker image from Dockerfile               │
│ ✓ Tag with commit SHA                              │
│ ✓ Test image with health check                     │
└─────────────────────────────────────────────────────┘
   ↓ (only if build succeeds + on main branch)
┌─────────────────────────────────────────────────────┐
│ Stage 4: DEPLOY (Production Deployment)             │
│ ✓ Deploy to Heroku / AWS / Azure / GCP            │
│ ✓ Verify deployment success                        │
└─────────────────────────────────────────────────────┘
   ↓ (always runs)
┌─────────────────────────────────────────────────────┐
│ Stage 5: NOTIFY (Status Report)                     │
│ ✓ Report success or failure                        │
│ ✓ Include test results and coverage                │
└─────────────────────────────────────────────────────┘
```

**Total: ~3-5 minutes** from push to production! 🚀

---

## 🧪 Hands-On Exercises

### Exercise 1: Trigger Your First Pipeline

```bash
# 1. Make a small change
echo "# CI/CD is awesome!" >> README.md

# 2. Push it
git add .
git commit -m "Test CI/CD pipeline"
git push

# 3. Watch in GitHub Actions tab!
```

**Expected:** All stages pass ✅

### Exercise 2: Break the Tests (Intentionally!)

1. Edit `test_app.py`, change a test to fail
2. Push it and watch pipeline **fail** ❌
3. Fix it and push again → Pipeline passes ✅

### Exercise 3: Add New Feature

1. Add new endpoint to `app.py`
2. Add test to `test_app.py`
3. Push and watch pipeline test your new feature!

---

## 🚀 Deployment Options

### Quick Comparison

| Platform | Difficulty | Free Tier | Auto-Deploy | Best For |
|----------|-----------|-----------|-------------|----------|
| **Docker Hub** | Easy | ✅ Yes | ✅ CI/CD | Image storage |
| **Heroku** | Easiest | ✅ Yes | ✅ Yes | Quick demos |
| **AWS EC2** | Medium | ✅ Yes | ⚙️ Setup needed | Production |
| **Azure** | Medium | ✅ Yes | ⚙️ Setup needed | Enterprise |
| **GCP Cloud Run** | Easy | ✅ Yes | ⚙️ Setup needed | Serverless |
| **DigitalOcean** | Easy | ✅ $200 credit | ✅ Yes | Startups |

### Recommended Path for Beginners

1. **Start with Docker Hub** → Learn container registry
2. **Deploy to Heroku** → See it live quickly
3. **Try AWS EC2** → Learn servers
4. **Explore others** → Find what fits your needs

**See [`DEPLOYMENT.md`](DEPLOYMENT.md) for detailed guides for each platform!**

---

## 🔐 GitHub Secrets Setup

To enable automated deployment, add these secrets:

**Go to:** `Settings → Secrets and variables → Actions → New repository secret`

### For Docker Hub:
```bash
DOCKER_USERNAME = your-dockerhub-username
DOCKER_PASSWORD = your-dockerhub-access-token
```

**Create Docker Hub Access Token:**
1. Go to: https://hub.docker.com/settings/security
2. Click **"New Access Token"**
3. Description: `GitHub Actions CI/CD`
4. Permissions: Read, Write, Delete
5. Copy token and save as `DOCKER_PASSWORD` secret

### For Heroku:
```bash
HEROKU_API_KEY = $(heroku auth:token)
HEROKU_APP_NAME = your-app-name
HEROKU_EMAIL = your@email.com
```

### For AWS EC2:
```bash
AWS_EC2_HOST = 54.123.45.67
AWS_EC2_USER = ubuntu
AWS_EC2_KEY = (contents of .pem file)
```

---

## 🐛 Troubleshooting

### "Module not found" error
```bash
./setup.sh  # Run setup script
```

### Tests fail locally
```bash
python3 --version  # Check Python version (need 3.8+)
python3 -m pip install -r requirements.txt  # Reinstall dependencies
python3 -m pytest test_app.py -v  # Run tests with verbose output
```

### Pipeline fails on GitHub
1. Check Actions tab → Click on failed run
2. Read the error message
3. Common issues: syntax error, tests failing, missing dependencies

### Docker build fails
```bash
docker --version  # Check Docker is running
docker build -t cicd-app . --progress=plain  # Build with more output
```

### Port 5000 already in use
```bash
lsof -i :5000  # Find process using port 5000
kill -9 <PID>  # Kill it
```

---

## 📝 Quick Command Reference

### Essential Commands

```bash
# Setup
./setup.sh                              # First-time setup

# Development
python3 app.py                          # Run app
python3 -m pytest test_app.py -v       # Run tests
python3 -m pytest --cov=app            # Check coverage

# Docker
docker build -t cicd-app .             # Build image
docker run -p 5000:5000 cicd-app       # Run container
docker ps                               # List containers
docker stop <container-id>              # Stop container

# Git
git status                              # Check changes
git add .                               # Stage all files
git commit -m "message"                 # Commit changes
git push                                # Push to GitHub (triggers CI/CD!)
```

**See [`CHEATSHEET.md`](CHEATSHEET.md) for more commands!**

### API Endpoints

```bash
# Health check
curl http://localhost:5000/health

# Get all tasks
curl http://localhost:5000/tasks

# Create task
curl -X POST http://localhost:5000/tasks \
  -H "Content-Type: application/json" \
  -d '{"title": "My task", "completed": false}'

# Update task
curl -X PUT http://localhost:5000/tasks/1 \
  -H "Content-Type: application/json" \
  -d '{"completed": true}'

# Delete task
curl -X DELETE http://localhost:5000/tasks/1
```

---

## ✅ What You've Built

Congratulations! You now have:

- ✅ A working Flask REST API
- ✅ 13 automated unit tests
- ✅ Beautiful web UI for task management
- ✅ Complete CI/CD pipeline (5 stages)
- ✅ Docker containerization
- ✅ GitHub Actions automation
- ✅ Production-ready deployment setup

### Skills You've Learned

1. **Backend Development**: Flask, REST APIs, routing
2. **Testing**: pytest, unit tests, test coverage
3. **CI/CD**: GitHub Actions, automated pipelines
4. **DevOps**: Docker, containerization, deployment
5. **Git**: Version control, branching, collaboration

---

## 🎯 Next Steps

### Immediate (This Week)
- [ ] Push to GitHub and watch pipeline run
- [ ] Complete all 3 hands-on exercises
- [ ] Deploy to Heroku
- [ ] Add a new feature with tests

### Short-term (This Month)
- [ ] Add database (PostgreSQL or MongoDB)
- [ ] Add user authentication (JWT tokens)
- [ ] Set up staging environment
- [ ] Add integration tests

### Long-term (Next 3 Months)
- [ ] Learn Kubernetes for orchestration
- [ ] Add monitoring (Prometheus, Grafana)
- [ ] Implement blue-green deployment
- [ ] Build mobile app that uses this API

---

## 📚 Additional Resources

### Learn More About CI/CD
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Martin Fowler's CI/CD Guide](https://martinfowler.com/articles/continuousIntegration.html)
- [Docker Getting Started](https://docs.docker.com/get-started/)

### Python & Flask
- [Flask Documentation](https://flask.palletsprojects.com/)
- [pytest Documentation](https://docs.pytest.org/)

### DevOps
- [The Phoenix Project (Book)](https://itrevolution.com/product/the-phoenix-project/)
- [Kubernetes Documentation](https://kubernetes.io/docs/home/)

---

## 🎉 Congratulations!

You've completed the CI/CD Starter Kit! You now understand:

✅ How CI/CD works  
✅ How to write automated tests  
✅ How to set up a pipeline  
✅ How to containerize applications  
✅ How to deploy to production  

**Put this on your resume!** This is a complete, professional CI/CD setup.

**Interview Questions You Can Now Answer:**
- "What is CI/CD?" ✅
- "Have you set up a CI/CD pipeline?" ✅
- "How do you ensure code quality?" ✅
- "What's your experience with Docker?" ✅
- "Can you explain your deployment process?" ✅

---

**Made with ❤️ for developers learning CI/CD**

Start your journey now: `./setup.sh` 🚀

---

## 📞 Support & Community

- 🐛 **Found a bug?** Open an issue on GitHub
- ❓ **Have a question?** Check GitHub Discussions
- 💡 **Want to contribute?** Pull requests welcome!
- 🌟 **Like this project?** Give it a star on GitHub!

**Repository:** https://github.com/anugurthi/cicd_starter_kit
