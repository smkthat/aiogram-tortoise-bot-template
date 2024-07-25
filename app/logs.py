# -*- coding: utf-8 -*-

"""This module configures logging."""

import logging
import sys
from typing import Union

from loguru import logger

from app.settings import settings


class InterceptHandler(logging.Handler):
    """Default handler from examples in loguru documentation.

    This handler intercepts all log requests and
    passes them to loguru.

    For more info see:
    https://loguru.readthedocs.io/en/stable/overview.html#entirely-compatible-with-standard-logging
    """

    def emit(self, record: logging.LogRecord) -> None:  # pragma: no cover
        """Propagates logs to loguru.

        :param record: record to log.
        """
        try:
            level: Union[str, int] = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno

        # Find caller from where originated the logged message
        frame, depth = logging.currentframe(), 2
        while frame.f_code.co_filename == logging.__file__:
            frame = frame.f_back  # type: ignore
            depth += 1

        logger.opt(depth=depth, exception=record.exc_info).log(
            level,
            record.getMessage(),
        )


def setup_logging() -> None:  # pragma: no cover
    """Setup logging."""
    logger.debug("Configuring logging...")

    intercept_handler = InterceptHandler()
    logging.basicConfig(handlers=[intercept_handler], level=logging.INFO)

    logging.getLogger("aiogram").setLevel(logging.DEBUG)
    logging.getLogger("aiogram").handlers = []
    logging.getLogger("asyncio").setLevel(logging.DEBUG)
    logging.getLogger("asyncio").handlers = []

    # set logs output, level and format
    logger.remove()
    logger.add(
        sys.stdout,
        level=settings.log_level.value,
    )

    logger.debug("Logging configured!")
