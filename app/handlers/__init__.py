# -*- coding: utf-8 -*-

"""This module registers handlers."""

from aiogram import Dispatcher
from loguru import logger

from app.handlers.base import setup_base
from app.handlers.errors import setup_errors


def register_handlers(dp: Dispatcher) -> None:
    """Register handlers."""

    logger.debug("Registering handlers...")

    setup_errors(dp)
    setup_base(dp)

    logger.debug("Handlers successfully registered!")