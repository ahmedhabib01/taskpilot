# 🧭 TaskPilot — FastAPI Backend + Simple Frontend  
A production-ready CRUD API built with **FastAPI**, **PostgreSQL**, **Docker**, **JWT auth**, and **GitHub Actions CI**.  
This project showcases backend architecture, DevOps practices, and clean code structure suitable for job portfolios.

---

## 🚀 Status & Badges

![API Status](https://img.shields.io/badge/API-Running-brightgreen)
![CI](https://github.com/ahmedhabib01/taskpilot/actions/workflows/ci.yml/badge.svg)
![Docker](https://img.shields.io/badge/Docker-Build-blue)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

# 📌 Short Description (for GitHub Page / Repo Header)

TaskPilot is a fully-containerized CRUD backend API built using FastAPI and PostgreSQL, featuring JWT authentication, Docker Compose, and GitHub Actions CI. Includes a lightweight HTML/JS frontend for quick testing. Ideal as a modern backend portfolio project.

---

# 📘 Full Project Overview

## 🔥 What This Project Demonstrates

- Modern Python backend using **FastAPI**
- **Clean architecture** — routers, schemas, models, services (CRUD)
- **PostgreSQL** database + **SQLAlchemy ORM**
- **JWT-based Authentication** (register/login)
- **Docker & Docker Compose** for reproducible environment
- **GitHub Actions CI/CD** (tests + lint)
- **Simple frontend** consuming the API
- **Beginners-friendly structure**, but professional quality

---

# 🧱 Tech Stack

| Layer | Tools |
|-------|--------|
| **Backend** | FastAPI, Python, SQLAlchemy |
| **Database** | PostgreSQL |
| **Auth** | JWT (PyJWT) |
| **Frontend** | Vanilla HTML + JS |
| **DevOps** | Docker, Docker Compose, GitHub Actions |
| **Testing** | pytest |

---
## Folder Structure

```text
taskpilot/
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── models.py
│   │   ├── schemas.py
│   │   ├── database.py
│   │   ├── crud.py
│   │   ├── auth.py
│   │   ├── deps.py
│   │   └── routers/
│   │       └── users.py
│   ├── tasks.py
│   └── tests/
│       └── test_basic.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── frontend/
│   └── simple-ui/
│       ├── index.html
│       └── main.js
├── .gitignore
├── .dockerignore
├── commit-message-template.txt
└── README.md
```
