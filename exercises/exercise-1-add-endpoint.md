# Exercise 1: Add a New Endpoint

**Difficulty:** Beginner  
**Time:** 20-30 minutes  
**Goal:** Add a new API endpoint with tests

---

## Your Task

Add a `/stats` endpoint that returns statistics about the tasks.

---

## Requirements

The endpoint should:
- Be accessible at `GET /stats`
- Return JSON with:
  - `total`: Total number of tasks
  - `completed`: Number of completed tasks
  - `pending`: Number of pending tasks
  - `completion_rate`: Percentage of completed tasks

**Example response:**
```json
{
  "total": 5,
  "completed": 3,
  "pending": 2,
  "completion_rate": 60.0
}
```

---

## Step-by-Step Guide

### Step 1: Add the Endpoint (10 min)

Open `app/app.py` and add this endpoint:

```python
@app.route('/stats')
def get_stats():
    total = len(tasks)
    completed = len([t for t in tasks if t['completed']])
    pending = total - completed
    completion_rate = (completed / total * 100) if total > 0 else 0
    
    return jsonify({
        'total': total,
        'completed': completed,
        'pending': pending,
        'completion_rate': round(completion_rate, 1)
    })
```

### Step 2: Test Locally (5 min)

```bash
# Start the app
cd app
python3 app.py

# In another terminal, test the endpoint
curl http://localhost:5000/stats
```

**Expected output:**
```json
{
  "total": 2,
  "completed": 0,
  "pending": 2,
  "completion_rate": 0.0
}
```

### Step 3: Write a Test (10 min)

Open `app/test_app.py` and add this test:

```python
def test_stats_endpoint(self):
    """Test the stats endpoint"""
    response = self.client.get('/stats')
    self.assertEqual(response.status_code, 200)
    
    data = response.get_json()
    self.assertIn('total', data)
    self.assertIn('completed', data)
    self.assertIn('pending', data)
    self.assertIn('completion_rate', data)
    
    # Verify the math
    self.assertEqual(data['total'], data['completed'] + data['pending'])
```

### Step 4: Run Tests (2 min)

```bash
pytest app/test_app.py -v
```

All tests should pass! ✅

### Step 5: Push to GitHub (3 min)

```bash
git add app/app.py app/test_app.py
git commit -m "Add /stats endpoint with tests"
git push
```

Watch the pipeline run and pass!

---

## Bonus Challenges

### Challenge 1: Add More Stats
Add these fields to the response:
- `oldest_task`: Title of the oldest task
- `newest_task`: Title of the newest task

### Challenge 2: Add Query Parameters
Allow filtering by completion status:
- `/stats?completed=true` - Stats for completed tasks only
- `/stats?completed=false` - Stats for pending tasks only

### Challenge 3: Add Time-based Stats
Add a `created_at` field to tasks and calculate:
- `tasks_today`: Tasks created today
- `tasks_this_week`: Tasks created this week

---

## Solution

<details>
<summary>💡 Click to see the complete solution</summary>

**app/app.py:**
```python
@app.route('/stats')
def get_stats():
    total = len(tasks)
    completed = len([t for t in tasks if t['completed']])
    pending = total - completed
    completion_rate = (completed / total * 100) if total > 0 else 0
    
    return jsonify({
        'total': total,
        'completed': completed,
        'pending': pending,
        'completion_rate': round(completion_rate, 1)
    })
```

**app/test_app.py:**
```python
def test_stats_endpoint(self):
    response = self.client.get('/stats')
    self.assertEqual(response.status_code, 200)
    
    data = response.get_json()
    self.assertIn('total', data)
    self.assertIn('completed', data)
    self.assertIn('pending', data)
    self.assertIn('completion_rate', data)
    
    self.assertEqual(data['total'], data['completed'] + data['pending'])
```

</details>

---

## What You Learned

- ✅ How to add new API endpoints
- ✅ How to calculate statistics from data
- ✅ How to write tests for new features
- ✅ How CI/CD validates your changes

---

[← Back to Exercises](README.md) | [Next Exercise →](exercise-2-add-tests.md)
