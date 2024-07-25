# -*- coding: utf-8 -*-

"""This module contains handlers for errors."""

from aiogram import Dispatcher, types
from loguru import logger


async def error_handler(error_event: types.ErrorEvent) -> bool:
    """Base errors handler."""
    logger.exception(
        "Cause exception {e} in update {event}",
        e=error_event.exception,
        event=error_event,
    )

    return True


def setup_errors(dp: Dispatcher) -> None:
    """Register errors handlers."""
    dp.error.register(error_handler)
    logger.debug("Errors handlers registered")
