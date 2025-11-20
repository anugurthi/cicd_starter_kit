# 🚀 Deployment Guide

Complete guide for deploying your CI/CD Starter Kit to various platforms.

---

## Table of Contents
1. [Heroku Deployment](#1-heroku-deployment-easiest)
2. [Docker Deployment](#2-docker-deployment)
3. [AWS Deployment](#3-aws-deployment)
4. [Azure Deployment](#4-azure-deployment)
5. [Google Cloud Deployment](#5-google-cloud-deployment)
6. [Environment Variables](#environment-variables)
7. [Security Best Practices](#security-best-practices)

---

## 1. Heroku Deployment (Easiest)

### Prerequisites
- Heroku account (free tier available)
- Heroku CLI installed

### Quick Deploy

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

### Automated Deployment with GitHub Actions

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

### Useful Heroku Commands

```bash
heroku ps:scale web=1                  # Scale dynos
heroku run python                      # Run commands
heroku addons:create heroku-postgresql:hobby-dev  # Add database
heroku domains:add www.yourdomain.com  # Custom domain
```

### Troubleshooting Heroku

**Application Error:**
```bash
heroku logs --tail  # Check logs
# Ensure Procfile exists and port is correctly set
```

**Build Failed:**
```bash
cat runtime.txt  # Should be: python-3.9.x
heroku run pip list  # Verify requirements.txt
```

---

## 2. Docker Deployment

### Local Docker Setup

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

### Using Docker Compose

```bash
docker-compose up -d        # Start all services
docker-compose logs -f      # View logs
docker-compose down         # Stop services
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

#### Prerequisites
- AWS Account
- AWS CLI configured
- Docker image pushed to ECR or Docker Hub

#### 1. Create ECR Repository
```bash
aws ecr create-repository \
  --repository-name cicd-starter-app \
  --region us-east-1
```

#### 2. Push Image to ECR
```bash
# Login to ECR
aws ecr get-login-password --region us-east-1 | \
  docker login --username AWS --password-stdin \
  YOUR_ACCOUNT.dkr.ecr.us-east-1.amazonaws.com

# Tag and push
docker tag cicd-starter-app:latest \
  YOUR_ACCOUNT.dkr.ecr.us-east-1.amazonaws.com/cicd-starter-app:latest
docker push YOUR_ACCOUNT.dkr.ecr.us-east-1.amazonaws.com/cicd-starter-app:latest
```

#### 3. Create ECS Cluster
```bash
aws ecs create-cluster \
  --cluster-name cicd-cluster \
  --region us-east-1
```

#### 4. Create Task Definition

Create `ecs-task-definition.json`:

```json
{
  "family": "cicd-task",
  "networkMode": "awsvpc",
  "requiresCompatibilities": ["FARGATE"],
  "cpu": "256",
  "memory": "512",
  "executionRoleArn": "arn:aws:iam::YOUR_ACCOUNT_ID:role/ecsTaskExecutionRole",
  "containerDefinitions": [
    {
      "name": "cicd-app",
      "image": "YOUR_ACCOUNT_ID.dkr.ecr.us-east-1.amazonaws.com/cicd-starter-app:latest",
      "portMappings": [
        {
          "containerPort": 5000,
          "protocol": "tcp"
        }
      ],
      "essential": true,
      "logConfiguration": {
        "logDriver": "awslogs",
        "options": {
          "awslogs-group": "/ecs/cicd-task",
          "awslogs-region": "us-east-1",
          "awslogs-stream-prefix": "ecs"
        }
      },
      "healthCheck": {
        "command": ["CMD-SHELL", "curl -f http://localhost:5000/health || exit 1"],
        "interval": 30,
        "timeout": 5,
        "retries": 3,
        "startPeriod": 60
      }
    }
  ]
}
```

Register task definition:
```bash
aws ecs register-task-definition \
  --cli-input-json file://ecs-task-definition.json
```

#### 5. Create ECS Service
```bash
aws ecs create-service \
  --cluster cicd-cluster \
  --service-name cicd-service \
  --task-definition cicd-task \
  --desired-count 2 \
  --launch-type FARGATE \
  --network-configuration "awsvpcConfiguration={subnets=[subnet-xxx,subnet-yyy],securityGroups=[sg-xxx],assignPublicIp=ENABLED}" \
  --region us-east-1
```

#### Required AWS Resources

**VPC & Networking:**
- VPC with CIDR block (e.g., 10.0.0.0/16)
- 2+ Public subnets in different AZs
- Internet Gateway attached to VPC
- Route tables configured

**Security Groups:**
- Allow inbound HTTP (80) from 0.0.0.0/0
- Allow inbound on port 5000 for ECS tasks
- Allow outbound to 0.0.0.0/0

**IAM Role for ECS Task Execution:**
- Attach `AmazonECSTaskExecutionRolePolicy`
- Attach `CloudWatchLogsFullAccess`

**CloudWatch Log Group:**
```bash
aws logs create-log-group \
  --log-group-name /ecs/cicd-task \
  --region us-east-1
```

### Option C: AWS EC2

#### 1. Launch EC2 Instance
1. Go to: https://console.aws.amazon.com/ec2
2. Click "Launch Instance"
3. Choose: Ubuntu Server 22.04 LTS
4. Instance type: t2.micro (free tier)
5. Create/select key pair (download .pem file)
6. Configure security group:
   - Allow SSH (port 22) from your IP
   - Allow HTTP (port 80) from anywhere
7. Launch instance

#### 2. Connect and Setup
```bash
# SSH into your server
ssh -i your-key.pem ubuntu@your-ec2-public-ip

# Install Docker
sudo apt update
sudo apt install docker.io -y
sudo systemctl start docker
sudo systemctl enable docker
sudo usermod -aG docker ubuntu

# Logout and login again
exit
ssh -i your-key.pem ubuntu@your-ec2-public-ip
```

#### 3. Deploy Your App
```bash
# Pull your Docker image
docker pull YOUR_DOCKERHUB_USERNAME/cicd-app:latest

# Run it
docker run -d -p 80:5000 --restart always \
  --name cicd-app \
  YOUR_DOCKERHUB_USERNAME/cicd-app:latest

# Your app is live at: http://your-ec2-public-ip
```

#### 4. Automate with GitHub Actions

Add to GitHub Secrets:
- `AWS_EC2_HOST` = Your EC2 public IP
- `AWS_EC2_KEY` = Contents of your .pem file
- `AWS_EC2_USER` = `ubuntu`

---

## 4. Azure Deployment

### Option A: Azure App Service

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

### 5. SSL/HTTPS

**Free SSL with Let's Encrypt (on VPS):**
```bash
sudo apt-get install certbot python3-certbot-nginx
sudo certbot --nginx -d yourdomain.com

# Auto-renewal (cron job)
sudo crontab -e
# Add: 0 12 * * * /usr/bin/certbot renew --quiet
```

**On Heroku:**
```bash
heroku certs:auto:enable  # Automated SSL on paid dynos
```

---

## Performance Optimization

### Gunicorn Configuration

Create `gunicorn.conf.py`:
```python
import multiprocessing

workers = multiprocessing.cpu_count() * 2 + 1
worker_class = "sync"
worker_connections = 1000
timeout = 30
keepalive = 2
```

Run with:
```bash
gunicorn -c gunicorn.conf.py app:app
```

### Caching with Redis

Add to `requirements.txt`:
```
redis==4.5.1
flask-caching==2.0.2
```

Update `app.py`:
```python
from flask_caching import Cache

cache = Cache(app, config={'CACHE_TYPE': 'redis', 'CACHE_REDIS_URL': 'redis://localhost:6379'})

@app.route('/data')
@cache.cached(timeout=300)
def get_data():
    return expensive_operation()
```

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
- [ ] Rollback plan documented

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

## Troubleshooting Deployments

### App crashes on startup
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

### Slow response times
```bash
# Scale up workers
heroku ps:scale web=2

# Use gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app

# Add caching
# Add database connection pooling
```

### Out of memory
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
