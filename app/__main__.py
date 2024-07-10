# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This module is the starting point of the application.
"""

import asyncio

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage, SimpleEventIsolation
from aiogram.fsm.strategy import FSMStrategy
from loguru import logger

from app.db.engine import database_close, database_init
from app.handlers import register_handlers
from app.logs import setup_logging
from app.middlewares import setup_middlewares
from app.settings import settings


def create_bot(token: str) -> Bot:
    """Create bot instance."""

    logger.debug("Creating bot")
    return Bot(
        token=token,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )


def run_polling(dp: Dispatcher, bot: Bot) -> None:
    """Start polling."""

    try:
        dp.run_polling(bot)
    finally:
        logger.info("Stopped")


def main() -> None:
    """Start application."""

    setup_logging()

    asyncio.run(database_init())

    dp = Dispatcher(
        storage=MemoryStorage(),
        fsm_strategy=FSMStrategy.CHAT,
        events_isolation=SimpleEventIsolation(),
    )

    dp.startup.register(database_init)
    dp.shutdown.register(database_close)

    setup_middlewares(dp)
    register_handlers(dp)

    bot = create_bot(settings.token)
    run_polling(dp, bot)


if __name__ == "__main__":
    logger.debug("Start application...")
    main()
