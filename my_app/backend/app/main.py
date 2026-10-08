from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from datetime import datetime, timezone

from fastapi import FastAPI

from .config import get_settings
from .database import Base, engine
from .routers import users

settings = get_settings()

tags_metadata = [
    {
        "name": "auth",
        "description": "Authentication endpoints (register & login)",
    },
    {
        "name": "users",
        "description": "User management endpoints",
    },
]


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    await engine.dispose()


app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    debug=settings.debug,
    lifespan=lifespan,
    openapi_tags=tags_metadata,
)

app.include_router(users.router)


@app.get("/api/health", tags=["health"])
async def health() -> dict:
    return {
        "status": "ok",
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }