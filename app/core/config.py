from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str = "whatsApp AI Customer Support Agent"
    APP_ENV: str = "development"
    DEBUG: bool = True
    DATABASE_URL: str
    OPEN_API_KEY: str = ""
    OPENAI_MODEL: str = "gpt-4.1-mini"
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )


settings = Settings()

