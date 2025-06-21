from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

from core.config.types import Environment


class DBSettings(BaseSettings):
    """ Класс для настройки параметров подключения к базе данных. """
    db_name: str
    db_user: str
    db_password: SecretStr
    db_host: str
    db_port: int
    db_echo: bool

    model_config = SettingsConfigDict(env_prefix='DB_', extra="ignore")

    @property
    def db_url(self):
        """
        Свойство, возвращающее строку подключения к базе данных PostgreSQL.
        """
        return f"postgresql+asyncpg://{self.db_user}:{self.db_password.get_secret_value()}@{self.db_host}:{self.db_port}/{self.db_name}"


class EmailSettings(BaseSettings):
    """ Настройки для электронной почты. """

    email_host: str
    email_port: int
    email_username: str
    email_password: SecretStr

    model_config = SettingsConfigDict(env_prefix="EMAIL_", extra="ignore")


class RedisSettings(BaseSettings):
    """ Класс для настройки соединения с Redis. """

    redis_host: str
    redis_port: int
    redis_db: int

    model_config = SettingsConfigDict(env_prefix="REDIS_", extra="ignore")

    @property
    def redis_url(self) -> str:
        """ Получает URL для подключения к Redis. """
        return f"redis://{self.redis_host}:{self.redis_port}/{self.redis_db}"


class AppSettings(BaseSettings):
    env: Environment = "local"
    secret_key: SecretStr
    templates_dir: str = "templates"
    frontend_url: str
    access_token_expire: int = 3600
    log_level: str = "INFO"

    model_config = SettingsConfigDict(env_prefix="", extra="ignore")


class Settings:
    def __init__(self):
        self.db = DBSettings()
        self.redis = RedisSettings()
        self.email = EmailSettings()
        self.app = AppSettings()


settings = Settings()
