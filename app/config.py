from pydantic import BaseSettings
from pathlib import Path


class Settings(BaseSettings):
    database_username: str
    database_password: str
    database_hostname: str
    database_port: int
    database_name: str

    class Config:
        env_file = "/usr/src/app/.env"


settings = Settings()
