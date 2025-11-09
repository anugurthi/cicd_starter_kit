"""
Unit tests for the Flask application
These tests will run automatically in the CI/CD pipeline
"""

import unittest
import json
from app import app, add, multiply


class TestFlaskApp(unittest.TestCase):
    """Test cases for Flask endpoints"""
    
    def setUp(self):
        """Set up test client before each test"""
        self.app = app.test_client()
        self.app.testing = True
    
    def test_home_endpoint(self):
        """Test the home endpoint returns HTML UI"""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'CI/CD Starter Kit', response.data)
    
    def test_api_endpoint(self):
        """Test the API documentation endpoint"""
        response = self.app.get('/api')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIn('message', data)
        self.assertEqual(data['status'], 'running')
    
    def test_health_endpoint(self):
        """Test health check endpoint"""
        response = self.app.get('/health')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['status'], 'healthy')
    
    def test_get_tasks(self):
        """Test getting all tasks"""
        response = self.app.get('/tasks')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIn('tasks', data)
        self.assertIn('count', data)
        self.assertIsInstance(data['tasks'], list)
    
    def test_create_task(self):
        """Test creating a new task"""
        new_task = {"title": "Test Task", "completed": False}
        response = self.app.post('/tasks',
                                 data=json.dumps(new_task),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.data)
        self.assertEqual(data['title'], 'Test Task')
        self.assertIn('id', data)
    
    def test_create_task_without_title(self):
        """Test creating task without title returns error"""
        response = self.app.post('/tasks',
                                 data=json.dumps({}),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 400)
    
    def test_get_single_task(self):
        """Test getting a single task by ID"""
        response = self.app.get('/tasks/1')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['id'], 1)
    
    def test_get_nonexistent_task(self):
        """Test getting a task that doesn't exist"""
        response = self.app.get('/tasks/9999')
        self.assertEqual(response.status_code, 404)
    
    def test_update_task(self):
        """Test updating a task"""
        update_data = {"title": "Updated Task", "completed": True}
        response = self.app.put('/tasks/1',
                               data=json.dumps(update_data),
                               content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['title'], 'Updated Task')
        self.assertTrue(data['completed'])


class TestUtilityFunctions(unittest.TestCase):
    """Test cases for utility functions"""
    
    def test_add_function(self):
        """Test addition function"""
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)
    
    def test_multiply_function(self):
        """Test multiplication function"""
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-1, 5), -5)
        self.assertEqual(multiply(0, 100), 0)


if __name__ == '__main__':
    unittest.main()
