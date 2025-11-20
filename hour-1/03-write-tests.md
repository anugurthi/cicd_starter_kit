# Step 3: Write Tests

**Time:** 15 minutes  
**Goal:** Write and run automated tests for the Flask app

---

## What You'll Do

1. Understand existing tests
2. Run the test suite
3. Write a new test
4. Check test coverage

---

## Why Testing Matters

**Without tests:**
- 😰 Fear of breaking things when making changes
- 🐛 Bugs slip into production
- 🤷 No confidence in your code

**With tests:**
- ✅ Confidence to refactor
- ✅ Catch bugs before users do
- ✅ Documentation of how code should work

---

## Tasks

### 1. Explore Existing Tests (5 min)

Open `app/test_app.py` in your editor.

**Find these test functions:**

- [ ] `test_home_endpoint()` - Tests the home page
- [ ] `test_health_endpoint()` - Tests `/health`
- [ ] `test_get_tasks()` - Tests getting all tasks
- [ ] `test_create_task()` - Tests creating a task
- [ ] `test_update_task()` - Tests updating a task
- [ ] `test_delete_task()` - Tests deleting a task

**Look at the pattern:**
```python
def test_health_endpoint(self):
    response = self.client.get('/health')  # Make request
    self.assertEqual(response.status_code, 200)  # Check status
    data = response.get_json()  # Get JSON data
    self.assertEqual(data['status'], 'healthy')  # Check content
```

**Every test follows this pattern:**
1. **Arrange** - Set up the test
2. **Act** - Do something (make a request)
3. **Assert** - Check the result

---

### 2. Run All Tests (3 min)

In your terminal:

```bash
cd app
python3 -m pytest test_app.py -v
```

**You should see:**
```
test_app.py::TestFlaskApp::test_home_endpoint PASSED
test_app.py::TestFlaskApp::test_health_endpoint PASSED
test_app.py::TestFlaskApp::test_get_tasks PASSED
...
============= 13 passed in 0.15s =============
```

✅ **All tests passing!** This means the app works as expected.

---

### 3. Write Your Own Test (5 min)

Let's add a test for the API documentation endpoint (`/api`).

**Add this to `test_app.py`** (after the other test methods):

```python
def test_api_endpoint(self):
    """Test the API documentation endpoint"""
    response = self.client.get('/api')
    self.assertEqual(response.status_code, 200)
    data = response.get_json()
    self.assertIn('endpoints', data)
```

**Save the file** and run tests again:

```bash
python3 -m pytest test_app.py -v
```

**You should now see:**
```
============= 14 passed in 0.16s =============
```

🎉 **You just wrote your first test!**

---

### 4. Check Test Coverage (2 min)

Test coverage shows which lines of code are tested.

```bash
python3 -m pytest test_app.py --cov=app --cov-report=term
```

**You should see:**
```
Name     Stmts   Miss  Cover
----------------------------
app.py      45      3    93%
```

**93% coverage** means 93% of your code is tested. Great!

---

## Understanding Test Output

### When tests pass ✅
```
test_health_endpoint PASSED
```
Means: The endpoint works as expected!

### When tests fail ❌
```
test_health_endpoint FAILED
AssertionError: 'healthy' != 'unhealthy'
```
Means: Something broke! The endpoint returned unexpected data.

---

## Quick Experiment

**Let's break a test on purpose:**

1. Open `app/app.py`
2. Find the `/health` endpoint
3. Change `"status": "healthy"` to `"status": "broken"`
4. Run tests: `pytest test_app.py -v`

**You should see:**
```
test_health_endpoint FAILED
```

**This is good!** Tests caught the bug before it reached users.

5. **Fix it** - Change it back to `"healthy"`
6. Run tests again - they should pass ✅

---

## Checkpoint ✅

**You should now understand:**
- ✅ How to read test code
- ✅ How to run tests with pytest
- ✅ How to write a simple test
- ✅ What test coverage means
- ✅ How tests catch bugs

**Time check:** You should be at **0:45** (45 minutes into Hour 1)

---

## What You Learned

- 🎯 Tests follow the Arrange-Act-Assert pattern
- 🎯 pytest makes testing easy in Python
- 🎯 Good tests give you confidence to change code
- 🎯 Test coverage shows what's tested
- 🎯 Failing tests are good - they catch bugs!

---

## Next Step

Now that we have tests, let's package the app with Docker!

### [→ Step 4: Docker Basics](04-docker-basics.md)

---

**Pro tip:** Run tests before every commit. It's your safety net!
