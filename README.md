# MavAssist

Student-services assistant for CSE 6324, Team 3. React/TypeScript/Vite/Tailwind frontend, FastAPI/SQLAlchemy API, PostgreSQL 16/pgvector production database, BM25/MiniLM passage retrieval and optional OpenAI cited answer generation. Includes FR-01–FR-10 application paths, automated tests, Docker, CI, deployment configuration and a requirement-by-requirement checklist.

**Contextual chat:** [RAG setup, source import and upgrade](docs/RAG.md).

**Start here:** [Deployment instructions](DEPLOYMENT.md), [requirement coverage and limits](docs/REQUIREMENTS.md), [user guide](docs/USER_GUIDE.md), [verification results](docs/VERIFICATION.md).

## Quick start on Windows — no Docker or API key required

Install Python 3.12 and Node.js 22.12+. Extract the ZIP into a normal writable folder. Open PowerShell there:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r backend/requirements-dev.txt
.\.venv\Scripts\python.exe scripts/configure.py
cd backend
..\.venv\Scripts\python.exe -m alembic upgrade head
..\.venv\Scripts\python.exe -m app.manage seed
..\.venv\Scripts\python.exe -m app.manage create-admin
..\.venv\Scripts\python.exe -m uvicorn app.main:app --host 127.0.0.1 --port 8000 --no-access-log
```

Keep that window open. In another PowerShell window, from the extracted project folder:

```powershell
cd frontend
npm.cmd ci
npm.cmd run dev
```

Open **http://localhost:5173**. Create a student account, or sign in with the administrator credentials you entered. API documentation: **http://127.0.0.1:8000/docs**. No fixed demo password is shipped.

This quick start uses **SQLite + BM25 source retrieval and cited summaries**, explicitly labeled in the chatbot. It is useful for local functional demonstrations; it is **not** the PostgreSQL/semantic/hosted-AI deployment required by the proposal. Follow DEPLOYMENT.md for the full configuration.

## Layout

```text
backend/app/         API, models, authentication, recommendation, seed/maintenance commands
backend/migrations/ Initial Alembic schema + pgvector extension/index
backend/tests/       API acceptance, authorization, privacy and fallback checks
frontend/src/        Responsive student/admin interfaces and frontend unit checks
frontend/tests/      Browser workflows and axe accessibility checks
scripts/             Configuration, 100-question evaluation, k6 load scenario
docs/                Architecture, traceability, test/operations and team handoff
docker-compose.yml   Full local PostgreSQL/API/nginx deployment
render.yaml          Render API deployment blueprint
.github/workflows/   PostgreSQL/API, frontend, browser and evaluation CI
```

## Important scope details

* Fifty seed **office/service records** are included. They are review-required starter records, not independently verified university directory data. Location/hours/contact deliberately direct users to official pages instead of inventing details. Administrators must curate these fields and verify each source before an assessed or public release.
* Hosted RAG is implemented, but requires a real key, selected model, model download and PostgreSQL deployment. Offline keyword results are never presented as hosted AI results.
* The chat retrieves source passages and generates explanations/next steps with validated citations when a model is configured. Without a key it displays cited source summaries. Full details and corpus limits are in docs/RAG.md.
* NFR performance, independent AI accuracy, human SUS scores and live cloud availability cannot be claimed from a source bundle. Their scripts/protocols are included; see REQUIREMENTS.md.
* Nothing here changes the original WBS owners or schedule, and generated source is not evidence that a named team member completed their assigned work.
