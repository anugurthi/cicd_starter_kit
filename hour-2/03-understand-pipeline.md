# Step 3: Understand Pipeline

**Time:** 15 minutes  
**Goal:** Learn how the CI/CD pipeline works.

---

## What You'll Do
1. Open the workflow file `.github/workflows/ci-cd.yml`.
2. Learn the basic YAML structure.
3. Understand the pipeline stages.

---

## Quick Overview
- **Triggers:** Runs on pushes to `main`, `master`, `develop` and on pull requests to `main` or `master`.
- **Jobs:**
  - **lint:** Checks code style.
  - **test:** Runs tests on multiple Python versions.
  - **build:** Builds the Docker image.
  - **deploy:** Deploys on the `main` branch.
  - **notify:** Always runs, reports the result.

---

## YAML Basics (very short)
```yaml
job_name:
  name: Display Name
  runs-on: ubuntu-latest
  steps:
    - name: Step 1
      run: echo "Hi"
```
- Indentation matters (use spaces).
- `-` starts a list item.

---

## Quick Experiment
1. Open `.github/workflows/ci-cd.yml`.
2. Change the `notify` job echo to `echo "🎉 Pipeline works!"`.
3. Commit and push:
```bash
git add .github/workflows/ci-cd.yml
git commit -m "Customize notify message"
git push
```
4. Check the **Actions** tab on GitHub to see the run.

---

## Checkpoint ✅
You should now understand:
- Where the pipeline is defined.
- When it runs.
- What each job does.
- Basic YAML syntax.

**Time check:** ~15 minutes.

---

## Next Step
[→ Step 4: Break and Fix](04-break-and-fix.md)
