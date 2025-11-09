# 🚀 Deployment Guide

Complete guide for deploying your CI/CD Starter Kit to various platforms.

---

## Table of Contents
1. [Heroku Deployment](#heroku-deployment)
2. [Docker Deployment](#docker-deployment)
3. [AWS Deployment](#aws-deployment)
4. [Azure Deployment](#azure-deployment)
5. [Google Cloud Deployment](#google-cloud-deployment)

---

## 1. Heroku Deployment (Easiest)

### Prerequisites
- Heroku account (free tier available)
- Heroku CLI installed

### Steps

**Option A: Using Heroku CLI**

```bash
# Login to Heroku
heroku login

# Create new app
heroku create your-app-name

# Deploy
git push heroku main

# Open your app
heroku open

# View logs
heroku logs --tail
```

**Option B: Using GitHub Actions (Automated)**

1. Get your Heroku API key:
```bash
heroku auth:token
```

2. Add secrets to GitHub:
   - Go to: Settings → Secrets and variables → Actions
   - Add: `HEROKU_API_KEY` = your token
   - Add: `HEROKU_APP_NAME` = your app name
   - Add: `HEROKU_EMAIL` = your email

3. Uncomment Heroku section in `.github/workflows/ci-cd.yml`

4. Push to GitHub - auto-deployment activated! 🎉

### Heroku Commands

```bash
# Scale dynos
heroku ps:scale web=1

# Run commands
heroku run python

# Database (if added)
heroku addons:create heroku-postgresql:hobby-dev

# Custom domain
heroku domains:add www.yourdomain.com
```

### Troubleshooting Heroku

**Issue: Application Error**
```bash
heroku logs --tail
# Check if port is correctly set
# Ensure Procfile exists
```

**Issue: Build Failed**
```bash
# Check Python version
cat runtime.txt  # Should be: python-3.9.x

# Verify requirements.txt
heroku run pip list
```

---

## 2. Docker Deployment

### Local Docker Setup

**Build and run:**
```bash
# Build image
docker build -t cicd-starter-app .

# Run container
docker run -d -p 5000:5000 --name my-app cicd-starter-app

# Test
curl http://localhost:5000/health

# View logs
docker logs my-app

# Stop and remove
docker stop my-app
docker rm my-app
```

**Using Docker Compose:**
```bash
# Start all services
docker-compose up -d

# View logs
docker-compose logs -f

# Stop services
docker-compose down
```

### Deploy to Docker Hub

```bash
# Login
docker login

# Tag image
docker tag cicd-starter-app:latest yourusername/cicd-starter-app:latest

# Push to Docker Hub
docker push yourusername/cicd-starter-app:latest

# Pull and run on any server
docker pull yourusername/cicd-starter-app:latest
docker run -d -p 80:5000 yourusername/cicd-starter-app:latest
```

### Docker on VPS (DigitalOcean, Linode, etc.)

```bash
# SSH into server
ssh root@your-server-ip

# Install Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sh get-docker.sh

# Pull and run your app
docker pull yourusername/cicd-starter-app
docker run -d -p 80:5000 --restart=always yourusername/cicd-starter-app

# Your app is now live at http://your-server-ip
```

---

## 3. AWS Deployment

### Option A: AWS Elastic Beanstalk

**Setup:**
```bash
# Install EB CLI
pip install awsebcli

# Initialize application
eb init -p python-3.9 cicd-starter-app --region us-east-1

# Create environment
eb create production-env

# Deploy
eb deploy

# Open application
eb open

# Check status
eb status

# View logs
eb logs
```

**Configuration file** (`.ebextensions/python.config`):
```yaml
option_settings:
  aws:elasticbeanstalk:container:python:
    WSGIPath: app:app
  aws:elasticbeanstalk:application:environment:
    FLASK_ENV: production
```

### Option B: AWS ECS (Docker)

**Steps:**
1. Push image to ECR (Elastic Container Registry)
```bash
# Login to ECR
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin YOUR_ACCOUNT.dkr.ecr.us-east-1.amazonaws.com

# Create repository
aws ecr create-repository --repository-name cicd-starter-app

# Tag and push
docker tag cicd-starter-app:latest YOUR_ACCOUNT.dkr.ecr.us-east-1.amazonaws.com/cicd-starter-app:latest
docker push YOUR_ACCOUNT.dkr.ecr.us-east-1.amazonaws.com/cicd-starter-app:latest
```

2. Create ECS cluster and service via AWS Console

### Option C: AWS Lambda (Serverless)

**Using Zappa:**
```bash
# Install Zappa
pip install zappa

# Initialize
zappa init

# Deploy
zappa deploy production

# Update
zappa update production

# Undeploy
zappa undeploy production
```

---

## 4. Azure Deployment

### Option A: Azure App Service

**Using Azure CLI:**
```bash
# Login
az login

# Create resource group
az group create --name cicd-rg --location eastus

# Create app service plan
az appservice plan create \
  --name cicd-plan \
  --resource-group cicd-rg \
  --sku FREE \
  --is-linux

# Create web app
az webapp create \
  --resource-group cicd-rg \
  --plan cicd-plan \
  --name your-unique-app-name \
  --runtime "PYTHON:3.9"

# Deploy code
az webapp up \
  --resource-group cicd-rg \
  --name your-unique-app-name

# Configure startup
az webapp config set \
  --resource-group cicd-rg \
  --name your-unique-app-name \
  --startup-file "gunicorn --bind=0.0.0.0 --timeout 600 app:app"

# Open app
az webapp browse --resource-group cicd-rg --name your-unique-app-name
```

### Option B: Azure Container Instances

```bash
# Create container instance
az container create \
  --resource-group cicd-rg \
  --name cicd-container \
  --image yourusername/cicd-starter-app \
  --dns-name-label cicd-unique-name \
  --ports 5000

# Get URL
az container show \
  --resource-group cicd-rg \
  --name cicd-container \
  --query ipAddress.fqdn
```

### GitHub Actions for Azure

Add to secrets:
- `AZURE_CREDENTIALS` - Get from: `az ad sp create-for-rbac --name "myApp" --role contributor --scopes /subscriptions/{subscription-id}/resourceGroups/{resource-group} --sdk-auth`

---

## 5. Google Cloud Deployment

### Option A: Google Cloud Run (Easiest)

```bash
# Install gcloud CLI
# Download from: https://cloud.google.com/sdk/docs/install

# Login
gcloud auth login

# Set project
gcloud config set project YOUR_PROJECT_ID

# Build and deploy
gcloud run deploy cicd-starter-app \
  --source . \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated

# Your app is live! URL will be shown in output
```

### Option B: Google Kubernetes Engine (GKE)

```bash
# Create cluster
gcloud container clusters create cicd-cluster \
  --num-nodes=2 \
  --zone=us-central1-a

# Get credentials
gcloud container clusters get-credentials cicd-cluster --zone=us-central1-a

# Deploy
kubectl create deployment cicd-app --image=yourusername/cicd-starter-app
kubectl expose deployment cicd-app --type=LoadBalancer --port=80 --target-port=5000

# Get external IP
kubectl get service cicd-app
```

---

## Environment Variables

### Setting Environment Variables

**Heroku:**
```bash
heroku config:set KEY=value
```

**AWS Elastic Beanstalk:**
```bash
eb setenv KEY=value
```

**Azure:**
```bash
az webapp config appsettings set --resource-group rg --name app-name --settings KEY=value
```

**Docker:**
```bash
docker run -e KEY=value your-image
```

**Docker Compose:**
```yaml
environment:
  - KEY=value
```

---

## SSL/HTTPS Configuration

### Free SSL with Let's Encrypt

**On VPS with Docker:**
```bash
# Install Certbot
sudo apt-get update
sudo apt-get install certbot python3-certbot-nginx

# Get certificate
sudo certbot --nginx -d yourdomain.com

# Auto-renewal (cron job)
sudo crontab -e
# Add: 0 12 * * * /usr/bin/certbot renew --quiet
```

**On Heroku:**
```bash
# Automated SSL on paid dynos
heroku certs:auto:enable
```

---

## Performance Optimization

### Production Settings

**Gunicorn configuration** (`gunicorn.conf.py`):
```python
import multiprocessing

workers = multiprocessing.cpu_count() * 2 + 1
worker_class = "sync"
worker_connections = 1000
timeout = 30
keepalive = 2
```

**Run with:**
```bash
gunicorn -c gunicorn.conf.py app:app
```

### Caching with Redis

**Add to requirements.txt:**
```
redis==4.5.1
flask-caching==2.0.2
```

**Update app.py:**
```python
from flask_caching import Cache

cache = Cache(app, config={'CACHE_TYPE': 'redis', 'CACHE_REDIS_URL': 'redis://localhost:6379'})

@app.route('/data')
@cache.cached(timeout=300)
def get_data():
    return expensive_operation()
```

---

## Monitoring & Logging

### Application Monitoring

**Sentry (Error Tracking):**
```bash
pip install sentry-sdk[flask]
```

```python
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration

sentry_sdk.init(
    dsn="your-sentry-dsn",
    integrations=[FlaskIntegration()]
)
```

**New Relic:**
```bash
pip install newrelic
newrelic-admin run-program gunicorn app:app
```

### Log Aggregation

**Papertrail:**
```bash
# On Heroku
heroku addons:create papertrail

# View logs
heroku addons:open papertrail
```

**ELK Stack (Self-hosted):**
- Elasticsearch
- Logstash
- Kibana

---

## Cost Comparison

| Platform | Free Tier | Paid Plans |
|----------|-----------|------------|
| Heroku | 550 dyno hours/month | From $7/month |
| AWS EB | 750 hours/month (12 months) | From $15/month |
| Azure | 60 minutes/day | From $13/month |
| Google Cloud Run | 2M requests/month | Pay per use |
| DigitalOcean | No free tier | From $5/month |

---

## Deployment Checklist

Before going to production:

- [ ] Environment variables set securely
- [ ] Debug mode disabled (`FLASK_ENV=production`)
- [ ] HTTPS enabled
- [ ] Database backups configured
- [ ] Monitoring setup (Sentry, New Relic)
- [ ] Log aggregation configured
- [ ] Error pages customized (404, 500)
- [ ] Rate limiting implemented
- [ ] CORS configured properly
- [ ] Security headers added
- [ ] Database migrations tested
- [ ] Rollback plan documented

---

## Security Best Practices

### 1. Use Environment Variables
```python
import os
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
```

### 2. Rate Limiting
```bash
pip install Flask-Limiter
```

```python
from flask_limiter import Limiter

limiter = Limiter(app, default_limits=["200 per day", "50 per hour"])
```

### 3. Security Headers
```bash
pip install flask-talisman
```

```python
from flask_talisman import Talisman
Talisman(app)
```

### 4. CORS
```bash
pip install flask-cors
```

```python
from flask_cors import CORS
CORS(app, origins=["https://yourdomain.com"])
```

---

## Troubleshooting Deployments

### Common Issues

**Issue: App crashes on startup**
```bash
# Check logs
# Heroku: heroku logs --tail
# Docker: docker logs container-name
# AWS: eb logs

# Common causes:
# - Missing dependencies in requirements.txt
# - Wrong Python version
# - Port binding issues
```

**Issue: Slow response times**
```bash
# Scale up workers
heroku ps:scale web=2

# Use gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app

# Add caching
# Add database connection pooling
```

**Issue: Out of memory**
```bash
# Monitor memory usage
heroku ps
docker stats

# Optimize:
# - Reduce worker count
# - Increase dyno/container size
# - Add caching
```

---

## Next Steps

1. **Set up staging environment**
2. **Implement database (PostgreSQL/MongoDB)**
3. **Add authentication (JWT/OAuth)**
4. **Implement CI/CD for multiple environments**
5. **Set up infrastructure as code (Terraform)**

---

**Happy Deploying! 🚀**

For questions or issues, open an issue on GitHub.
