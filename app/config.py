from pydantic import BaseSettings


class Settings(BaseSettings):
    database_username: str
    database_password: str
    database_hostname: str
    database_port: int
    database_name: str

    class Config:
        env_file = "C:\\Users\\willm\\Desktop\\NotesApi\\.env"


settings = Settings()
