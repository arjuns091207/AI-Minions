from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str = "AI Minions"
    APP_VERSION: str = "0.1.0"
    APP_ENV: str = "development"

    OLLAMA_BASE_URL: str = "http://localhost:11434"
    OLLAMA_MODEL: str = "qwen3.5:4b"

    MAX_AGENT_ITERATIONS: int = 5
    MAX_TOOL_CALLS_PER_TASK: int = 10
    TASK_TIMEOUT_SECONDS: int = 120

    WORKSPACE_ROOT: str = "projects"

    REQUIRE_APPROVAL_FOR_DESTRUCTIVE_ACTIONS: bool = True
    ENABLE_AUDIT_LOGGING: bool = True

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Settings()

APP_NAME = settings.APP_NAME
APP_VERSION = settings.APP_VERSION
APP_ENV = settings.APP_ENV

OLLAMA_BASE_URL = settings.OLLAMA_BASE_URL
OLLAMA_MODEL = settings.OLLAMA_MODEL

MAX_AGENT_ITERATIONS = settings.MAX_AGENT_ITERATIONS
MAX_TOOL_CALLS_PER_TASK = settings.MAX_TOOL_CALLS_PER_TASK
TASK_TIMEOUT_SECONDS = settings.TASK_TIMEOUT_SECONDS

WORKSPACE_ROOT = settings.WORKSPACE_ROOT

REQUIRE_APPROVAL_FOR_DESTRUCTIVE_ACTIONS = (
    settings.REQUIRE_APPROVAL_FOR_DESTRUCTIVE_ACTIONS
)
ENABLE_AUDIT_LOGGING = settings.ENABLE_AUDIT_LOGGING