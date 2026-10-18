# MavAssist

A UTA student-services assistant built for **CSE 6324 — Team 3**. Find campus resources, ask questions, and get next steps with links to official sources.

## Features

- Campus directory with search and category filters.
- Chat with follow-up context, source citations, and suggested questions.
- Student accounts, saved resources, and recently viewed services.
- Admin tools for managing resources, notices, and usage analytics.

## Technology

React, TypeScript, Vite, Tailwind CSS, FastAPI, and SQLAlchemy. Local setup uses SQLite and source-based answers. PostgreSQL/pgvector and AI-generated answers are available through additional configuration.

## Run locally on Windows

Install **Python 3.12** and **Node.js 22.12+**. Open PowerShell in the project folder.

**1. Set up and start the backend:**

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r backend/requirements-dev.txt
.\.venv\Scripts\python.exe scripts/configure.py
cd backend
..\.venv\Scripts\python.exe -m alembic upgrade head
..\.venv\Scripts\python.exe -m app.manage seed
..\.venv\Scripts\python.exe -m uvicorn app.main:app --host 127.0.0.1 --port 8000 --no-access-log
```

**2. Open another PowerShell window in the project folder and start the frontend:**

```powershell
cd frontend
npm.cmd ci
npm.cmd run dev
```

**3. Open [MavAssist](http://localhost:5173) and create a student account.** Keep both terminals running: one serves the API and the other serves the website. API documentation is available at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

To create an administrator, run this from the `backend` folder in another terminal:

```powershell
..\.venv\Scripts\python.exe -m app.manage create-admin
```

The local setup works without an API key. It returns cited source summaries; AI-generated answers require a configured API key and model. Verify current campus details on the linked official pages.

## Documentation

- [Deployment instructions](DEPLOYMENT.md)
- [Chat and RAG setup](docs/RAG.md)
- [User guide](docs/USER_GUIDE.md)
- [Requirements](docs/REQUIREMENTS.md)
- [Test results](docs/VERIFICATION.md)

## Contributors

- Ashwinder Singh
- Krisha Patel
- Suhas Surendra Kumar
- Harmanpreet Kaur

Independent student project; not an official UTA service.
