# Step 2: First Pipeline

**Time:** 15 minutes  
**Goal:** Trigger your first automated CI/CD pipeline

---

## What You'll Do

1. Make a small code change
2. Commit and push to GitHub
3. Watch GitHub Actions run automatically
4. See your first pipeline complete!

---

## The Magic Moment

When you push code to GitHub, **GitHub Actions automatically:**
1. Checks out your code
2. Runs linting (code quality checks)
3. Runs all tests
4. Builds a Docker image
5. Reports results

**All without you doing anything!** This is CI/CD! 🎉

---

## Tasks

### 1. Make a Small Change (2 min)

Let's add a comment to the README:

```bash
echo "" >> README.md
echo "<!-- I'm learning CI/CD! -->" >> README.md
```

**Or** open `README.md` and add any small change.

---

### 2. Commit the Change (2 min)

```bash
git add README.md
git commit -m "Trigger my first CI/CD pipeline"
```

✅ **Change committed!**

---

### 3. Push to GitHub (1 min)

```bash
git push
```

**This is the magic moment!** 🪄

---

### 4. Watch the Pipeline Run (10 min)

1. Go to your GitHub repository
2. Click the **"Actions"** tab (top menu)
3. You should see a workflow running!

**You'll see:**
```
● Trigger my first CI/CD pipeline
  Running...
```

Click on it to see details!

---

## Understanding the Pipeline View

### Workflow Run Page

You'll see **5 jobs** running:

```
1. ✓ Code Quality Check (lint)
2. ✓ Run Unit Tests (test)
3. ✓ Build Docker Image (build)
4. ○ Deploy Application (deploy) - Skipped
5. ✓ Send Notifications (notify)
```

**Click on any job** to see what it's doing!

---

### Job Details

Click on **"Run Unit Tests"** to see:

```
Set up job
Run actions/checkout@v3
Set up Python 3.9
Install dependencies
Run tests with pytest
  ✓ test_home_endpoint PASSED
  ✓ test_health_endpoint PASSED
  ✓ test_get_tasks PASSED
  ...
  ============= 13 passed in 0.15s =============
Post Run actions/checkout@v3
Complete job
```

**This is your code being tested automatically!**

---

## What Just Happened?

```
You pushed code
     ↓
GitHub detected the push
     ↓
GitHub Actions started
     ↓
Workflow file (.github/workflows/ci-cd.yml) was read
     ↓
Jobs ran in sequence:
  1. Lint - Check code quality ✓
  2. Test - Run all tests ✓
  3. Build - Create Docker image ✓
  4. Deploy - (Skipped, only runs on main branch)
  5. Notify - Report results ✓
     ↓
All jobs completed successfully! 🎉
```

---

## Exploring the Actions Tab

### Workflow Runs
- Shows all pipeline runs
- Green ✓ = Success
- Red ✗ = Failed
- Yellow ● = Running

### Click on a run to see:
- Which jobs ran
- How long each took
- Logs for each step
- Any errors or warnings

---

## Quick Experiment

**Try making another change:**

```bash
echo "# CI/CD is awesome!" >> README.md
git add README.md
git commit -m "Test pipeline again"
git push
```

**Then:**
1. Go to Actions tab
2. Watch the new pipeline run
3. See it complete successfully!

**You just triggered CI/CD twice!** 🚀

---

## Understanding the Timeline

```
0:00 - You push code
0:05 - GitHub Actions starts
0:10 - Lint job completes
0:30 - Test job completes (runs on 3 Python versions!)
1:00 - Build job completes
1:05 - Notify job completes
1:10 - Pipeline complete! ✓
```

**Total time:** ~1-2 minutes from push to completion!

---

## Checkpoint ✅

**You should now have:**
- ✅ Made a code change
- ✅ Pushed to GitHub
- ✅ Seen the Actions tab
- ✅ Watched a pipeline run successfully
- ✅ Seen all jobs complete

**Time check:** You should be at **1:30** (30 minutes into Hour 2)

---

## What You Learned

- 🎯 Pushing code triggers GitHub Actions automatically
- 🎯 Pipelines run multiple jobs (lint, test, build, etc.)
- 🎯 You can see real-time logs in the Actions tab
- 🎯 Green checkmarks mean everything passed!
- 🎯 This happens on EVERY push - that's CI/CD!

---

## This is CI/CD!

**What you just experienced:**
- ✅ **Continuous Integration** - Code was automatically tested
- ✅ **Automated Quality Checks** - Linting ran automatically
- ✅ **Fast Feedback** - Results in ~1 minute
- ✅ **No Manual Work** - Everything happened automatically

**This is what professional teams use every day!**

---

## Next Step

Now that you've seen it work, let's understand HOW it works!

### [→ Step 3: Understand Pipeline](03-understand-pipeline.md)

---

**Pro tip:** Bookmark the Actions tab - you'll be checking it often!
