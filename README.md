# Task Manager API

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