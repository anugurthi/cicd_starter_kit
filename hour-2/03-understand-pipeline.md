# Step 3: Understand Pipeline

**Time:** 15 minutes  
**Goal:** Deep dive into how the CI/CD pipeline works

---

## What You'll Do

1. Explore the workflow file
2. Understand YAML syntax
3. Learn about each pipeline stage
4. Understand triggers and conditions

---

## The Workflow File

Everything is defined in `.github/workflows/ci-cd.yml`

**Open this file** in your editor and let's break it down!

---

## Part 1: Triggers (When to Run)

```yaml
on:
  push:
    branches: [ master, main, develop ]
  pull_request:
    branches: [ master, main ]
```

**Meaning:**
- Run on **push** to main, master, or develop branches
- Run on **pull requests** to main or master

**This is why** the pipeline ran when you pushed!

---

## Part 2: Jobs (What to Run)

The pipeline has **5 jobs**:

### Job 1: Lint (Code Quality)
```yaml
lint:
  name: Code Quality Check
  runs-on: ubuntu-latest
  steps:
    - uses: actions/checkout@v3
    - uses: actions/setup-python@v4
    - run: pip install flake8
    - run: flake8 app/ --max-line-length=127
```

**What it does:**
1. Checks out your code
2. Sets up Python
3. Installs flake8 (linting tool)
4. Checks code style

---

### Job 2: Test (Run Tests)
```yaml
test:
  needs: lint  # Waits for lint to finish
  strategy:
    matrix:
      python-version: ['3.8', '3.9', '3.10']
  steps:
    - run: pytest test_app.py -v --cov=app
```

**What it does:**
1. Waits for lint to pass
2. Runs tests on **3 Python versions** (matrix strategy!)
3. Generates coverage report

**Matrix strategy** means it runs the same tests 3 times with different Python versions!

---

### Job 3: Build (Docker Image)
```yaml
build:
  needs: test  # Waits for tests to pass
  steps:
    - run: docker build -t cicd-app .
    - run: docker run -d -p 5000:5000 cicd-app
    - run: curl http://localhost:5000/health
```

**What it does:**
1. Waits for tests to pass
2. Builds Docker image
3. Runs container
4. Tests the health endpoint

---

### Job 4: Deploy (Production)
```yaml
deploy:
  needs: build
  if: github.ref == 'refs/heads/main'  # Only on main branch!
  steps:
    - run: echo "🚀 Deploying..."
```

**What it does:**
1. Waits for build to succeed
2. **Only runs on main branch** (that's the `if` condition)
3. Simulates deployment

**This is why** it was skipped earlier - you might not be on the main branch!

---

### Job 5: Notify (Report Results)
```yaml
notify:
  needs: [lint, test, build, deploy]
  if: always()  # Runs even if previous jobs fail
  steps:
    - run: echo "Pipeline completed!"
```

**What it does:**
1. Runs after all other jobs
2. **Always runs** even if something failed
3. Reports status

---

## Understanding YAML Syntax

YAML uses **indentation** to show structure:

```yaml
job_name:              # Job
  name: Display Name   # Job property
  steps:               # List of steps
    - name: Step 1     # First step
      run: echo "Hi"   # Step property
    - name: Step 2     # Second step
      run: echo "Bye"  # Step property
```

**Key points:**
- Indentation matters (use 2 spaces)
- `-` indicates list items
- `:` separates keys and values

---

## Job Dependencies

```
lint
  ↓
test (waits for lint)
  ↓
build (waits for test)
  ↓
deploy (waits for build, only on main)
  ↓
notify (waits for all, always runs)
```

**This is called a pipeline!** Jobs run in sequence.

---

## Understanding `needs`

```yaml
test:
  needs: lint  # This job waits for 'lint' to complete
```

**Without `needs`:** Jobs run in parallel  
**With `needs`:** Jobs run in sequence

**Why?** You don't want to build if tests fail!

---

## Understanding `if` Conditions

```yaml
deploy:
  if: github.ref == 'refs/heads/main'
```

**Meaning:** Only run this job if we're on the main branch

**Other examples:**
```yaml
if: success()           # Only if previous jobs succeeded
if: failure()           # Only if previous jobs failed
if: always()            # Always run
```

---

## Quick Experiment

**Let's see the workflow in action:**

1. Open `.github/workflows/ci-cd.yml`
2. Find the `notify` job
3. Change the echo message to: `echo "🎉 My pipeline works!"`
4. Save, commit, and push:

```bash
git add .github/workflows/ci-cd.yml
git commit -m "Customize notify message"
git push
```

5. Go to Actions tab
6. Click on the new run
7. Click on "Send Notifications" job
8. You should see your custom message!

---

## Checkpoint ✅

**You should now understand:**
- ✅ Where the pipeline is defined (`.github/workflows/ci-cd.yml`)
- ✅ When it runs (on push and pull requests)
- ✅ What each job does (lint, test, build, deploy, notify)
- ✅ How jobs depend on each other (`needs`)
- ✅ How to use conditions (`if`)
- ✅ Basic YAML syntax

**Time check:** You should be at **1:45** (45 minutes into Hour 2)

---

## What You Learned

- 🎯 Workflows are defined in YAML files
- 🎯 Jobs run in sequence using `needs`
- 🎯 Conditions control when jobs run
- 🎯 Matrix strategy runs same job with different versions
- 🎯 You can customize every part of the pipeline

---

## Next Step

Now let's learn by breaking things (and fixing them)!

### [→ Step 4: Break and Fix](04-break-and-fix.md)

---

**Pro tip:** The workflow file is just code - you can modify it like any other file!
