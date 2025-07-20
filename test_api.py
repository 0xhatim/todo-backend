#!/usr/bin/env python3
"""
Simple test script to verify the Todo API endpoints
Run this after starting the Django server
"""

import requests
import json

BASE_URL = "http://127.0.0.1:8000/api/v1"

def test_api():
    """Test the API endpoints"""
    print("🧪 Testing Todo API...")
    print("=" * 50)
    
    # Test 1: Check if server is running
    try:
        response = requests.get(f"{BASE_URL}/auth/register/")
        print("✅ Server is running")
    except requests.exceptions.ConnectionError:
        print("❌ Server is not running. Please start with: python manage.py runserver")
        return
    
    # Test 2: Register a new user
    print("\n📝 Testing User Registration...")
    register_data = {
        "username": "htom22shi",
        "email": "0xhatimm211@gmail.com.com",
        "password": "testpass123",
        "password_confirm": "testpass123",
        "first_name": "Test",
        "last_name": "User"
    }
    
    response = requests.post(f"{BASE_URL}/auth/register/", json=register_data)
    print(response.text)
    if response.status_code == 201:
        print("✅ User registration successful")
        user_data = response.json()
        access_token = user_data['tokens']['access']
        refresh_token = user_data['tokens']['refresh']
    else:
        print(f"❌ Registration failed: {response.status_code}")
        print(response.text)
        return
    
    # Test 3: Login
    print("\n🔐 Testing User Login...")
    login_data = {
        "email": "test@example.com",
        "password": "testpass123"
    }
    
    response = requests.post(f"{BASE_URL}/auth/login/", json=login_data)
    print(response.text)
    if response.status_code == 200:
        print("✅ User login successful")
    else:
        print(f"❌ Login failed: {response.status_code}")
        print(response.text)
    
    # Test 4: Get Profile
    print("\n👤 Testing Profile Retrieval...")
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(f"{BASE_URL}/auth/profile/", headers=headers)
    print(response.text)
    if response.status_code == 200:
        print("✅ Profile retrieval successful")
        profile = response.json()
        print(f"   User: {profile['username']} ({profile['email']})")
    else:
        print(f"❌ Profile retrieval failed: {response.status_code}")
    
    # Test 5: Create Todo
    print("\n📝 Testing Todo Creation...")
    todo_data = {
        "title": "Test Todo Item",
        "description": "This is a test todo item",
        "status": "PENDING",
        "priority": "MEDIUM"
    }
    
    response = requests.post(f"{BASE_URL}/todos/", json=todo_data, headers=headers)
    print(response.text)

    if response.status_code == 201:
        print("✅ Todo creation successful")
        todo = response.json()['todo']
        todo_id = todo['id']
    else:
        print(f"❌ Todo creation failed: {response.status_code}")
        print(response.text)
        return
    
    # Test 6: Get Todos List
    print("\n📋 Testing Todos List...")
    response = requests.get(f"{BASE_URL}/todos/", headers=headers)
    print(response.text)

    if response.status_code == 200:
        todos = response.json()
        print(f"✅ Todos list retrieved ({todos['count']} todos)")
    else:
        print(f"❌ Todos list failed: {response.status_code}")
    
    # Test 7: Update Todo
    print("\n✏️ Testing Todo Update...")
    update_data = {
        "title": "Updated Test Todo",
        "description": "This todo has been updated",
        "status": "IN_PROGRESS",
        "priority": "HIGH"
    }
    
    response = requests.put(f"{BASE_URL}/todos/{todo_id}/", json=update_data, headers=headers)
    print(response.text)

    if response.status_code == 200:
        print("✅ Todo update successful")
    else:
        print(f"❌ Todo update failed: {response.status_code}")
    
    # Test 8: Get Todo Statistics
    print("\n📊 Testing Todo Statistics...")
    response = requests.get(f"{BASE_URL}/todos/stats/", headers=headers)
    print(response.text)

    if response.status_code == 200:
        stats = response.json()
        print("✅ Todo statistics retrieved")
        print(f"   Total: {stats['total_todos']}")
        print(f"   Pending: {stats['pending_todos']}")
        print(f"   In Progress: {stats['in_progress_todos']}")
        print(f"   Completed: {stats['completed_todos']}")
    else:
        print(f"❌ Todo statistics failed: {response.status_code}")
    
    # Test 9: Delete Todo
    print("\n🗑️ Testing Todo Deletion...")
    response = requests.delete(f"{BASE_URL}/todos/{todo_id}/", headers=headers)
    if response.status_code == 200:
        print("✅ Todo deletion successful")
    else:
        print(f"❌ Todo deletion failed: {response.status_code}")
    
    # Test 10: Logout
    print("\n🚪 Testing Logout...")
    logout_data = {"refresh_token": refresh_token}
    response = requests.post(f"{BASE_URL}/auth/logout/", json=logout_data, headers=headers)
    print(response.text)

    if response.status_code == 200:
        print("✅ Logout successful")
    else:
        print(f"❌ Logout failed: {response.status_code}")
    
    print("\n" + "=" * 50)
    print("🎉 All tests completed!")
    print("\n📚 API Documentation available at:")
    print("   - ReDoc: http://127.0.0.1:8000/api/docs/redoc/")
    print("   - Swagger: http://127.0.0.1:8000/api/docs/")
    print("   - Admin: http://127.0.0.1:8000/admin/")

if __name__ == "__main__":
    test_api() 