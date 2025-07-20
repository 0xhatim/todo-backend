# Product Requirements Document (PRD)
## Todo App with Django API & Flutter Client

### 1. Project Overview

**Project Name:** Todo App with JWT Authentication  
**Technology Stack:** Django REST API + Flutter Mobile App  
**Environment:** Local Development (Debug Mode)  
**Authentication:** JWT with Access & Refresh Tokens  

### 2. Core Features

#### 2.1 Authentication System
- **User Registration:** Email, username, password
- **User Login:** Email/username + password
- **JWT Authentication:** 
  - Access Token (24 hours)
  - Refresh Token (7 days)
  - Automatic token refresh
- **Profile Management:** Edit profile, upload profile picture
- **Password Reset:** Email-based password reset

#### 2.2 Todo List Management
- **CRUD Operations:**
  - Create new todo items
  - Read/View todo list
  - Update todo items (title, description, status)
  - Delete todo items
- **Todo Item Properties:**
  - Title (required)
  - Description (optional)
  - Status (Pending/In Progress/Completed)
  - Created date
  - Updated date
  - Due date (optional)
  - Priority (Low/Medium/High)

#### 2.3 User Profile
- **Profile Information:**
  - Username
  - Email
  - First Name
  - Last Name
  - Profile Picture
  - Bio (optional)
- **Profile Operations:**
  - View profile
  - Edit profile information
  - Upload/Change profile picture
  - Delete account

### 3. Technical Requirements

#### 3.1 Django API Backend
**Framework:** Django 4.2+ with Django REST Framework  
**Database:** SQLite (for development)  
**Authentication:** JWT (djangorestframework-simplejwt)  
**Documentation:** ReDoc/OpenAPI 3.0  
**CORS:** Allow all origins for development  
**Debug:** True for development  

**API Endpoints Structure:**
```
/api/v1/
├── auth/
│   ├── register/ (POST)
│   ├── login/ (POST)
│   ├── refresh/ (POST)
│   ├── logout/ (POST)
│   └── password-reset/ (POST)
├── users/
│   ├── profile/ (GET, PUT, PATCH)
│   ├── profile-picture/ (POST)
│   └── delete-account/ (DELETE)
├── todos/
│   ├── list/ (GET, POST)
│   ├── detail/<id>/ (GET, PUT, PATCH, DELETE)
│   └── bulk-operations/ (POST)
└── docs/
    ├── redoc/ (ReDoc UI)
    └── swagger/ (Swagger UI)
```

#### 3.2 Flutter Mobile App
**Framework:** Flutter 3.0+  
**State Management:** Provider/Riverpod  
**HTTP Client:** Dio/HTTP  
**Local Storage:** SharedPreferences  
**Image Handling:** Image picker + caching  

**App Screens:**
```
Screens/
├── Auth/
│   ├── LoginScreen
│   ├── RegisterScreen
│   └── ForgotPasswordScreen
├── Main/
│   ├── HomeScreen (Todo List)
│   ├── AddTodoScreen
│   ├── EditTodoScreen
│   └── TodoDetailScreen
├── Profile/
│   ├── ProfileScreen
│   ├── EditProfileScreen
│   └── ChangePasswordScreen
└── Common/
    ├── SplashScreen
    └── ErrorScreen
```

### 4. API Documentation Requirements

#### 4.1 ReDoc Integration
- **OpenAPI 3.0 Specification:** Auto-generated from Django REST Framework
- **Interactive Documentation:** Available at `/api/docs/redoc/`
- **Postman Collection:** Exportable API collection
- **Authentication Examples:** JWT token usage examples
- **Request/Response Examples:** For all endpoints

#### 4.2 API Documentation Features
- **Endpoint Descriptions:** Clear purpose and usage
- **Request Parameters:** Required vs optional fields
- **Response Formats:** JSON structure examples
- **Error Codes:** HTTP status codes and error messages
- **Authentication:** JWT token requirements
- **Rate Limiting:** API usage limits (if applicable)

### 5. Security Requirements

#### 5.1 JWT Implementation
- **Access Token:** 24 hours validity
- **Refresh Token:** 7 days validity
- **Token Storage:** Secure storage in Flutter app
- **Auto-refresh:** Automatic token refresh before expiry
- **Logout:** Clear all tokens on logout

#### 5.2 Data Protection
- **Password Hashing:** Django's built-in password hashing
- **Input Validation:** Server-side validation for all inputs
- **CORS Configuration:** Allow all origins for development
- **CSRF Protection:** Disabled for API endpoints (using JWT)

### 6. Database Schema

#### 6.1 User Model
```python
User:
- id (Primary Key)
- username (Unique)
- email (Unique)
- password (Hashed)
- first_name
- last_name
- profile_picture (FileField)
- bio (TextField)
- is_active (Boolean)
- date_joined (DateTime)
- last_login (DateTime)
```

#### 6.2 Todo Model
```python
Todo:
- id (Primary Key)
- user (ForeignKey to User)
- title (CharField)
- description (TextField)
- status (ChoiceField: PENDING, IN_PROGRESS, COMPLETED)
- priority (ChoiceField: LOW, MEDIUM, HIGH)
- due_date (DateTimeField, optional)
- created_at (DateTimeField)
- updated_at (DateTimeField)
```

### 7. Development Environment Setup

#### 7.1 Django Backend Setup
- **Python Version:** 3.8+
- **Virtual Environment:** Required
- **Dependencies:** requirements.txt
- **Environment Variables:** .env file
- **Database:** SQLite (development)
- **Debug Mode:** True
- **CORS:** Allow all origins

#### 7.2 Flutter App Setup
- **Flutter Version:** 3.0+
- **Dependencies:** pubspec.yaml
- **Platform Support:** Android & iOS
- **Development:** Hot reload enabled
- **API Base URL:** Configurable for development

### 8. Testing Strategy

#### 8.1 Backend Testing
- **Unit Tests:** Django test framework
- **API Tests:** DRF test client
- **Authentication Tests:** JWT token validation
- **CRUD Tests:** Todo operations

#### 8.2 Frontend Testing
- **Widget Tests:** Flutter widget testing
- **Integration Tests:** API integration testing
- **UI Tests:** Screen navigation and interactions

### 9. Deployment Considerations

#### 9.1 Development
- **Local Development:** Django development server
- **Database:** SQLite
- **Static Files:** Django's built-in server
- **Media Files:** Local storage

#### 9.2 Production (Future)
- **Database:** PostgreSQL
- **Static Files:** CDN/Cloud storage
- **Media Files:** Cloud storage (AWS S3)
- **Environment:** Production settings

### 10. Success Metrics

#### 10.1 Functional Requirements
- ✅ User can register and login
- ✅ JWT authentication works correctly
- ✅ CRUD operations for todos
- ✅ Profile management works
- ✅ API documentation is accessible
- ✅ Flutter app connects to API

#### 10.2 Performance Requirements
- **API Response Time:** < 500ms for CRUD operations
- **App Launch Time:** < 3 seconds
- **Image Upload:** < 5MB file size
- **Offline Handling:** Basic offline state management

### 11. Future Enhancements

#### 11.1 Potential Features
- **Todo Categories:** Organize todos by categories
- **Todo Sharing:** Share todos with other users
- **Push Notifications:** Due date reminders
- **Offline Sync:** Local storage with sync
- **Dark Mode:** Theme switching
- **Multi-language:** Internationalization

#### 11.2 Technical Improvements
- **Caching:** Redis for API caching
- **Background Tasks:** Celery for async operations
- **Real-time Updates:** WebSocket integration
- **Analytics:** User behavior tracking

---

**Next Steps:**
1. Review and approve this PRD
2. Create detailed implementation plan
3. Set up development environment
4. Begin backend development
5. Begin frontend development
6. Integration testing
7. Documentation completion 