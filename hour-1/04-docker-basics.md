# Step 4: Docker Basics

**Time:** 15 minutes  
**Goal:** Package the Flask app in a Docker container

---

## What You'll Do

1. Understand what Docker is
2. Build a Docker image
3. Run the app in a container
4. Understand why Docker matters for CI/CD

---

## What is Docker?

**The Problem:**
- "It works on my machine!" 🤷
- Different Python versions on different machines
- Missing dependencies
- Environment inconsistencies

**The Solution: Docker**
- 📦 Packages app + dependencies together
- 🔒 Same environment everywhere
- 🚀 Easy to deploy anywhere

**Think of it as:** A shipping container for your code!

---

## Tasks

### 1. Understand the Dockerfile (3 min)

Open `Dockerfile` in your editor.

**Let's break it down:**

```dockerfile
FROM python:3.9-slim
```
**Meaning:** Start with a lightweight Python 3.9 image

```dockerfile
WORKDIR /app
```
**Meaning:** Set working directory to `/app`

```dockerfile
COPY requirements.txt .
RUN pip install -r requirements.txt
```
**Meaning:** Install Python dependencies

```dockerfile
COPY app/ .
```
**Meaning:** Copy our application code

```dockerfile
EXPOSE 5000
```
**Meaning:** Tell Docker the app uses port 5000

```dockerfile
CMD ["python", "app.py"]
```
**Meaning:** Command to run when container starts

---

### 2. Build a Docker Image (4 min)

**Make sure Docker is running**, then:

```bash
docker build -t cicd-app .
```

**What's happening:**
- `-t cicd-app` = Tag the image as "cicd-app"
- `.` = Use current directory for build context

**You should see:**
```
[+] Building 15.2s
 => [1/5] FROM python:3.9-slim
 => [2/5] WORKDIR /app
 => [3/5] COPY requirements.txt .
 => [4/5] RUN pip install -r requirements.txt
 => [5/5] COPY app/ .
 => exporting to image
```

✅ **Image built successfully!**

**Verify it:**
```bash
docker images
```

You should see `cicd-app` in the list.

---

### 3. Run the Container (4 min)

Start a container from your image:

```bash
docker run -d -p 5000:5000 --name my-app cicd-app
```

**What's happening:**
- `-d` = Run in background (detached)
- `-p 5000:5000` = Map port 5000 (host) to 5000 (container)
- `--name my-app` = Name the container "my-app"
- `cicd-app` = Use the image we just built

**Check if it's running:**
```bash
docker ps
```

You should see your container listed!

---

### 4. Test the Containerized App (2 min)

```bash
# Test health endpoint
curl http://localhost:5000/health

# Test in browser
# Open: http://localhost:5000
```

✅ **It works!** The app is running in a container!

---

### 5. View Container Logs (1 min)

```bash
docker logs my-app
```

You should see the Flask startup messages!

---

### 6. Stop and Clean Up (1 min)

```bash
# Stop the container
docker stop my-app

# Remove the container
docker rm my-app
```

---

## Docker vs. Regular Python

### Running Normally:
```bash
python3 app.py
```
- ❌ Requires Python installed
- ❌ Requires correct Python version
- ❌ Requires dependencies installed
- ❌ Different on every machine

### Running in Docker:
```bash
docker run cicd-app
```
- ✅ No Python installation needed
- ✅ Exact same environment everywhere
- ✅ All dependencies included
- ✅ Works on any machine with Docker

---

## Why Docker Matters for CI/CD

**In CI/CD pipelines:**
1. Build Docker image
2. Run tests in container
3. Push image to registry
4. Deploy same image to production

**Benefits:**
- 🎯 Test in same environment as production
- 🎯 No "works on my machine" problems
- 🎯 Easy to deploy anywhere (AWS, Azure, GCP, etc.)
- 🎯 Consistent builds every time

---

## Quick Experiment

**Try this to see Docker's power:**

1. Build the image: `docker build -t cicd-app .`
2. Run it: `docker run -d -p 5000:5000 cicd-app`
3. Test: `curl http://localhost:5000/health`
4. Stop it: `docker stop $(docker ps -q)`

**You just:**
- Built a complete environment
- Started the app
- Tested it
- Stopped it

All without installing Python or dependencies on your machine!

---

## Checkpoint ✅

**You should now understand:**
- ✅ What Docker is and why it's useful
- ✅ How to build a Docker image
- ✅ How to run a container
- ✅ Why Docker is important for CI/CD

**Time check:** You should be at **1:00** (Hour 1 complete!)

---

## What You Learned

- 🎯 Docker packages apps with their dependencies
- 🎯 Dockerfiles define how to build images
- 🎯 Containers run from images
- 🎯 Same container works everywhere
- 🎯 Docker eliminates environment issues

---

## Hour 1 Complete! 🎉

**You've learned:**
- ✅ Flask application structure
- ✅ Running apps locally
- ✅ Writing automated tests
- ✅ Docker containerization

**You're ready for Hour 2!**

### [→ Continue to Hour 2: CI/CD Pipeline](../hour-2/README.md)

---

**Don't have Docker?** That's okay! You can still continue to Hour 2. Docker will be used in the CI/CD pipeline, which runs in the cloud.
