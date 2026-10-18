# Resources and licenses

Verify exact package/model versions and license notices before distributing or publishing. Frontend versions are resolved in package-lock.json; Python bounded versions are in requirements*.txt. This register identifies intended resources, not university approval or a licensing audit.

| Resource | Purpose | Source / access |
|---|---|---|
| React, TypeScript, Vite, Tailwind | Web UI and build | react.dev, typescriptlang.org, vite.dev, tailwindcss.com; preserve package license notices |
| Lucide | UI SVG icons | lucide.dev; ISC license |
| Python, FastAPI, SQLAlchemy, Alembic | API/persistence/migrations | python.org, fastapi.tiangolo.com, sqlalchemy.org, alembic.sqlalchemy.org; review pinned package licenses |
| PostgreSQL, pgvector | Data/vector index | postgresql.org, github.com/pgvector/pgvector; PostgreSQL-style licenses |
| bcrypt, PyJWT, httpx | Password/token/HTTP handling | official package repositories; review installed distributions |
| sentence-transformers/all-MiniLM-L6-v2 | Local semantic retrieval | huggingface.co/sentence-transformers/all-MiniLM-L6-v2; model card lists Apache 2.0, verify downloaded revision |
| OpenAI API | Hosted structured service routing | platform.openai.com; account terms/paid usage, project key required |
| Public campus resource pages | Seed review candidates | Per-record source_url, primarily uta.edu; service descriptions here are brief draft summaries, not scraped pages |
| Playwright, axe-core, pytest, Vitest, k6, ZAP | Quality/test tooling | Official docs and package licenses; BrowserStack needs separate account |
| Docker/GitHub/Vercel/Render/Neon/Supabase | Packaging/source/hosting | Separate service terms, limits and budgets; no account entitlement included |

The application is an independent course project. No UTA logo asset, affiliation claim, SSO access or privileged university data is bundled. Backend environment files and third-party credentials are excluded from the source ZIP.
