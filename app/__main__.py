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
from tortoise import Tortoise

from app.db.config import TORTOISE_CONFIG
from app.handlers import register_handlers
from app.logs import setup_logging
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


async def database_init() -> None:
    """Init database."""

    await Tortoise.init(
        TORTOISE_CONFIG,
    )
    await Tortoise.generate_schemas()
    logger.debug("Tortoise inited!")


async def on_startup() -> None:
    """On start handler."""

    await database_init()
    logger.info("Application started")


def main() -> None:
    """Start application."""

    setup_logging()

    asyncio.run(database_init())

    dp = Dispatcher(
        storage=MemoryStorage(),
        fsm_strategy=FSMStrategy.CHAT,
        events_isolation=SimpleEventIsolation(),
        on_startup=on_startup,
    )

    register_handlers(dp)

    logger.debug("Start application")

    bot = create_bot(settings.token)
    run_polling(dp, bot)


if __name__ == "__main__":
    main()
