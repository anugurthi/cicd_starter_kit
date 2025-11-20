# Step 4: Break and Fix

**Time:** 15 minutes  
**Goal:** Learn by intentionally breaking things and fixing them

---

## What You'll Do

1. Break a test (see pipeline fail)
2. Fix it (see pipeline pass)
3. Break the code (see linting fail)
4. Fix it (see everything pass)

**Why?** The best way to learn is by seeing what happens when things go wrong!

---

## Exercise 1: Break a Test

### 1. Make a Test Fail (2 min)

Open `app/test_app.py` and find this test:

```python
def test_health_endpoint(self):
    response = self.client.get('/health')
    self.assertEqual(response.status_code, 200)
    data = response.get_json()
    self.assertEqual(data['status'], 'healthy')
```

**Change the last line to:**
```python
    self.assertEqual(data['status'], 'broken')  # Wrong on purpose!
```

### 2. Push the Broken Code (1 min)

```bash
git add app/test_app.py
git commit -m "Break test intentionally"
git push
```

### 3. Watch It Fail (3 min)

1. Go to Actions tab
2. Click on the new workflow run
3. Watch the **test job fail** ❌

**Click on the test job** to see the error:

```
AssertionError: 'healthy' != 'broken'
- healthy
+ broken
```

**This is good!** The pipeline caught the bug!

### 4. Fix It (1 min)

Change the line back to:
```python
    self.assertEqual(data['status'], 'healthy')
```

Push again:
```bash
git add app/test_app.py
git commit -m "Fix test"
git push
```

Watch it pass! ✅

---

## Exercise 2: Break the Code

### 1. Introduce a Bug (2 min)

Open `app/app.py` and find the `/health` endpoint:

```python
@app.route('/health')
def health():
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat()
    })
```

**Break it by removing a comma:**
```python
@app.route('/health')
def health():
    return jsonify({
        'status': 'healthy'  # Removed comma - syntax error!
        'timestamp': datetime.now().isoformat()
    })
```

### 2. Push the Broken Code (1 min)

```bash
git add app/app.py
git commit -m "Introduce syntax error"
git push
```

### 3. Watch Multiple Jobs Fail (2 min)

Go to Actions tab and watch:
- ❌ **Lint fails** (syntax error detected!)
- ⏭️ **Test skipped** (because lint failed)
- ⏭️ **Build skipped** (because test didn't run)

**Click on the lint job** to see:

```
app/app.py:15:24: E999 SyntaxError: invalid syntax
```

**The pipeline stopped early!** This saves time.

### 4. Fix It (1 min)

Add the comma back:
```python
        'status': 'healthy',
```

Push the fix:
```bash
git add app/app.py
git commit -m "Fix syntax error"
git push
```

Watch everything pass! ✅

---

## Exercise 3: Break Linting

### 1. Add Bad Code Style (1 min)

Add this to `app/app.py` (anywhere in the file):

```python
x=1+2+3+4+5+6+7+8+9+10+11+12+13+14+15+16+17+18+19+20+21+22+23+24+25+26+27+28+29+30
```

**This line is too long!** (over 127 characters)

### 2. Push It (1 min)

```bash
git add app/app.py
git commit -m "Add line that's too long"
git push
```

### 3. Watch Lint Fail (1 min)

The lint job will show:

```
app/app.py:XX:128: E501 line too long (XXX > 127 characters)
```

### 4. Fix It (1 min)

Remove that line and push:

```bash
git add app/app.py
git commit -m "Remove long line"
git push
```

---

## What You Learned

### 🎯 Failing Tests Stop Deployment
- Tests failed → Build didn't run
- This prevents broken code from reaching production!

### 🎯 Linting Catches Errors Early
- Syntax errors caught before tests run
- Saves time and resources

### 🎯 Pipeline Provides Fast Feedback
- You know within minutes if something broke
- Detailed error messages help you fix it

### 🎯 Every Push is Validated
- Can't accidentally push broken code
- Team is protected from bugs

---

## Understanding Failure Modes

```
Lint fails
  ↓
Tests don't run (skipped)
  ↓
Build doesn't run (skipped)
  ↓
Deploy doesn't run (skipped)
  ↓
You get notified of failure
```

**This is a safety mechanism!**

---

## Reading Error Messages

### Test Failure
```
AssertionError: 'healthy' != 'broken'
```
**Meaning:** Expected 'healthy', got 'broken'

### Syntax Error
```
E999 SyntaxError: invalid syntax
```
**Meaning:** Python can't parse the code

### Style Error
```
E501 line too long (150 > 127 characters)
```
**Meaning:** Line exceeds maximum length

---

## Checkpoint ✅

**You should now understand:**
- ✅ How to read pipeline failures
- ✅ How to debug using error messages
- ✅ Why pipelines fail fast (save time)
- ✅ How to fix common issues
- ✅ The value of automated testing

**Time check:** You should be at **2:00** (Hour 2 complete!)

---

## Hour 2 Complete! 🎉

**You've learned:**
- ✅ How to set up GitHub and push code
- ✅ How to trigger CI/CD pipelines
- ✅ How pipelines work (jobs, dependencies, conditions)
- ✅ How to debug and fix pipeline failures

**You now understand CI/CD!** 🚀

---

## What's Next?

You've completed the 2-hour workshop! Here's what you can do next:

### Immediate Next Steps
1. [Try bonus exercises](../exercises/) - Practice what you learned
2. [Deploy to production](../NEXT-STEPS.md) - Make it live!
3. [Explore advanced topics](../reference/) - Go deeper

### Share Your Success!
- ⭐ Star this repository
- 📱 Share on social media: "I just learned CI/CD in 2 hours!"
- 💬 Tell a friend about this workshop

---

## Congratulations! 🎊

You went from zero to having a complete CI/CD pipeline in 2 hours!

**You can now:**
- ✅ Build Flask APIs
- ✅ Write automated tests
- ✅ Use Docker
- ✅ Set up CI/CD pipelines
- ✅ Debug pipeline failures

**This is a valuable skill!** Put it on your resume!

---

### [🎯 See What's Next →](../NEXT-STEPS.md)

---

**Want more?** Check out the [exercises](../exercises/) for hands-on practice!
