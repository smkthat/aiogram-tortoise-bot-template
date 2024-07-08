# -*- coding: utf-8 -*-

"""
This module contains handlers for base commands.
"""

from aiogram import Dispatcher, types
from aiogram.filters.command import CommandStart
from loguru import logger


async def cmd_start(message: types.Message) -> None:
    """Start command handler."""

    if user := message.from_user:
        logger.info("User {user} start conversation with bot", user=user.id)
        await message.answer(
            text=f"Hello, {user.mention_html()}",
        )
    else:
        raise RuntimeError("User not found")


def setup_base(dp: Dispatcher) -> None:
    """Register base handlers."""

    dp.message.register(cmd_start, CommandStart())
    logger.debug("Base handlers registered")
