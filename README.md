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
# Look at the main app
cat app.py

# Look at tests
cat test_app.py

# Look at CI/CD pipeline
cat .github/workflows/ci-cd.yml
```

#### 15-30 min: Run locally
```bash
./setup.sh              # Install everything
python3 app.py          # Start the app
```

Visit: http://localhost:5000 (you'll see a beautiful task manager!)

#### 30-45 min: Test the app
```bash
# Run all tests
python3 -m pytest test_app.py -v

# Check test coverage
python3 -m pytest test_app.py --cov=app

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
# Name it: cicd_starter_kit

# Push your code
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

Open `.github/workflows/ci-cd.yml` and see:

```yaml
# Stage 1: Lint (check code quality)
lint:
  - runs: flake8 app.py test_app.py

# Stage 2: Test (run all tests)
test:
  - runs: pytest test_app.py -v

# Stage 3: Build (create Docker image)
build:
  - runs: docker build -t cicd-app .

# Stage 4: Deploy (send to production)
deploy:
  - runs: deploy to server

# Stage 5: Notify (report results)
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

### Stage 1: Lint (Code Quality)
```yaml
- name: Lint with flake8
  run: flake8 app.py test_app.py
```
**What it does:** Checks for code style issues  
**Why:** Keeps code clean and readable  
**When it runs:** Every push

### Stage 2: Test (Automated Testing)
```yaml
- name: Test with pytest
  run: pytest test_app.py -v --cov=app
```
**What it does:** Runs all 13 tests  
**Why:** Ensures nothing breaks  
**When it runs:** After lint passes  
**Matrix:** Tests on Python 3.8, 3.9, 3.10

### Stage 3: Build (Docker Image)
```yaml
- name: Build Docker image
  run: docker build -t cicd-app .
```
**What it does:** Creates a container image  
**Why:** Package app with all dependencies  
**When it runs:** After tests pass

### Stage 4: Deploy (Production)
```yaml
- name: Deploy to production
  run: # deployment commands
```
**What it does:** Pushes to live server  
**Why:** Make changes available to users  
**When it runs:** After build succeeds (only on main branch)

### Stage 5: Notify (Results)
```yaml
- name: Notify results
  run: echo "Pipeline completed!"
```
**What it does:** Reports success/failure  
**Why:** Keep team informed  
**When it runs:** Always (even if previous stages fail)

---

## 🧪 Hands-On Exercises

### Exercise 1: Trigger Your First Pipeline

1. Make a small change:
```bash
echo "# CI/CD is awesome!" >> README.md
```

2. Push it:
```bash
git add .
git commit -m "Test CI/CD pipeline"
git push
```

3. Watch in GitHub Actions tab!

**Expected:** All stages pass ✅

### Exercise 2: Break the Tests (Intentionally!)

1. Edit `test_app.py`, change line 13:
```python
# Change from:
assert response.status_code == 200
# To:
assert response.status_code == 404
```

2. Push it:
```bash
git add .
git commit -m "Break tests intentionally"
git push
```

3. Watch pipeline **fail** ❌

**What you'll see:** Test stage fails, deploy stage skips

4. Fix it and push again → Pipeline passes ✅

### Exercise 3: Add New Feature

1. Add new endpoint to `app.py`:
```python
@app.route('/about')
def about():
    return jsonify({
        'app': 'Task Manager',
        'version': '1.0.0',
        'author': 'Your Name'
    })
```

2. Add test to `test_app.py`:
```python
def test_about_endpoint(self):
    response = self.client.get('/about')
    self.assertEqual(response.status_code, 200)
    data = response.get_json()
    self.assertEqual(data['app'], 'Task Manager')
```

3. Push and watch pipeline test your new feature!

---

## 🚀 Deployment Options

### Option 1: Heroku (Easiest)

```bash
# Install Heroku CLI
# Visit: https://devcenter.heroku.com/articles/heroku-cli

# Login and create app
heroku login
heroku create your-app-name

# Deploy
git push heroku main

# Open app
heroku open
```

**See `DEPLOYMENT.md` for complete Heroku guide with screenshots!**

### Option 2: Docker Hub

```bash
# Build and tag
docker build -t yourusername/cicd-app .

# Login to Docker Hub
docker login

# Push
docker push yourusername/cicd-app
```

### Option 3: AWS, Azure, GCP

Add deployment secrets to GitHub:
1. Go to repo Settings → Secrets → Actions
2. Add: `DEPLOY_KEY`, `SERVER_HOST`, etc.
3. Pipeline will auto-deploy on push to main

**See `DEPLOYMENT.md` for step-by-step guides for all platforms!**

---

## 🐛 Troubleshooting

### "Module not found" error
```bash
# Solution: Run setup script
./setup.sh
```

### Tests fail locally
```bash
# Check Python version (need 3.8+)
python3 --version

# Reinstall dependencies
python3 -m pip install -r requirements.txt

# Run tests with verbose output
python3 -m pytest test_app.py -v
```

### Pipeline fails on GitHub
1. Check Actions tab → Click on failed run
2. Read the error message
3. Common issues:
   - Syntax error in code
   - Tests failing
   - Missing dependencies

### Docker build fails
```bash
# Check Docker is running
docker --version

# Try building with more output
docker build -t cicd-app . --progress=plain
```

### Port 5000 already in use
```bash
# Find process using port 5000
lsof -i :5000

# Kill it
kill -9 <PID>

# Or use different port
python3 app.py  # then edit app.py to use port 8000
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

**See `CHEATSHEET.md` for 100+ more commands!**

### API Endpoints

```bash
# Health check
curl http://localhost:5000/health

# Get all tasks
curl http://localhost:5000/tasks

# Get specific task
curl http://localhost:5000/tasks/1

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
- [ ] Add input validation
- [ ] Set up staging environment
- [ ] Add integration tests

### Long-term (Next 3 Months)
- [ ] Learn Kubernetes for orchestration
- [ ] Add monitoring (Prometheus, Grafana)
- [ ] Implement blue-green deployment
- [ ] Add performance testing
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

## 💡 Tips for Success

1. **Take your time** - Don't rush through exercises
2. **Experiment** - Break things, fix them, learn!
3. **Read logs** - Pipeline errors tell you exactly what's wrong
4. **Ask questions** - Search GitHub/Stack Overflow
5. **Build something real** - Modify this to solve your own problem

---

**Made with ❤️ for developers learning CI/CD**

Start your journey now: `./setup.sh` 🚀
