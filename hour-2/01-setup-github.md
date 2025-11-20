# Step 1: Setup GitHub

**Time:** 15 minutes  
**Goal:** Create a GitHub repository and push your code

---

## What You'll Do

1. Create a GitHub repository
2. Initialize Git locally
3. Push your code to GitHub

---

## Why GitHub?

**GitHub provides:**
- 📦 Code hosting
- 🤝 Collaboration tools
- 🤖 **GitHub Actions** (for CI/CD)
- 📊 Project management

**For CI/CD:** GitHub Actions will automatically run tests every time you push code!

---

## Tasks

### 1. Create a GitHub Repository (5 min)

1. Go to [github.com](https://github.com)
2. Click the **"+"** icon (top right) → **"New repository"**
3. Fill in:
   - **Repository name:** `cicd_starter_kit`
   - **Description:** "Learning CI/CD in 2 hours"
   - **Visibility:** Public (or Private, your choice)
   - **DO NOT** initialize with README, .gitignore, or license
4. Click **"Create repository"**

✅ **Repository created!**

**Keep this page open** - you'll need the URL in the next step.

---

### 2. Initialize Git Locally (3 min)

In your terminal, from the `cicd_starter_kit` directory:

```bash
# Initialize Git repository
git init

# Add all files
git add .

# Make first commit
git commit -m "Initial commit: Task Manager with CI/CD"

# Rename branch to main
git branch -M main
```

✅ **Git initialized!**

**What just happened:**
- `git init` - Created a Git repository
- `git add .` - Staged all files
- `git commit` - Saved a snapshot
- `git branch -M main` - Renamed default branch to "main"

---

### 3. Connect to GitHub (2 min)

Copy the repository URL from GitHub (looks like: `https://github.com/YOUR_USERNAME/cicd_starter_kit.git`)

Then run:

```bash
git remote add origin https://github.com/YOUR_USERNAME/cicd_starter_kit.git
```

**Replace `YOUR_USERNAME` with your actual GitHub username!**

**Verify it:**
```bash
git remote -v
```

You should see your GitHub URL listed.

---

### 4. Push to GitHub (5 min)

```bash
git push -u origin main
```

**You might be asked to authenticate:**
- **Username:** Your GitHub username
- **Password:** Use a [Personal Access Token](https://github.com/settings/tokens), NOT your password

<details>
<summary>💡 How to create a Personal Access Token</summary>

1. Go to: https://github.com/settings/tokens
2. Click **"Generate new token"** → **"Generate new token (classic)"**
3. Name it: `CI/CD Workshop`
4. Select scopes: `repo` (all checkboxes under it)
5. Click **"Generate token"**
6. **Copy the token** (you won't see it again!)
7. Use this token as your password when pushing

</details>

**After pushing, you should see:**
```
Enumerating objects: 15, done.
Writing objects: 100% (15/15), done.
To https://github.com/YOUR_USERNAME/cicd_starter_kit.git
 * [new branch]      main -> main
```

✅ **Code pushed to GitHub!**

---

### 5. Verify on GitHub (1 min)

1. Go to your GitHub repository page
2. Refresh the page
3. You should see all your files!

**Check for:**
- [ ] `app/` directory
- [ ] `hour-1/` directory
- [ ] `hour-2/` directory
- [ ] `.github/workflows/ci-cd.yml`
- [ ] `README.md`

---

## Understanding Git Workflow

```
Local Machine                    GitHub
     │                              │
     │  git init                    │
     │  git add .                   │
     │  git commit                  │
     │                              │
     │  git push ──────────────────>│
     │                              │
     │                         (Code stored)
```

**Key commands:**
- `git add` - Stage changes
- `git commit` - Save snapshot locally
- `git push` - Send to GitHub

---

## Quick Reference

```bash
# Check status
git status

# See what changed
git diff

# View commit history
git log --oneline

# See remote URL
git remote -v
```

---

## Checkpoint ✅

**You should now have:**
- ✅ GitHub repository created
- ✅ Code pushed to GitHub
- ✅ All files visible on GitHub

**Time check:** You should be at **1:15** (15 minutes into Hour 2)

---

## What You Learned

- 🎯 How to create a GitHub repository
- 🎯 Basic Git commands (init, add, commit, push)
- 🎯 How to connect local code to GitHub
- 🎯 How to authenticate with GitHub

---

## Next Step

Now that your code is on GitHub, let's trigger your first CI/CD pipeline!

### [→ Step 2: First Pipeline](02-first-pipeline.md)

---

**Stuck with Git?** Check [reference/CHEATSHEET.md](../reference/CHEATSHEET.md) for more Git commands!
