import os

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")

class Config:
    DATABASE_URL = DATABASE_URL
    API_V1_STR = "/api/v1"
    PROJECT_NAME = "Simple FastAPI API"
    VERSION = "0.1.0"