# Library Management System

This is a full-stack Library Management System built with Django (backend) and Vue.js (frontend). The application allows users to manage books, borrow and return books, and includes authentication with role-based access control.

## Features

- **User Roles**: Librarian and Member
  - **Librarian**: Can add, update, and delete books, view borrowed books history.
  - **Member**: Can browse books, borrow, and return books.
- **Authentication**: Register, login, and logout with JWT authentication.
- **Django REST API**: Backend is built using Django REST Framework.
- **Vue.js Frontend**: Modern frontend using Vue 3 and Vite.
- **PostgreSQL Database**: Data persistence using PostgreSQL.
- **Dockerized**: Runs in Docker containers for easy deployment.

## Tech Stack

- **Backend**: Django, Django REST Framework, PostgreSQL
- **Frontend**: Vue.js 3, Vite, Tailwind CSS
- **Containerization**: Docker, Docker Compose

## Installation & Setup

### Prerequisites

- Docker & Docker Compose installed

### Run the Application

1. Clone the repository:

   ```sh
   git clone https://github.com/your-repo/library-management.git
   cd library-management
   ```

2. Create a `.env` file for the backend (same level as `manage.py`):

   ```env
   DEBUG=False
   SECRET_KEY=your_secret_key
   DATABASE_NAME=library
   DATABASE_USER=postgresUser
   DATABASE_PASSWORD=postgressPassword
   DATABASE_HOST=db
   DATABASE_PORT=5432
   ```

3. Build and run the containers:

   ```sh
   docker-compose up --build -d
   ```

4. Run database migrations:

   ```sh
   docker exec -it django_backend python manage.py migrate
   ```

5. Collect static files:

   ```sh
   docker exec -it django_backend python manage.py collectstatic --noinput
   ```

6. Create a superuser:

   ```sh
   docker exec -it django_backend python manage.py createsuperuser
   ```

7. Access the application:

   - **Backend API**: `http://localhost:8000/api/`
   - **Frontend**: `http://localhost:5173/`

## Project Structure

```
library/
│── apps/
│   ├── users/
│   ├── books/
│   ├── dashboard/
│── config/
│── manage.py
│── Dockerfile
│── .env
│── frontend/
│   ├── src/
│   ├── public/
│   ├── Dockerfile
│── docker-compose.yml
│── README.md
```

## API Endpoints

#### OAuth
- `POST /api/auth/register/` – Register a new user 
- `POST /api/auth/login/` – Login and obtain JWT

#### Books
- `GET /api/books/` – List books
- `GET /books/history/` – Books history (Librarian only)
- `POST /api/books/` – Add a new book (Librarian only)
- `PUT /api/books/:id/` – Update book (Librarian only)
- `DELETE /api/books/:id/` – Delete book (Librarian only)
- `POST /api/books/:id/borrow/` – Borrow a book (Member only)
- `POST /api/books/:id/return/` – Return a book (Member only)

