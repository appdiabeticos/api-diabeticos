from pydantic_settings import BaseSettings
from dotenv import load_dotenv
from pathlib import Path


env_path = Path(__file__).resolve().parent.parent.parent / '.env'
load_dotenv(dotenv_path=env_path)


class Settings(BaseSettings):
    version: str
    host: str
    fastapi_port: int
    mongo_database: str
    mongo_url: str
    debug: bool
    reload: bool
    log_level: str
    api_maps: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int

    class Config:
        env_file = str(env_path)
        env_file_encoding = "utf-8"


settings = Settings()
