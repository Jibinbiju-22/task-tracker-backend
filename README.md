# 📝 Task Tracker Backend

This is the backend for a Task Tracker application built with **Django** and **Django REST Framework**.  
It supports user authentication via **Google Sign-In only** (no traditional email/password), and allows authenticated users to perform CRUD operations on their personal tasks.

## 🚀 Features

- Google OAuth2 login (no traditional login)  
- CRUD operations on tasks  
- User-specific data (each user only sees their own tasks)  
- Auth-required API endpoints  
- Session-based authentication for browser access  
- Ready for frontend integration via Django Templates  

## 🔧 Tech Stack

- Python 3.11+  
- Django 4+  
- Django REST Framework  
- django-allauth (Google Sign-In)  
- SQLite (can be switched to PostgreSQL)  

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

1. **Clone the repository**

```bash
git clone https://github.com/Jibinbiju-22/task-tracker-backend.git
cd task-tracker-backend
```

2. **Create a virtual environment**

```bash
python -m venv venv
```

Activate the environment:

- On **Windows**:

  ```bash
  venv\Scripts\activate
  ```

- On **macOS/Linux**:

  ```bash
  source venv/bin/activate
  ```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Set up Google OAuth**

- Go to [Google Cloud Console](https://console.cloud.google.com/)
- Create a new project
- Set up OAuth 2.0 credentials
- Add the following redirect URI:

  ```
  http://localhost:8000/accounts/google/login/callback/
  ```

- Add your client ID and secret to Django settings:

```python
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'APP': {
            'client_id': 'YOUR_GOOGLE_CLIENT_ID',
            'secret': 'YOUR_GOOGLE_CLIENT_SECRET',
            'key': ''
        }
    }
}
```

5. **Apply migrations**

```bash
python manage.py migrate
```

6. **Run the development server**

```bash
python manage.py runserver
```

7. **Log in using Google**

Open your browser and go to:

```
http://localhost:8000/accounts/google/login/
```

## ✍️ Author

**Jibin Biju**  
GitHub: [@Jibinbiju-22](https://github.com/Jibinbiju-22)
