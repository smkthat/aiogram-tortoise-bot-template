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
    token: str = ""
    webhook_url: Optional[URL] = None

    model_config = SettingsConfigDict(
        env_file=Path(__file__).parent.parent / ".env",
        env_prefix="BOT_",
        env_file_encoding="utf-8",
    )


settings = Settings()
logger.debug("Settings loaded")
