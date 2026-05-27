from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class CoreSettings(BaseSettings):
    APP_NAME: str = "FastAPI education project"
    DEBUG: bool = False


class PostgresSettings(BaseSettings):
    PGHOST: str
    PGDATABASE: str
    PGUSER: str
    PGPASSWORD: str
    PGPORT: int = 5432

    # noinspection PyPep8Naming
    @property
    def DATABASE_ASYNC_URL(self) -> str:
        return (f"postgresql+asyncpg://{self.PGUSER}:{self.PGPASSWORD}@"
                f"{self.PGHOST}:{self.PGPORT}/{self.PGDATABASE}")


class Settings(CoreSettings, PostgresSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


@lru_cache()
def get_settings() -> Settings:
    # noinspection PyArgumentList
    return Settings()


settings = get_settings()
