from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    GROQ_API_KEY: str
    MODEL_NAME: str = "llama-3.1-8b-instant"
    BASE_URL: str = "https://api.groq.com/openai/v1"

    class Config:
        env_file = ".env"

settings = Settings()