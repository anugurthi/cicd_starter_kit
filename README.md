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

## 🎯 CI/CD Pipeline Explained (Deep Dive)

Your `.github/workflows/ci-cd.yml` file defines a **5-stage automated pipeline** that runs on every push.

### 📊 Pipeline Flow

```
Git Push
   ↓
┌─────────────────────────────────────────────────────┐
│ Stage 1: LINT (Code Quality Check)                  │
│ ✓ Check Python code style with flake8              │
│ ✓ Ensure PEP 8 compliance                          │
│ ✓ Find common bugs and issues                      │
└─────────────────────────────────────────────────────┘
   ↓ (only if lint passes)
┌─────────────────────────────────────────────────────┐
│ Stage 2: TEST (Automated Testing)                   │
│ ✓ Run 13 unit tests                                │
│ ✓ Test on Python 3.8, 3.9, 3.10 (matrix)          │
│ ✓ Generate coverage report                         │
│ ✓ Upload to Codecov                                │
└─────────────────────────────────────────────────────┘
   ↓ (only if tests pass)
┌─────────────────────────────────────────────────────┐
│ Stage 3: BUILD (Docker Image)                       │
│ ✓ Build Docker image from Dockerfile               │
│ ✓ Tag with commit SHA                              │
│ ✓ Test image with health check                     │
│ ✓ Push to Docker Hub (if secrets configured)       │
└─────────────────────────────────────────────────────┘
   ↓ (only if build succeeds + on master branch)
┌─────────────────────────────────────────────────────┐
│ Stage 4: DEPLOY (Production Deployment)             │
│ ✓ Deploy to Heroku / AWS / Azure / GCP            │
│ ✓ Run database migrations                          │
│ ✓ Update production environment                    │
│ ✓ Verify deployment success                        │
└─────────────────────────────────────────────────────┘
   ↓ (always runs)
┌─────────────────────────────────────────────────────┐
│ Stage 5: NOTIFY (Status Report)                     │
│ ✓ Send Slack/email notification                    │
│ ✓ Report success or failure                        │
│ ✓ Include test results and coverage                │
└─────────────────────────────────────────────────────┘
```

---

### Stage 1: Lint (Code Quality) - ~30 seconds

**What happens:**
```yaml
lint:
  name: Code Quality Check
  runs-on: ubuntu-latest
  steps:
    - uses: actions/checkout@v3
    - uses: actions/setup-python@v4
      with:
        python-version: '3.9'
    - run: |
        pip install flake8 pylint
        flake8 app.py test_app.py --max-line-length=120
```

**What it checks:**
- ✅ Code follows PEP 8 style guide
- ✅ No syntax errors
- ✅ No unused variables or imports
- ✅ Proper indentation
- ✅ Line length < 120 characters

**Example issues caught:**
- Missing spaces around operators
- Unused imports
- Undefined variables
- Incorrect indentation

**If it fails:** The pipeline stops here. Fix the linting errors and push again.

---

### Stage 2: Test (Automated Testing) - ~1-2 minutes

**What happens:**
```yaml
test:
  name: Run Tests
  runs-on: ubuntu-latest
  strategy:
    matrix:
      python-version: [3.8, 3.9, '3.10']
  steps:
    - uses: actions/checkout@v3
    - uses: actions/setup-python@v4
      with:
        python-version: ${{ matrix.python-version }}
    - run: |
        pip install -r requirements.txt
        pytest test_app.py -v --cov=app --cov-report=xml
    - uses: codecov/codecov-action@v3
      with:
        file: ./coverage.xml
```

**What it tests:**
- ✅ All 13 unit tests pass
- ✅ Tests run on Python 3.8, 3.9, 3.10 (matrix strategy)
- ✅ Code coverage > 80%
- ✅ All endpoints work correctly
- ✅ No regressions introduced

**Tests running:**
1. `test_home_endpoint()` - Check UI loads
2. `test_api_endpoint()` - Check API docs
3. `test_health_endpoint()` - Check health status
4. `test_get_tasks()` - Get all tasks
5. `test_create_task()` - Create new task
6. `test_get_single_task()` - Get specific task
7. `test_update_task()` - Update task
8. `test_delete_task()` - Delete task
9. `test_create_task_missing_fields()` - Validation
10. `test_get_nonexistent_task()` - 404 handling
11. `test_add_function()` - Utility function
12. `test_multiply_function()` - Utility function
13. More edge cases...

**Coverage report:**
- Shows which lines were executed during tests
- Uploaded to Codecov for visualization
- Badge shows coverage % on GitHub

**If it fails:** Check test logs to see which test failed and why. Fix the code or test.

---

### Stage 3: Build (Docker Image) - ~1-2 minutes

**What happens:**
```yaml
build:
  name: Build Docker Image
  runs-on: ubuntu-latest
  needs: [lint, test]  # Only runs if lint and test pass
  steps:
    - uses: actions/checkout@v3
    
    - name: Login to Docker Hub
      uses: docker/login-action@v2
      with:
        username: ${{ secrets.DOCKER_USERNAME }}
        password: ${{ secrets.DOCKER_PASSWORD }}
    
    - name: Build and push
      uses: docker/build-push-action@v4
      with:
        context: .
        push: true
        tags: |
          ${{ secrets.DOCKER_USERNAME }}/cicd-app:latest
          ${{ secrets.DOCKER_USERNAME }}/cicd-app:${{ github.sha }}
    
    - name: Test Docker image
      run: |
        docker run -d -p 5000:5000 --name test-container \
          ${{ secrets.DOCKER_USERNAME }}/cicd-app:latest
        sleep 5
        curl http://localhost:5000/health || exit 1
        docker stop test-container
```

**What it does:**
1. ✅ **Login to Docker Hub** using secrets
2. ✅ **Build Docker image** from Dockerfile
3. ✅ **Tag image** with:
   - `latest` - Always points to most recent
   - `<commit-sha>` - Specific version (e.g., `abc123def`)
4. ✅ **Push to Docker Hub** (if secrets configured)
5. ✅ **Test image** - Start container and check health endpoint
6. ✅ **Cleanup** - Stop test container

**Docker Hub setup required:**
```bash
# Add these secrets to GitHub:
# Settings → Secrets → Actions

DOCKER_USERNAME = your-dockerhub-username
DOCKER_PASSWORD = your-dockerhub-token  # Use Access Token, not password!
```

**Create Docker Hub Access Token:**
1. Login to https://hub.docker.com
2. Account Settings → Security → New Access Token
3. Description: `GitHub Actions CI/CD`
4. Permissions: Read, Write, Delete
5. Copy token and save as `DOCKER_PASSWORD` secret

**What you get:**
- Image available at: `docker.io/YOUR_USERNAME/cicd-app:latest`
- Can pull and run anywhere: `docker pull YOUR_USERNAME/cicd-app:latest`
- Version history with commit SHAs

**If it fails:** Check Docker Hub credentials, Dockerfile syntax, or build logs.

---

### Stage 4: Deploy (Production) - ~30 seconds to 2 minutes

**What happens:**
```yaml
deploy:
  name: Deploy to Production
  runs-on: ubuntu-latest
  needs: [build]
  if: github.ref == 'refs/heads/master'  # Only deploy from master branch
  steps:
    - uses: actions/checkout@v3
    
    # Option A: Deploy to Heroku
    - name: Deploy to Heroku
      uses: akhileshns/heroku-deploy@v3.12.12
      with:
        heroku_api_key: ${{ secrets.HEROKU_API_KEY }}
        heroku_app_name: ${{ secrets.HEROKU_APP_NAME }}
        heroku_email: ${{ secrets.HEROKU_EMAIL }}
    
    # Option B: Deploy to AWS EC2
    - name: Deploy to AWS EC2
      run: |
        echo "${{ secrets.AWS_EC2_KEY }}" > key.pem
        chmod 600 key.pem
        ssh -i key.pem ${{ secrets.AWS_EC2_USER }}@${{ secrets.AWS_EC2_HOST }} \
          "docker pull ${{ secrets.DOCKER_USERNAME }}/cicd-app:latest && \
           docker stop cicd-app || true && \
           docker rm cicd-app || true && \
           docker run -d -p 80:5000 --name cicd-app --restart always \
             ${{ secrets.DOCKER_USERNAME }}/cicd-app:latest"
    
    # Option C: Deploy to Azure
    - name: Deploy to Azure
      uses: azure/webapps-deploy@v2
      with:
        app-name: ${{ secrets.AZURE_WEBAPP_NAME }}
        publish-profile: ${{ secrets.AZURE_PUBLISH_PROFILE }}
        images: ${{ secrets.DOCKER_USERNAME }}/cicd-app:latest
```

**Deployment Options:**

#### **Heroku Deployment**
Secrets needed:
```bash
HEROKU_API_KEY      # Get from: heroku auth:token
HEROKU_APP_NAME     # Your app name (e.g., my-cicd-app)
HEROKU_EMAIL        # Your Heroku email
```

Steps:
1. Builds from Dockerfile or Procfile
2. Deploys to Heroku dynos
3. Runs database migrations
4. App live at: `https://YOUR_APP_NAME.herokuapp.com`

#### **AWS EC2 Deployment**
Secrets needed:
```bash
AWS_EC2_HOST        # Public IP (e.g., 54.123.45.67)
AWS_EC2_USER        # Usually 'ubuntu' or 'ec2-user'
AWS_EC2_KEY         # Contents of your .pem file
DOCKER_USERNAME     # Your Docker Hub username
```

Steps:
1. SSH into EC2 instance
2. Pull latest Docker image from Docker Hub
3. Stop old container
4. Start new container on port 80
5. App live at: `http://YOUR_EC2_IP`

#### **Azure App Service Deployment**
Secrets needed:
```bash
AZURE_WEBAPP_NAME        # Your app name
AZURE_PUBLISH_PROFILE    # Download from Azure Portal
```

Steps:
1. Deploys Docker container to Azure App Service
2. Configures auto-scaling
3. App live at: `https://YOUR_APP_NAME.azurewebsites.net`

#### **GCP Cloud Run Deployment**
Secrets needed:
```bash
GCP_PROJECT_ID      # Your GCP project ID
GCP_SA_KEY          # Service account key JSON
```

Steps:
1. Deploys to serverless Cloud Run
2. Auto-scales based on traffic
3. App live at: `https://cicd-app-xxxxx.run.app`

**If it fails:** Check deployment logs, credentials, and server access.

---

### Stage 5: Notify (Status Report) - ~5 seconds

**What happens:**
```yaml
notify:
  name: Notify Results
  runs-on: ubuntu-latest
  needs: [lint, test, build, deploy]
  if: always()  # Run even if previous stages fail
  steps:
    - name: Send Slack notification
      uses: 8398a7/action-slack@v3
      with:
        status: ${{ job.status }}
        text: |
          Pipeline ${{ job.status }}!
          Commit: ${{ github.sha }}
          Author: ${{ github.actor }}
          Tests: ${{ needs.test.result }}
          Deployment: ${{ needs.deploy.result }}
        webhook_url: ${{ secrets.SLACK_WEBHOOK }}
    
    - name: Send Email notification
      run: |
        echo "Pipeline completed with status: ${{ job.status }}"
        # Add email sending logic here
```

**What it does:**
- ✅ **Sends Slack message** with pipeline results
- ✅ **Sends email notification** to team
- ✅ **Reports**:
  - Success or failure status
  - Which stages passed/failed
  - Test coverage percentage
  - Deployment URL
  - Commit info and author

**Setup Slack notifications:**
1. Create Slack webhook: https://api.slack.com/messaging/webhooks
2. Add webhook URL as `SLACK_WEBHOOK` secret in GitHub
3. Customize message format in workflow

**Example notification:**
```
🚀 Pipeline Success!
Commit: abc123def (feat: Add new endpoint)
Author: anugurthi
✅ Lint: Passed
✅ Tests: Passed (13/13, 85% coverage)
✅ Build: Passed (Image pushed to Docker Hub)
✅ Deploy: Passed (Live at https://my-app.herokuapp.com)
Duration: 3m 42s
```

---

## 🔐 GitHub Secrets Setup (Complete Guide)

Add these secrets for full automation:

### **1. Go to GitHub Repository Settings**
```
https://github.com/YOUR_USERNAME/cicd_starter_kit/settings/secrets/actions
```

### **2. Click "New repository secret"**

### **3. Add Required Secrets**

#### For Docker Hub:
```
DOCKER_USERNAME = your-dockerhub-username
DOCKER_PASSWORD = your-dockerhub-access-token
```

#### For Heroku:
```
HEROKU_API_KEY = output of: heroku auth:token
HEROKU_APP_NAME = your-app-name
HEROKU_EMAIL = your@email.com
```

#### For AWS EC2:
```
AWS_EC2_HOST = 54.123.45.67
AWS_EC2_USER = ubuntu
AWS_EC2_KEY = -----BEGIN RSA PRIVATE KEY-----
              (paste entire .pem file contents)
              -----END RSA PRIVATE KEY-----
```

#### For Azure:
```
AZURE_WEBAPP_NAME = your-app-name
AZURE_PUBLISH_PROFILE = (download from Azure Portal)
```

#### For GCP:
```
GCP_PROJECT_ID = your-project-id
GCP_SA_KEY = {
              "type": "service_account",
              "project_id": "your-project",
              ...
             }
```

#### For Notifications:
```
SLACK_WEBHOOK = https://hooks.slack.com/services/YOUR/WEBHOOK/URL
```

---

## ⏱️ Pipeline Timeline

| Stage | Duration | Runs On | Depends On |
|-------|----------|---------|------------|
| Lint | ~30s | Every push | Nothing |
| Test | ~1-2m | Every push | Lint passes |
| Build | ~1-2m | Every push | Lint + Test pass |
| Deploy | ~30s-2m | Master branch only | Build passes |
| Notify | ~5s | Always | All stages complete |

**Total: ~3-5 minutes** from push to production! 🚀

---

## 🎓 What You Learn

By understanding this pipeline, you now know:

✅ **CI/CD fundamentals** - Automated testing and deployment  
✅ **GitHub Actions** - Workflow syntax and secrets  
✅ **Docker** - Containerization and registries  
✅ **Cloud deployment** - Multiple platform options  
✅ **DevOps practices** - Industry-standard automation  

**This is production-ready CI/CD!** 🎉
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

### Option 1: Docker Hub (Recommended for CI/CD)

Push your Docker image to Docker Hub so it can be pulled and deployed anywhere.

#### **Step 1: Create Docker Hub Account**
1. Go to: https://hub.docker.com/signup
2. Create free account
3. Verify your email

#### **Step 2: Create Repository on Docker Hub**
1. Login to Docker Hub
2. Click "Create Repository"
3. Name it: `cicd-app`
4. Set visibility: Public (free) or Private (paid)
5. Click "Create"

#### **Step 3: Push Manually (Test First)**
```bash
# Login to Docker Hub
docker login
# Enter your Docker Hub username and password

# Build and tag your image
docker build -t YOUR_DOCKERHUB_USERNAME/cicd-app:latest .

# Example:
docker build -t anugurthi/cicd-app:latest .

# Push to Docker Hub
docker push YOUR_DOCKERHUB_USERNAME/cicd-app:latest

# Verify it's uploaded
# Visit: https://hub.docker.com/r/YOUR_DOCKERHUB_USERNAME/cicd-app
```

#### **Step 4: Automate with GitHub Actions**

**Add Docker Hub credentials to GitHub:**

1. Go to your GitHub repo: `https://github.com/YOUR_USERNAME/cicd_starter_kit`
2. Click **Settings** → **Secrets and variables** → **Actions**
3. Click **"New repository secret"**
4. Add two secrets:

   **Secret 1:**
   - Name: `DOCKER_USERNAME`
   - Value: `your-dockerhub-username`
   
   **Secret 2:**
   - Name: `DOCKER_PASSWORD`
   - Value: `your-dockerhub-password` (or use Access Token - recommended!)

**Create Docker Hub Access Token (More Secure):**
1. Go to: https://hub.docker.com/settings/security
2. Click **"New Access Token"**
3. Description: `GitHub Actions CI/CD`
4. Permissions: Read, Write, Delete
5. Click **"Generate"**
6. Copy the token
7. Use this token as `DOCKER_PASSWORD` in GitHub secrets

**Your pipeline will now automatically:**
- Build Docker image on every push
- Tag it with commit SHA
- Push to Docker Hub
- Available for deployment anywhere!

#### **Step 5: Pull and Deploy Anywhere**
```bash
# On any server (AWS, Azure, GCP, DigitalOcean, etc.)
docker pull YOUR_DOCKERHUB_USERNAME/cicd-app:latest
docker run -d -p 80:5000 YOUR_DOCKERHUB_USERNAME/cicd-app:latest

# Your app is now live on: http://your-server-ip
```

---

### Option 2: Heroku (Easiest Platform Deployment)

Deploy directly to Heroku's cloud platform (free tier available).

#### **Step 1: Install Heroku CLI**
```bash
# macOS
brew tap heroku/brew && brew install heroku

# Or download from:
# https://devcenter.heroku.com/articles/heroku-cli
```

#### **Step 2: Login and Create App**
```bash
# Login
heroku login

# Create app (name must be unique globally)
heroku create your-unique-app-name

# Example:
heroku create my-cicd-task-manager
```

#### **Step 3: Deploy Manually**
```bash
# Add Heroku remote
heroku git:remote -a your-app-name

# Push to Heroku
git push heroku master

# Open your app
heroku open

# Your app is live at: https://your-app-name.herokuapp.com
```

#### **Step 4: Automate with GitHub Actions**

**Add Heroku credentials to GitHub:**

1. Get your Heroku API key:
   ```bash
   heroku auth:token
   ```
   Copy the token that appears

2. Go to GitHub repo: Settings → Secrets → Actions
3. Add two secrets:

   **Secret 1:**
   - Name: `HEROKU_API_KEY`
   - Value: `your-heroku-api-token`
   
   **Secret 2:**
   - Name: `HEROKU_APP_NAME`
   - Value: `your-app-name` (e.g., `my-cicd-task-manager`)

**Your pipeline will now automatically deploy to Heroku on every push to master!**

**See `DEPLOYMENT.md` for complete Heroku guide with troubleshooting!**

---

### Option 3: AWS (EC2, ECS, or Elastic Beanstalk)

Deploy to Amazon Web Services for production-grade hosting.

#### **AWS EC2 (Virtual Server)**

**Step 1: Launch EC2 Instance**
1. Go to: https://console.aws.amazon.com/ec2
2. Click "Launch Instance"
3. Choose: Ubuntu Server 22.04 LTS
4. Instance type: t2.micro (free tier)
5. Create/select key pair (download .pem file)
6. Configure security group:
   - Allow SSH (port 22) from your IP
   - Allow HTTP (port 80) from anywhere
   - Allow Custom TCP (port 5000) from anywhere
7. Launch instance

**Step 2: Connect and Setup**
```bash
# SSH into your server
ssh -i your-key.pem ubuntu@your-ec2-public-ip

# Install Docker
sudo apt update
sudo apt install docker.io -y
sudo systemctl start docker
sudo systemctl enable docker
sudo usermod -aG docker ubuntu

# Logout and login again for docker permissions
exit
ssh -i your-key.pem ubuntu@your-ec2-public-ip
```

**Step 3: Deploy Your App**
```bash
# Pull your Docker image
docker pull YOUR_DOCKERHUB_USERNAME/cicd-app:latest

# Run it
docker run -d -p 80:5000 --restart always \
  --name cicd-app \
  YOUR_DOCKERHUB_USERNAME/cicd-app:latest

# Your app is live at: http://your-ec2-public-ip
```

**Step 4: Automate with GitHub Actions**

Add to GitHub Secrets:
- `AWS_EC2_HOST` = Your EC2 public IP
- `AWS_EC2_KEY` = Contents of your .pem file
- `AWS_EC2_USER` = `ubuntu`

**See `DEPLOYMENT.md` for AWS ECS, Elastic Beanstalk, and Lambda options!**

---

### Option 4: Azure (App Service or Container Instances)

#### **Azure App Service**

**Step 1: Install Azure CLI**
```bash
# macOS
brew install azure-cli

# Or download from:
# https://docs.microsoft.com/cli/azure/install-azure-cli
```

**Step 2: Login and Deploy**
```bash
# Login
az login

# Create resource group
az group create --name cicd-rg --location eastus

# Create App Service plan
az appservice plan create \
  --name cicd-plan \
  --resource-group cicd-rg \
  --is-linux \
  --sku B1

# Create web app with Docker
az webapp create \
  --resource-group cicd-rg \
  --plan cicd-plan \
  --name your-unique-app-name \
  --deployment-container-image-name YOUR_DOCKERHUB_USERNAME/cicd-app:latest

# Your app is live at: https://your-app-name.azurewebsites.net
```

**Step 3: Automate with GitHub Actions**

Add to GitHub Secrets:
- `AZURE_CREDENTIALS` = Service principal JSON
- `AZURE_WEBAPP_NAME` = Your app name

---

### Option 5: Google Cloud Platform (Cloud Run)

#### **GCP Cloud Run (Serverless)**

**Step 1: Install gcloud CLI**
```bash
# macOS
brew install google-cloud-sdk

# Or download from:
# https://cloud.google.com/sdk/docs/install
```

**Step 2: Deploy**
```bash
# Login
gcloud auth login

# Set project
gcloud config set project YOUR_PROJECT_ID

# Deploy to Cloud Run
gcloud run deploy cicd-app \
  --image YOUR_DOCKERHUB_USERNAME/cicd-app:latest \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated

# Your app is live at the URL shown
```

**Step 3: Automate with GitHub Actions**

Add to GitHub Secrets:
- `GCP_PROJECT_ID` = Your GCP project ID
- `GCP_SA_KEY` = Service account key JSON

---

### Option 6: DigitalOcean (Droplet or App Platform)

#### **DigitalOcean App Platform (Easiest)**

**Step 1: Create Account**
1. Go to: https://www.digitalocean.com
2. Sign up (free $200 credit for 60 days)

**Step 2: Deploy from GitHub**
1. Click "Create" → "Apps"
2. Connect your GitHub account
3. Select repository: `cicd_starter_kit`
4. DigitalOcean auto-detects Dockerfile
5. Click "Next" → "Launch App"
6. Your app is deployed automatically!

**Auto-deploys on every push to GitHub!**

---

## 🔧 Deployment Comparison

| Platform | Difficulty | Free Tier | Auto-Deploy | Best For |
|----------|-----------|-----------|-------------|----------|
| **Docker Hub** | Easy | ✅ Yes | ✅ CI/CD | Image storage |
| **Heroku** | Easiest | ✅ Yes | ✅ Yes | Quick demos |
| **AWS EC2** | Medium | ✅ Yes | ⚙️ Setup needed | Production |
| **Azure** | Medium | ✅ Yes | ⚙️ Setup needed | Enterprise |
| **GCP Cloud Run** | Easy | ✅ Yes | ⚙️ Setup needed | Serverless |
| **DigitalOcean** | Easy | ✅ $200 credit | ✅ Yes | Startups |

---

## 🎯 Recommended Path for Beginners

1. **Start with Docker Hub** → Learn container registry
2. **Deploy to Heroku** → See it live quickly
3. **Try AWS EC2** → Learn servers
4. **Explore others** → Find what fits your needs

**See `DEPLOYMENT.md` for detailed guides with screenshots for each platform!**

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

## � Quick Reference Summary

### Your Complete CI/CD Stack:

```
┌─────────────────────────────────────────────────────┐
│                   YOUR TECH STACK                    │
├─────────────────────────────────────────────────────┤
│ Language:       Python 3.9                          │
│ Framework:      Flask (REST API)                    │
│ Testing:        pytest, unittest                    │
│ Coverage:       pytest-cov                          │
│ Linting:        flake8                              │
│ Containerization: Docker                            │
│ CI/CD:          GitHub Actions                      │
│ Registry:       Docker Hub                          │
│ Deployment:     Heroku/AWS/Azure/GCP               │
└─────────────────────────────────────────────────────┘
```

### Essential Commands Cheat Sheet:

```bash
# 🚀 QUICK START
./setup.sh                    # One-command setup
python3 app.py                # Run app locally
open http://localhost:5000    # View in browser

# 🧪 TESTING
python3 -m pytest test_app.py -v              # Run tests
python3 -m pytest --cov=app                   # Check coverage
python3 -m pytest -k test_health              # Run specific test

# 🐳 DOCKER
docker build -t cicd-app .                    # Build image
docker run -d -p 5000:5000 cicd-app          # Run container
docker ps                                     # List containers
docker logs <container-id>                    # View logs
docker stop <container-id>                    # Stop container
docker exec -it <container-id> /bin/bash     # Shell into container

# 🔄 GIT & CI/CD
git add .                                     # Stage changes
git commit -m "message"                       # Commit
git push                                      # Push (triggers CI/CD!)
git log --oneline -5                          # View recent commits

# 🚀 DOCKER HUB
docker login                                  # Login to Docker Hub
docker tag cicd-app user/cicd-app:latest     # Tag image
docker push user/cicd-app:latest             # Push to registry
docker pull user/cicd-app:latest             # Pull from registry

# 🌐 DEPLOYMENT
heroku login                                  # Login to Heroku
heroku create app-name                        # Create app
git push heroku master                        # Deploy
heroku logs --tail                            # View logs
heroku open                                   # Open app

# 🔍 DEBUGGING
curl http://localhost:5000/health            # Test endpoint
docker inspect <container-id>                # Inspect container
lsof -i :5000                                # Check port usage
kill -9 $(lsof -t -i:5000)                  # Kill process on port
```

### GitHub Secrets You Need:

```bash
# For Docker Hub deployment:
DOCKER_USERNAME = your-dockerhub-username
DOCKER_PASSWORD = your-dockerhub-access-token

# For Heroku deployment:
HEROKU_API_KEY = $(heroku auth:token)
HEROKU_APP_NAME = your-app-name
HEROKU_EMAIL = your@email.com

# For AWS EC2 deployment:
AWS_EC2_HOST = 54.123.45.67
AWS_EC2_USER = ubuntu
AWS_EC2_KEY = (contents of .pem file)

# For notifications:
SLACK_WEBHOOK = https://hooks.slack.com/...
```

Add at: `https://github.com/YOUR_USERNAME/cicd_starter_kit/settings/secrets/actions`

---

## 🎯 Learning Checklist

### Beginner Level (2 Hours) ✅
- [ ] Understand what CI/CD is
- [ ] Run the app locally
- [ ] Run all tests successfully
- [ ] Build Docker image
- [ ] Push code to GitHub
- [ ] Watch pipeline run
- [ ] See all 5 stages complete

### Intermediate Level (1 Week)
- [ ] Add Docker Hub credentials
- [ ] Push Docker image automatically
- [ ] Deploy to Heroku
- [ ] Add a new API endpoint with tests
- [ ] Make tests fail intentionally and fix
- [ ] Set up Slack notifications
- [ ] Add code coverage badge to README

### Advanced Level (1 Month)
- [ ] Deploy to AWS EC2
- [ ] Set up staging environment
- [ ] Add integration tests
- [ ] Implement blue-green deployment
- [ ] Add database (PostgreSQL)
- [ ] Add user authentication
- [ ] Set up monitoring (Prometheus/Grafana)
- [ ] Add load testing

---

## 📚 File Guide

### Files You'll Edit Often:
- `app.py` - Add new endpoints and features
- `test_app.py` - Add tests for new features
- `requirements.txt` - Add Python dependencies
- `README.md` - Update documentation

### Files You'll Rarely Touch:
- `Dockerfile` - Only if changing deployment
- `setup.sh` - Only if changing setup process
- `.github/workflows/ci-cd.yml` - Only if customizing pipeline
- `docker-compose.yml` - Only for multi-container apps

### Files for Reference:
- `CHEATSHEET.md` - Command reference
- `DEPLOYMENT.md` - Deployment guides

---

## 🐛 Common Issues & Solutions

### Issue: "Module not found"
```bash
# Solution:
./setup.sh                    # Run setup again
source venv/bin/activate      # Activate virtual environment
python3 -m pip install -r requirements.txt
```

### Issue: Pipeline not triggering
```bash
# Check branch name matches workflow config
git branch                    # Should be 'master' or 'main'

# Check .github/workflows/ci-cd.yml has your branch
cat .github/workflows/ci-cd.yml | grep "branches:"

# Push again
git push
```

### Issue: Docker build fails in pipeline
```bash
# Test locally first:
docker build -t cicd-app .

# Check Dockerfile syntax
# Make sure all files are copied (app.py, templates/, etc.)
```

### Issue: Deployment fails
```bash
# Check secrets are set correctly:
# GitHub → Settings → Secrets → Actions

# Verify credentials work locally:
docker login                  # Test Docker Hub
heroku login                  # Test Heroku
```

### Issue: Port already in use
```bash
# Find and kill process:
lsof -i :5000
kill -9 <PID>

# Or use different port:
# Edit app.py: app.run(port=8000)
```

---

## 🎓 What Makes This Project Special

### ✅ Production-Ready Features:
1. **Automated Testing** - 13 comprehensive tests
2. **Code Quality** - Linting with flake8
3. **Containerization** - Docker with multi-stage builds
4. **CI/CD Pipeline** - 5-stage automation
5. **Multiple Deployment Options** - 6 platforms supported
6. **Health Checks** - Endpoint monitoring
7. **Coverage Reporting** - Track test coverage
8. **Matrix Testing** - Test on 3 Python versions
9. **Beautiful UI** - Modern task manager interface
10. **Complete Documentation** - 1000+ lines of guides

### ✅ Industry Standards:
- RESTful API design
- Test-Driven Development (TDD)
- Continuous Integration (CI)
- Continuous Deployment (CD)
- Infrastructure as Code (IaC)
- Container orchestration ready
- Cloud-native architecture
- DevOps best practices

### ✅ Resume-Worthy Skills:
- Python backend development
- API design and testing
- Docker containerization
- GitHub Actions CI/CD
- Cloud platform deployment
- DevOps automation
- System monitoring
- Production troubleshooting

---

## �💡 Tips for Success

1. **Take your time** - Don't rush through exercises
2. **Experiment** - Break things, fix them, learn!
3. **Read logs** - Pipeline errors tell you exactly what's wrong
4. **Ask questions** - Search GitHub/Stack Overflow
5. **Build something real** - Modify this to solve your own problem
6. **Document your learning** - Keep notes of what you learned
7. **Share your work** - Post on LinkedIn, Twitter
8. **Add to resume** - This is production experience!

---

## 🌟 Next Steps After Completion

### This Week:
1. Push to GitHub and watch pipeline run ✅
2. Complete all 3 hands-on exercises ✅
3. Deploy to Heroku or Docker Hub ✅
4. Add one new feature with tests ✅
5. Share your success on social media ✅

### This Month:
1. Add database (PostgreSQL/MongoDB)
2. Add user authentication (JWT)
3. Deploy to AWS/Azure/GCP
4. Set up staging environment
5. Add monitoring and alerts
6. Contribute to open source

### This Year:
1. Build 3 more projects with CI/CD
2. Learn Kubernetes
3. Get DevOps certification
4. Mentor others in CI/CD
5. Land a DevOps/SRE role

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
