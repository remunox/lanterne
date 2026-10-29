"""
App configuration, loaded from the root .env
"""

from pathlib import Path
from typing import Literal

from pydantic import SecretStr, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Lanterne"

    database_url: SecretStr
    test_database_url: SecretStr

    jwt_secret: SecretStr
    llm_provider: Literal["fake", "local", "api"] = "fake"

    model_config = SettingsConfigDict(
        env_file=Path(__file__).resolve().parents[3] / ".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

    @field_validator("jwt_secret")
    @classmethod
    def validate_jwt_secret(cls, value: SecretStr) -> SecretStr:
        secret = value.get_secret_value()
        if len(secret) < 32:
            raise ValueError("JWT_SECRET must be at least 32 characters; generate one with `secrets.token_urlsafe(32)`")
        return value


settings = Settings()  # pyright: ignore[reportCallIssue]
