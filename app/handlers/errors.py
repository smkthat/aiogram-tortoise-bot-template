# -*- coding: utf-8 -*-

"""
This module contains handlers for errors.
"""

from aiogram import Dispatcher, types
from loguru import logger


async def errors_handler(update: types.Update, exception: Exception) -> bool:
    """Base errors handler."""

    logger.exception(
        "Cause exception {e} in update {update}",
        e=exception,
        update=update,
    )

    return True


def setup_errors(dp: Dispatcher) -> None:
    """Register errors handlers."""

    dp.error.register(errors_handler)
    logger.debug("Errors handlers registered")
