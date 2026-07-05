from pydantic_settings import BaseSettings
from typing import List
import os

class Settings(BaseSettings):
    app_name: str = "Musabaqat"
    app_version: str = "0.1.0"
    debug: bool = os.getenv("DEBUG", "False") == "True"
    database_url: str = os.getenv("DATABASE_URL", "postgresql://user:password@db:5432/musabaqat")
    secret_key: str = os.getenv("SECRET_KEY", "dev-secret-key-change-in-production")
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    cors_origins: List[str] = ["http://localhost:3000", "http://localhost:8000", "http://127.0.0.1:3000"]
    audio_upload_dir: str = os.getenv("AUDIO_UPLOAD_DIR", "/app/audio_uploads")
    max_upload_size: int = 50 * 1024 * 1024
    jwt_secret: str = os.getenv("JWT_SECRET", "jwt-secret-key")
    redis_url: str = os.getenv("REDIS_URL", "redis://redis:6379/0")
    tajweed_model_path: str = os.getenv("TAJWEED_MODEL_PATH", "/app/models/tajweed_detector.pt")
    
    class Config:
        env_file = ".env"

settings = Settings()
