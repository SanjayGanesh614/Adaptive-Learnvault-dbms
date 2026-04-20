from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    PROJECT_NAME: str = "Adaptive LearnVault API"
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    GEMINI_API_KEY: Optional[str] = None
    MONGODB_URL: str
    DATABASE_NAME: str
    YOUTUBE_API_KEY: Optional[str] = None
    NVIDIA_API_KEY: Optional[str] = None

    model_config = {
        "env_file": ".env",
        "extra": "ignore"
    }

settings = Settings()
