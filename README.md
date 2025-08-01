# 📝 Task Tracker Backend

This is the backend for a Task Tracker application built with **Django** and **Django REST Framework**. It supports user authentication via **Google Sign-In only** (no traditional email/password), and allows authenticated users to perform CRUD operations on their personal tasks.

## 🚀 Features

- ✅ Google OAuth2 login (no traditional login)
- ✅ CRUD operations on tasks
- ✅ User-specific data (each user only sees their own tasks)
- ✅ Auth-required API endpoints
- ✅ Session-based authentication for browser access
- ✅ Ready for frontend integration via Django Templates

## 🔧 Tech Stack

- Python 3.11+
- Django 4+
- Django REST Framework
- django-allauth (for Google Sign-In)
- SQLite (can be switched to PostgreSQL)

## 🔐 Google Sign-In

Users can only authenticate via **Google OAuth2**. After logging in, users are redirected to the task list page. Logout is also supported.

## 📦 API Endpoints

All endpoints require authentication.

| Method | Endpoint            | Description              |
|--------|---------------------|--------------------------|
| GET    | `/api/tasks/`       | List all user tasks      |
| POST   | `/api/tasks/`       | Create a new task        |
| GET    | `/api/tasks/<id>/`  | Retrieve task details    |
| PUT    | `/api/tasks/<id>/`  | Update an existing task  |
| DELETE | `/api/tasks/<id>/`  | Delete a task            |

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Jibinbiju-22/task-tracker-backend.git
cd task-tracker-backend
