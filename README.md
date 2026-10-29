# Lanterne

[![CI](https://github.com/remunox/lanterne/actions/workflows/ci.yml/badge.svg)](https://github.com/remunox/lanterne/actions/workflows/ci.yml)

A D&D table companion that gets first-time players playing in one evening — and keeps the DM's campaign straight afterwards.

> **Status:** early development. The foundation (M0) is in progress; none of the AI features below exist yet.

## Planned features

- **Rules lookup** — ask a rules question, get an answer with cited sections from the SRD.
- **Character creation** — describe a character concept in plain words and get a rules-valid character to review and edit.
- **"What can I do?"** — a player's realistic options on their turn, based on their character sheet.
- **Recaps & lore** — the DM's session notes turned into a recap plus tracked NPCs, places, factions and events.

Built on the [System Reference Document 5.2](https://www.dndbeyond.com/srd) (CC-BY-4.0).

## Stack

| Layer | Technology |
| --- | --- |
| Backend | Python, FastAPI, SQLAlchemy, Alembic |
| Database | PostgreSQL + pgvector |
| Frontend | React, TypeScript, Vite |
| LLM | Swappable providers: hosted API or local model (llama.cpp) |
| Tooling | uv, ruff, pytest, pnpm, Docker Compose, GitHub Actions |

## Repository layout

```
backend/   FastAPI app, migrations, tests
web/       React frontend
evals/     evaluation sets for the AI features
docker/    database init scripts
```

## Running locally

**Requirements:** Docker, [uv](https://docs.astral.sh/uv/), Node.js and [pnpm](https://pnpm.io/).

1. **Configure environment**

   ```bash
   cp .env.example .env
   ```

   Generate a JWT secret and put it in `JWT_SECRET`:

   ```bash
   python -c "import secrets; print(secrets.token_urlsafe(32))"
   ```

2. **Start the database**

   ```bash
   docker compose up -d
   ```

3. **Run the backend** (from `backend/`)

   ```bash
   uv sync
   uv run alembic upgrade head
   uv run fastapi dev src/lanterne/main.py
   ```

   API docs: <http://localhost:8000/docs>

4. **Run the frontend** (from `web/`)

   ```bash
   pnpm install
   pnpm dev
   ```

   App: <http://localhost:5173>

## Tests and linting

From `backend/`:

```bash
uv run pytest
uv run ruff check
uv run ruff format --check
```

## License

TBD
