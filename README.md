# Task Manager API

<<<<<<< HEAD
Task Manager API is a backend application built with FastAPI for managing users, projects, and tasks.

This project demonstrates Python backend development skills:
- FastAPI
- PostgreSQL
- SQLAlchemy 2.0
- Alembic
- JWT authentication
- Docker / Docker Compose
- Pytest

---

## Features

- user registration
- JWT login
- current user retrieval
- project creation
- listing personal projects
- updating and deleting projects
- task creation inside a project
- listing project tasks
- task filtering by status, creator, and assignee
- basic access control
- database migrations with Alembic
- tests for auth, projects, and tasks

---

## Tech Stack

- Python 3.11
- FastAPI
- SQLAlchemy 2.0
- PostgreSQL 16
- Alembic
- asyncpg
- python-jose
- passlib
- Docker
- Pytest
- httpx

---

## Project Structure

```text
task-manager-api/
├── app/
│   ├── api/
│   │   └── v1/
│   │       ├── auth.py
│   │       ├── users.py
│   │       ├── projects.py
│   │       └── tasks.py
│   ├── core/
│   │   ├── config.py
│   │   └── security.py
│   ├── db/
│   │   ├── base.py
│   │   └── session.py
│   ├── models/
│   │   ├── user.py
│   │   ├── project.py
│   │   └── task.py
│   ├── schemas/
│   │   ├── user.py
│   │   ├── project.py
│   │   └── task.py
│   ├── crud/
│   │   ├── project.py
│   │   └── task.py
│   ├── deps.py
│   └── main.py
├── alembic/
├── tests/
├── .env.example
├── .gitignore
├── docker-compose.yml
├── Dockerfile
├── pyproject.toml
└── README.md
=======
Backend API for managing tasks with authentication and filtering.

## Tech Stack

* Python
* Django
* Django REST Framework
* PostgreSQL
* Docker
* JWT (SimpleJWT)
* drf-spectacular (Swagger)

## Features

* User registration
* JWT authentication
* CRUD for tasks
* Filtering tasks by status
* Search tasks
* Ordering tasks
* Pagination
* API documentation (Swagger)
* Automated tests

## Project Structure

```
task_manager/
├── apps/
│   ├── users/
│   └── tasks/
├── api/
├── core/
├── docker/
├── tests/
├── docker-compose.yml
├── requirements.txt
└── manage.py
```

## Run with Docker

```bash
docker compose up --build
```

## Apply migrations

```bash
docker compose exec web python manage.py migrate
```

## Run tests

```bash
docker compose exec web python manage.py test
```

## API Documentation

Swagger UI:

```
http://127.0.0.1:8000/api/docs/
```

## Main Endpoints

Register user

```
POST /api/users/register/
```

Login

```
POST /api/login/
```

Tasks

```
GET /api/tasks/
POST /api/tasks/
PATCH /api/tasks/{id}/
DELETE /api/tasks/{id}/
```
>>>>>>> 629efeffa29c35f9031cbd938acaa1a22a29f7a0
