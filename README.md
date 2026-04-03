# FoodCorp

FoodCorp is a full-stack web application designed to help users manage their personalized food collections and keep track of their favorite foods. It features a robust Django REST API backend coupled with a modern, fast React frontend built with Vite.

## 🚀 Features

- **User Authentication**: Secure login and registration using JWT (JSON Web Tokens).
- **Protected Routes**: Frontend routing secured based on authentication state.
- **Personalized Food Profile**: A dedicated space for users to manage their food collections.
- **Favorites Management**: Easily add, view, and manage your favorite foods list.
- **Admin Dashboard**: Built-in Django admin interface for easy data management.

## 🛠️ Tech Stack

### Frontend
- **Framework**: React 19
- **Build Tool**: Vite
- **Routing**: React Router DOM v7
- **HTTP/API**: Axios
- **Authentication**: JWT-Decode

### Backend
- **Framework**: Django 4.2
- **API**: Django REST Framework (DRF)
- **Authentication**: djangorestframework-simplejwt (JWT)
- **Database**: PostgreSQL / SQLite (via psycopg2-binary)
- **Server**: Gunicorn (for deployment)

## 📋 Prerequisites

Before you begin, ensure you have met the following requirements:
- **Node.js** (v18 or higher) and **npm**
- **Python** (v3.8 or higher)
- **pip** (Python package manager)

## ⚙️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/foodCorp.git
cd foodCorp
```

### 2. Backend Setup
Navigate into the backend directory and set up the Python environment:

```bash
cd backend

# Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Install dependencies
pip install -r requirements.txt

# Run database migrations
python manage.py makemigrations
python manage.py migrate

# Create a superuser (optional)
# python manage.py createsuperuser

# Start the Django development server
python manage.py runserver
```

### 3. Frontend Setup
Open a new terminal, navigate to the frontend directory, and set up the React app:

```bash
cd frontend

# Install dependencies
npm install

# Create a .env file and set your Django API URL
# Example: VITE_API_URL=http://127.0.0.1:8000
echo "VITE_API_URL=http://127.0.0.1:8000" > .env

# Start the Vite development server
npm run dev
```

## 🗺️ Application Routes

**Frontend:**
- `/` - Home
- `/login` - User Login
- `/register` - User Registration
- `/profile` - User Profile (Protected)

**Backend API:**
- `/admin/` - Django Admin Panel
- `/api/token/` - Get JWT Access & Refresh Tokens
- `/api/token/refresh/` - Refresh JWT Token
- `/food/` - Base Food API
- `/profile/favourites/` - User's Favorites List
- `/fav/<id>/` - Add/Remove specific favorite

## 🚀 Deployment

This project includes a `Procfile` pre-configured to run the WSGI application with Gunicorn, making it ready for deployment to platforms like Heroku, Render, or any standard Linux server.

Remember to update your CORS settings and `ALLOWED_HOSTS` in Django's `settings.py` before deploying to production.

## 🤝 Contributing
Contributions, issues, and feature requests are welcome!

---
*Built by AlisherOP*
