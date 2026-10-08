# My App

A containerized full-stack starter with a static frontend, Python FastAPI API, and PostgreSQL database.

## Run locally

From this directory:

```sh
docker compose up --build
```

Open <http://localhost:3000> for the frontend and <http://localhost:8000/docs> for the API documentation. The API health endpoint is <http://localhost:8000/api/health>. PostgreSQL data persists in the `postgres_data` Docker volume.

Set `POSTGRES_USER`, `POSTGRES_PASSWORD`, `POSTGRES_DB`, and `JWT_SECRET` in your environment or a local `.env` file before deploying. The Compose defaults are for local development only.

## API

- `POST /api/auth/register` creates an account.
- `POST /api/auth/login` accepts OAuth2 form credentials and returns a bearer token.
- `POST /api/auth/login-json` accepts JSON credentials and returns a bearer token.
- `GET /api/users/` lists accounts for an authenticated user.
- `GET`, `PUT`, and `DELETE /api/users/{user_id}` manage the authenticated user's account.

The frontend is served by a small Node.js/Express container. Its static files are in `frontend/public`; the API source is in `backend/app`.

## CI

GitHub Actions compiles the Python source, installs frontend dependencies, validates the Compose file, and builds both application images on pushes and pull requests that touch `my_app`.
