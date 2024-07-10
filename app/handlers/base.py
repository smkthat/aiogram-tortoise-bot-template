# -*- coding: utf-8 -*-

"""
This module contains handlers for base commands.
"""

from aiogram import Dispatcher, types
from aiogram.filters.command import CommandStart
from loguru import logger

from app.schemas.user_scheme import UserSchema


async def cmd_start(message: types.Message, user: UserSchema) -> None:
    """Start command handler."""

    logger.info("User {user} start conversation with bot", user=user.id)
    await message.answer(
        text=f"Hello, {user.mention_html()}",
    )


def setup_base(dp: Dispatcher) -> None:
    """Register base handlers."""

    dp.message.register(cmd_start, CommandStart())
    logger.debug("Base handlers registered")
