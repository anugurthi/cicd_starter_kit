# CI/CD Starter Kit - Quick Reference

## 🚀 Essential Commands

### Setup & Run
```bash
./setup.sh                              # One-time setup
python3 app.py                          # Run app
open http://localhost:5000              # View in browser
```

### Testing
```bash
pytest test_app.py -v                   # Run all tests
pytest test_app.py --cov=app            # With coverage
pytest test_app.py::TestFlaskApp::test_health  # Single test
pytest -k "health"                      # Tests matching "health"
```

### Docker
```bash
# Build & Run
docker build -t cicd-app .              # Build image
docker run -d -p 5000:5000 cicd-app     # Run detached
docker run -p 5000:5000 --name my-app cicd-app  # Run with name

# Management
docker ps                               # List running containers
docker ps -a                            # List all containers
docker logs my-app                      # View logs
docker logs -f my-app                   # Follow logs
docker stop my-app                      # Stop container
docker rm my-app                        # Remove container
docker images                           # List images
docker rmi cicd-app                     # Remove image
docker system prune -a                  # Clean up everything

# Docker Compose
docker-compose up                       # Start services
docker-compose up -d                    # Start detached
docker-compose down                     # Stop services
docker-compose logs -f                  # Follow logs
```

### Git
```bash
# Initial Setup
git init                                # Initialize repo
git add .                               # Stage all files
git commit -m "message"                 # Commit
git branch -M main                      # Rename to main
git remote add origin <url>             # Add remote
git push -u origin main                 # Push to GitHub

# Regular Workflow
git status                              # Check status
git add .                               # Stage changes
git commit -m "message"                 # Commit
git push                                # Push (triggers CI/CD!)
git pull                                # Pull from remote
git log --oneline -5                    # View recent commits

# Branching
git checkout -b feature/new-feature     # Create branch
git checkout main                       # Switch to main
git merge feature/new-feature           # Merge branch
git branch -d feature/new-feature       # Delete branch
```

### API Testing
```bash
# GET Requests
curl http://localhost:5000/             # Home
curl http://localhost:5000/health       # Health check
curl http://localhost:5000/tasks        # Get all tasks
curl http://localhost:5000/tasks/1      # Get task by ID

# POST (Create Task)
curl -X POST http://localhost:5000/tasks \
  -H "Content-Type: application/json" \
  -d '{"title": "Learn CI/CD", "completed": false}'

# PUT (Update Task)
curl -X PUT http://localhost:5000/tasks/1 \
  -H "Content-Type: application/json" \
  -d '{"title": "Master CI/CD", "completed": true}'

# DELETE
curl -X DELETE http://localhost:5000/tasks/1

# Pretty print JSON
curl http://localhost:5000/tasks | python -m json.tool
```

---

## 🚀 Deployment Commands

### Heroku
```bash
heroku login                            # Login
heroku create app-name                  # Create app
git push heroku main                    # Deploy
heroku open                             # Open app
heroku logs --tail                      # View logs
heroku ps:scale web=1                   # Scale dynos
heroku config:set KEY=value             # Set env var
```

### Docker Hub
```bash
docker login                            # Login
docker tag cicd-app user/cicd-app       # Tag image
docker push user/cicd-app               # Push image
docker pull user/cicd-app               # Pull image
```

### AWS Elastic Beanstalk
```bash
eb init                                 # Initialize
eb create prod-env                      # Create environment
eb deploy                               # Deploy
eb open                                 # Open app
eb logs                                 # View logs
```

---

## 🐛 Troubleshooting

### Port 5000 in use
```bash
lsof -i :5000                           # Find process
kill -9 <PID>                           # Kill process
kill -9 $(lsof -t -i:5000)             # Kill in one command
```

### Module not found
```bash
source venv/bin/activate                # Activate virtual env
pip install -r requirements.txt         # Reinstall dependencies
```

### Tests failing
```bash
pytest test_app.py -vv                  # Verbose output
pytest test_app.py::test_name -v        # Run specific test
python --version                        # Check Python version (need 3.8+)
```

### Docker build fails
```bash
docker system prune -a                  # Clear cache
docker build --no-cache -t cicd-app .   # Build without cache
```

### GitHub Actions not triggering
```bash
ls .github/workflows/ci-cd.yml          # Check file exists
# Validate YAML: http://www.yamllint.com/
# Check: GitHub repo → Settings → Actions → Enabled
```

---

## 📊 CI/CD Pipeline Stages

```
1. LINT    → Check code quality (flake8)
2. TEST    → Run unit tests (pytest) on Python 3.8, 3.9, 3.10
3. BUILD   → Build Docker image
4. DEPLOY  → Deploy to production (main branch only)
5. NOTIFY  → Send status notifications
```

---

## 💡 Pro Tips

### Test before pushing
```bash
pytest test_app.py -v && git push
```

### Git aliases
```bash
git config --global alias.cm "commit -m"
git config --global alias.st "status"
# Now use: git cm "message"
```

### Auto-reload Flask
```bash
FLASK_ENV=development python app.py
```

### Health check monitoring
```bash
# Local
curl http://localhost:5000/health

# Production (replace with your URL)
curl https://your-app.herokuapp.com/health
```

---

## 🔗 Useful Links

- **GitHub Actions**: https://docs.github.com/en/actions
- **Flask**: https://flask.palletsprojects.com/
- **Docker**: https://docs.docker.com/
- **pytest**: https://docs.pytest.org/
- **Heroku**: https://devcenter.heroku.com/

---

## 📞 Getting Help

1. Check `README.md` and `DEPLOYMENT.md`
2. Search GitHub Issues
3. Create new issue with logs
4. Stack Overflow: tag `flask`, `github-actions`, `docker`

---

**Keep this handy while learning!** 📌
