# Step 1: Understand the App

**Time:** 15 minutes  
**Goal:** Understand what the Flask application does

---

## What You'll Do

1. Explore the application code
2. Identify the API endpoints
3. Understand the data flow

---

## Tasks

### 1. Open the Application Code (3 min)

Open `app/app.py` in your code editor.

**Look for:**
- The `Flask` import at the top
- The `@app.route()` decorators
- The functions below each route

### 2. Find All Endpoints (7 min)

The app has **7 endpoints**. Find them all and check them off:

- [ ] **`/`** - Home page (returns HTML)
- [ ] **`/health`** - Health check (returns JSON status)
- [ ] **`/api`** - API documentation
- [ ] **`GET /tasks`** - Get all tasks
- [ ] **`POST /tasks`** - Create a new task
- [ ] **`GET /tasks/<id>`** - Get a specific task
- [ ] **`PUT /tasks/<id>`** - Update a task
- [ ] **`DELETE /tasks/<id>`** - Delete a task

**Hint:** Look for lines starting with `@app.route`

### 3. Understand the Data Structure (5 min)

Look at the `tasks` list near the top of the file:

```python
tasks = [
    {"id": 1, "title": "Learn Flask", "completed": False},
    {"id": 2, "title": "Build API", "completed": False}
]
```

**Questions to answer:**
- What fields does each task have? ________________
- Where is this data stored? ________________
- What happens when you restart the app? ________________

<details>
<summary>💡 Click for answers</summary>

- **Fields:** `id`, `title`, `completed`
- **Storage:** In memory (Python list)
- **On restart:** Data is lost (not persistent)

</details>

---

## Quick Quiz

Test your understanding:

1. **How many endpoints does the app have?**
   - [ ] 5
   - [ ] 7
   - [ ] 10

2. **What does the `/health` endpoint return?**
   - [ ] HTML page
   - [ ] JSON with status
   - [ ] List of tasks

3. **What HTTP method creates a new task?**
   - [ ] GET
   - [ ] POST
   - [ ] PUT

<details>
<summary>💡 Click for answers</summary>

1. 7 endpoints
2. JSON with status
3. POST

</details>

---

## Understanding Check

Before moving on, make sure you can answer:

- ✅ What does this app do? (It's a task manager API)
- ✅ How many endpoints are there? (7)
- ✅ What data does it manage? (Tasks with id, title, completed)
- ✅ Where is the data stored? (In memory, not persistent)

---

## What You Learned

- 🎯 Flask uses `@app.route()` to define endpoints
- 🎯 REST APIs use different HTTP methods (GET, POST, PUT, DELETE)
- 🎯 JSON is used to send/receive data
- 🎯 This app stores data in memory (not a database)

---

## Checkpoint ✅

**You should now understand:**
- The app structure
- What each endpoint does
- How data flows through the app

**Time check:** You should be at **0:15** (15 minutes into Hour 1)

---

## Next Step

Now that you understand the code, let's run it!

### [→ Step 2: Run Locally](02-run-locally.md)

---

**Stuck?** Check the [reference/CHEATSHEET.md](../reference/CHEATSHEET.md) or ask for help!
