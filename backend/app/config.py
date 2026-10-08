from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    app_name: str = "SharpFront API"
    app_version: str = "1.0.0"
    debug: bool = Field(default=False)

    database_url: str = Field(
        default="postgresql+asyncpg://sharpfront:sharpfront@localhost:5432/sharpfront"
    )
    jwt_secret: str = Field(default="change-me-in-production")
    jwt_algorithm: str = Field(default="HS256")
    access_token_expire_minutes: int = Field(default=30)


@lru_cache
def get_settings() -> Settings:
    return Settings()