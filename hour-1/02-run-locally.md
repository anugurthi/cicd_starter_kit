# Step 2: Run Locally

**Time:** 15 minutes  
**Goal:** Get the Flask app running on your machine

---

## What You'll Do

1. Start the Flask development server
2. Test the app in your browser
3. Test the API with curl commands

---

## Tasks

### 1. Start the Flask App (3 min)

Open your terminal and run:

```bash
cd app
python3 app.py
```

**You should see:**
```
 * Running on http://127.0.0.1:5000
 * Debug mode: on
```

✅ **Success!** Your app is running!

**Troubleshooting:**
- `ModuleNotFoundError`? → Run `pip install -r requirements.txt`
- `Port 5000 in use`? → Kill the process: `lsof -i :5000` then `kill -9 <PID>`

---

### 2. Test in Browser (5 min)

Open your web browser and visit: **http://localhost:5000**

**You should see:**
- A beautiful task manager interface
- Two sample tasks
- Buttons to add, edit, and delete tasks

**Try these actions:**

- [ ] **Add a task** - Type "Learn CI/CD" and click Add
- [ ] **Mark complete** - Click the checkbox next to a task
- [ ] **Delete a task** - Click the delete button (🗑️)

**What's happening?**
- Your browser sends HTTP requests to Flask
- Flask processes them and returns responses
- The UI updates based on the responses

---

### 3. Test the Health Endpoint (2 min)

Keep the app running. Open a **new terminal** and run:

```bash
curl http://localhost:5000/health
```

**You should see:**
```json
{
  "status": "healthy",
  "timestamp": "2024-11-20T18:50:00"
}
```

✅ **This is your first API call!**

---

### 4. Test All API Endpoints (5 min)

Try these curl commands:

#### Get all tasks
```bash
curl http://localhost:5000/tasks
```

**Expected:** JSON array of tasks

#### Get a specific task
```bash
curl http://localhost:5000/tasks/1
```

**Expected:** JSON object for task with id=1

#### Create a new task
```bash
curl -X POST http://localhost:5000/tasks \
  -H "Content-Type: application/json" \
  -d '{"title": "Learn CI/CD", "completed": false}'
```

**Expected:** JSON of the newly created task

#### Update a task
```bash
curl -X PUT http://localhost:5000/tasks/1 \
  -H "Content-Type: application/json" \
  -d '{"completed": true}'
```

**Expected:** JSON of the updated task

#### Delete a task
```bash
curl -X DELETE http://localhost:5000/tasks/1
```

**Expected:** Success message

---

## Understanding the Output

When you run curl commands, you're seeing **JSON responses**:

```json
{
  "id": 1,
  "title": "Learn Flask",
  "completed": false
}
```

This is the same data your browser gets, just displayed as raw JSON!

---

## Quick Experiment

**Try this:**

1. In your browser, add a task called "Test Task"
2. In your terminal, run: `curl http://localhost:5000/tasks`
3. You should see your new task in the JSON response!

**What does this prove?**
- The browser and curl are using the same API
- REST APIs work the same regardless of the client
- JSON is the universal language for APIs

---

## Checkpoint ✅

**You should now be able to:**
- ✅ Start the Flask development server
- ✅ Access the app in your browser
- ✅ Make API calls with curl
- ✅ See JSON responses

**Time check:** You should be at **0:30** (30 minutes into Hour 1)

---

## What You Learned

- 🎯 Flask runs a development server on port 5000
- 🎯 You can test APIs with both browser and curl
- 🎯 REST APIs return JSON data
- 🎯 Same API works for different clients (browser, curl, mobile apps, etc.)

---

## Next Step

Now that the app is running, let's write tests for it!

### [→ Step 3: Write Tests](03-write-tests.md)

---

**Pro tip:** Keep the Flask app running in one terminal while you work in another!
