"""
Simple Flask Web Application for CI/CD Learning
This app demonstrates a basic web service with multiple endpoints
"""

from flask import Flask, jsonify, request, render_template
from datetime import datetime

# Initialize the Flask application
# This is like starting the engine of a car
app = Flask(__name__)

# In-memory storage for demonstration
# NOTE: In a real app, we would use a database (like PostgreSQL or SQLite)
# But for learning, a simple list is easier to understand!
tasks = [
    {"id": 1, "title": "Learn CI/CD", "completed": False},
    {"id": 2, "title": "Build a pipeline", "completed": False}
]


@app.route('/')
def home():
    """
    Home endpoint - returns the web UI.
    When you visit http://localhost:5000, this function runs.
    """
    return render_template('index.html')


@app.route('/api')
def api_home():
    """API documentation endpoint"""
    return jsonify({
        "message": "Welcome to CI/CD Starter Kit API!",
        "status": "running",
        "timestamp": datetime.now().isoformat(),
        "endpoints": {
            "/": "Web UI (Task Manager)",
            "/api": "API documentation (this page)",
            "/health": "Health check",
            "/tasks": "Get all tasks (GET) or create task (POST)",
            "/tasks/<id>": "Get, update (PUT), or delete (DELETE) a specific task"
        }
    })


@app.route('/health')
def health():
    """
    Health check endpoint for monitoring.
    CI/CD pipelines use this to check if the app is alive and working.
    """
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.now().isoformat()
    }), 200


@app.route('/tasks', methods=['GET', 'POST'])
def handle_tasks():
    """Handle task list operations"""
    if request.method == 'GET':
        return jsonify({
            "tasks": tasks,
            "count": len(tasks)
        })
    
    elif request.method == 'POST':
        data = request.get_json()
        if not data or 'title' not in data:
            return jsonify({"error": "Title is required"}), 400
        
        new_task = {
            "id": max([t['id'] for t in tasks], default=0) + 1,
            "title": data['title'],
            "completed": data.get('completed', False)
        }
        tasks.append(new_task)
        return jsonify(new_task), 201


@app.route('/tasks/<int:task_id>', methods=['GET', 'PUT', 'DELETE'])
def handle_task(task_id):
    """Handle individual task operations"""
    task = next((t for t in tasks if t['id'] == task_id), None)
    
    if not task:
        return jsonify({"error": "Task not found"}), 404
    
    if request.method == 'GET':
        return jsonify(task)
    
    elif request.method == 'PUT':
        data = request.get_json()
        if 'title' in data:
            task['title'] = data['title']
        if 'completed' in data:
            task['completed'] = data['completed']
        return jsonify(task)
    
    elif request.method == 'DELETE':
        tasks.remove(task)
        return jsonify({"message": "Task deleted"}), 200


def add(a, b):
    """Simple addition function for testing"""
    return a + b


def multiply(a, b):
    """Simple multiplication function for testing"""
    return a * b


if __name__ == '__main__':
    print("\n" + "="*70)
    print("🚀 CI/CD STARTER KIT - Flask Application Starting...")
    print("="*70)
    print("\n✨ Welcome! Your application is starting up!\n")
    print("📍 Your app will be available at:")
    print("   → http://localhost:5000")
    print("   → http://127.0.0.1:5000")
    print("\n📚 Available Endpoints:")
    print("   → GET  /              - Welcome message & API documentation")
    print("   → GET  /health        - Health check endpoint")
    print("   → GET  /tasks         - Get all tasks")
    print("   → POST /tasks         - Create a new task")
    print("   → GET  /tasks/<id>    - Get a specific task")
    print("   → PUT  /tasks/<id>    - Update a task")
    print("   → DELETE /tasks/<id>  - Delete a task")
    print("\n💡 Quick Test:")
    print("   Open your browser and visit: http://localhost:5000")
    print("   Or try: curl http://localhost:5000/health")
    print("\n⚡ Tips:")
    print("   • Press CTRL+C to stop the server")
    print("   • Check README.md for complete guide")
    print("   • Run 'python3 -m pytest test_app.py -v' to run tests")
    print("\n" + "="*70)
    print("🎉 Happy Learning! Let's build something awesome!")
    print("="*70 + "\n")
    
    app.run(host='0.0.0.0', port=5000, debug=True)
