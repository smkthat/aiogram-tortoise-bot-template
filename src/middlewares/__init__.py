# -*- coding: utf-8 -*-

"""This module register middlewares."""

from aiogram import Dispatcher
from loguru import logger

from src.middlewares.user_middleware import UserMiddleware


def setup_middlewares(dp: Dispatcher) -> None:
    """Setup middlewares."""
    logger.debug("Setup middlewares...")

    dp.message.middleware.register(UserMiddleware())
    dp.callback_query.middleware.register(UserMiddleware())

    logger.debug("All middlewares setup!")
