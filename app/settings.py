# -*- coding: utf-8 -*-

"""
This module contains application settings.
"""

import enum

from pathlib import Path
from tempfile import gettempdir
from typing import Optional

from loguru import logger
from pydantic_settings import BaseSettings, SettingsConfigDict
from yarl import URL

TEMP_DIR = Path(gettempdir())


class LogLevel(str, enum.Enum):  # noqa: WPS600
    """Possible log levels."""

    NOTSET = "NOTSET"
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    FATAL = "FATAL"


class Settings(BaseSettings):
    """
    Application settings.

    These parameters can be configured
    with environment variables.
    """

    # Current environment
    environment: str = "dev"
    log_level: LogLevel = LogLevel.DEBUG

    # Bot vars
    token: str = ""
    webhook_url: Optional[str] = None

    # Database vars
    db_host: str = "localhost"
    db_port: int = 5432
    db_user: str = "postgres"
    db_pass: str = "postgres"
    db_base: str = "schedule_bot"
    db_echo: bool = False

    model_config = SettingsConfigDict(
        env_file=Path(__file__).parent.parent / ".env",
        env_prefix="BOT_",
        env_file_encoding="utf-8",
    )

    @property
    def db_url(self) -> URL:
        """
        Assemble database URL from settings.

        :return: database URL.
        """
        return URL.build(
            scheme="postgres",
            host=self.db_host,
            port=self.db_port,
            user=self.db_user,
            password=self.db_pass,
            path=f"/{self.db_base}",
        )


settings = Settings()
logger.debug("Settings loaded!")
