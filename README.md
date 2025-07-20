# Todo API - Django REST API with JWT Authentication

A simple and powerful Todo API built with Django REST Framework, featuring JWT authentication, user management, and comprehensive API documentation.

## 🚀 Features

- **JWT Authentication** with access and refresh tokens
- **User Registration & Login** with email/password
- **Profile Management** with picture upload
- **Complete Todo CRUD** operations
- **Bulk Operations** for todos
- **API Documentation** with ReDoc and Swagger
- **Admin Interface** for database management
- **CORS Support** for frontend integration

## 📋 Requirements

- Python 3.8+
- Django 5.2+
- Django REST Framework
- JWT Authentication
- SQLite (development)

## 🛠️ Installation & Setup

### 1. Clone and Setup Environment

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Environment Configuration

Copy the environment example file:
```bash
cp env.example .env
```

Edit `.env` file with your settings:
```env
DEBUG=True
SECRET_KEY=your-secret-key-here
ALLOWED_HOSTS=localhost,127.0.0.1
CORS_ALLOW_ALL_ORIGINS=True
```

### 3. Database Setup

```bash
# Create and apply migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser for admin access
python manage.py createsuperuser
```

### 4. Run Development Server

```bash
python manage.py runserver
```

The API will be available at: `http://127.0.0.1:8000/`

## 📚 API Documentation

### Interactive Documentation
- **ReDoc UI**: http://127.0.0.1:8000/api/docs/redoc/
- **Swagger UI**: http://127.0.0.1:8000/api/docs/
- **API Schema**: http://127.0.0.1:8000/api/schema/

### Admin Interface
- **Django Admin**: http://127.0.0.1:8000/admin/

## 🔐 Authentication Endpoints

### Register User
```http
POST /api/v1/auth/register/
Content-Type: application/json

{
    "username": "john_doe",
    "email": "john@example.com",
    "password": "securepassword123",
    "password_confirm": "securepassword123",
    "first_name": "John",
    "last_name": "Doe"
}
```

### Login User
```http
POST /api/v1/auth/login/
Content-Type: application/json

{
    "email": "john@example.com",
    "password": "securepassword123"
}
```

### Refresh Token
```http
POST /api/v1/auth/refresh/
Content-Type: application/json

{
    "refresh": "your-refresh-token-here"
}
```

### Logout User
```http
POST /api/v1/auth/logout/
Authorization: Bearer your-access-token
Content-Type: application/json

{
    "refresh_token": "your-refresh-token-here"
}
```

## 👤 User Profile Endpoints

### Get Profile
```http
GET /api/v1/auth/profile/
Authorization: Bearer your-access-token
```

### Update Profile
```http
PUT /api/v1/auth/profile/
Authorization: Bearer your-access-token
Content-Type: application/json

{
    "first_name": "John",
    "last_name": "Smith",
    "bio": "Software Developer"
}
```

### Upload Profile Picture
```http
POST /api/v1/auth/profile/picture/
Authorization: Bearer your-access-token
Content-Type: multipart/form-data

profile_picture: [file]
```

### Change Password
```http
POST /api/v1/auth/profile/change-password/
Authorization: Bearer your-access-token
Content-Type: application/json

{
    "old_password": "currentpassword",
    "new_password": "newpassword123",
    "new_password_confirm": "newpassword123"
}
```

## 📝 Todo Endpoints

### List Todos
```http
GET /api/v1/todos/
Authorization: Bearer your-access-token

# Optional query parameters:
# ?status=PENDING&priority=HIGH&search=meeting&ordering=-created_at
```

### Create Todo
```http
POST /api/v1/todos/
Authorization: Bearer your-access-token
Content-Type: application/json

{
    "title": "Complete project documentation",
    "description": "Write comprehensive API documentation",
    "status": "PENDING",
    "priority": "HIGH",
    "due_date": "2024-01-15T10:00:00Z"
}
```

### Get Todo Detail
```http
GET /api/v1/todos/{id}/
Authorization: Bearer your-access-token
```

### Update Todo
```http
PUT /api/v1/todos/{id}/
Authorization: Bearer your-access-token
Content-Type: application/json

{
    "title": "Updated todo title",
    "description": "Updated description",
    "status": "IN_PROGRESS",
    "priority": "MEDIUM",
    "due_date": "2024-01-20T10:00:00Z"
}
```

### Delete Todo
```http
DELETE /api/v1/todos/{id}/
Authorization: Bearer your-access-token
```

### Update Todo Status
```http
PATCH /api/v1/todos/{id}/status/
Authorization: Bearer your-access-token
Content-Type: application/json

{
    "status": "COMPLETED"
}
```

### Bulk Operations
```http
POST /api/v1/todos/bulk/
Authorization: Bearer your-access-token
Content-Type: application/json

# Delete multiple todos
{
    "action": "delete",
    "todo_ids": [1, 2, 3]
}

# Update status of multiple todos
{
    "action": "update_status",
    "todo_ids": [1, 2, 3],
    "status": "COMPLETED"
}
```

### Get Todo Statistics
```http
GET /api/v1/todos/stats/
Authorization: Bearer your-access-token
```

## 🔧 Configuration

### JWT Settings
- **Access Token Lifetime**: 24 hours
- **Refresh Token Lifetime**: 7 days
- **Token Rotation**: Enabled
- **Blacklist After Rotation**: Enabled

### CORS Settings
- **Allow All Origins**: True (development)
- **Allow Credentials**: True

### File Upload
- **Profile Picture Size Limit**: 5MB
- **Supported Formats**: All image formats

## 🧪 Testing the API

### Using Postman

1. **Import the API Collection**:
   - Use the Swagger UI to export OpenAPI specification
   - Import into Postman for easy testing

2. **Authentication Flow**:
   - Register a new user
   - Login to get access and refresh tokens
   - Use access token in Authorization header for protected endpoints

### Using cURL

```bash
# Register
curl -X POST http://127.0.0.1:8000/api/v1/auth/register/ \
  -H "Content-Type: application/json" \
  -d '{"username":"testuser","email":"test@example.com","password":"testpass123","password_confirm":"testpass123","first_name":"Test","last_name":"User"}'

# Login
curl -X POST http://127.0.0.1:8000/api/v1/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{"email":"test@example.com","password":"testpass123"}'

# Create Todo (use access token from login)
curl -X POST http://127.0.0.1:8000/api/v1/todos/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"title":"Test Todo","description":"Test description","status":"PENDING","priority":"MEDIUM"}'
```

## 📁 Project Structure

```
backend/
├── todo_api/          # Main Django project
│   ├── settings.py    # Django settings
│   └── urls.py        # Main URL configuration
├── users/             # User management app
│   ├── models.py      # Custom User model
│   ├── serializers.py # User serializers
│   ├── views.py       # User views
│   ├── urls.py        # User URLs
│   └── admin.py       # User admin
├── todos/             # Todo management app
│   ├── models.py      # Todo model
│   ├── serializers.py # Todo serializers
│   ├── views.py       # Todo views
│   ├── urls.py        # Todo URLs
│   └── admin.py       # Todo admin
├── requirements.txt   # Python dependencies
├── env.example        # Environment variables example
└── README.md         # This file
```

## 🚀 Next Steps

1. **Test all endpoints** using the provided documentation
2. **Create Flutter app** to consume this API
3. **Add more features** like todo categories, sharing, etc.
4. **Deploy to production** with proper security settings

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is open source and available under the MIT License. 