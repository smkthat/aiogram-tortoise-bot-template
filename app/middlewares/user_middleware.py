# -*- coding: utf-8 -*-

"""
This module contains user middleware.
"""

from typing import Any, Awaitable, Callable, Optional

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject
from aiogram.types import User as TelegramUser

from app.services.user_service import UserService


class UserMiddleware(BaseMiddleware):  # pylint: disable=too-few-public-methods
    """User middleware."""

    async def __call__(
        self,
        handler: Callable[[TelegramObject, dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: dict[str, Any],
    ) -> Any:
        tg_user: Optional[TelegramUser] = getattr(event, "from_user", None)
        if tg_user:
            db_user, _ = await UserService.get_or_create(
                **tg_user.dict(),
            )
            data["user"] = db_user

        result = await handler(event, data)

        if updated_user := data.get("user"):
            await UserService.update(user=updated_user)

        return result
