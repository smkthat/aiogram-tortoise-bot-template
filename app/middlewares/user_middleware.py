# -*- coding: utf-8 -*-

"""This module contains user middleware."""

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
        """Handle user-related operations in the middleware.

        This method checks if a Telegram user exists in the event data,
        gets or creates the corresponding
        user in the database using the UserService,
        updates the user if needed, and then calls the handler
        with the event and data.
        Returns the result of the handler.

        Args:
            handler (Callable): The handler function to call.
            event (TelegramObject): The Telegram event object.
            data (dict[str, Any]): Additional data related to the event.

        Returns:
            Any: The result of calling the handler function.

        Note:
            If a Telegram user exists,
            it is associated with the event data under the key 'user'.
            The user is updated in the database
            if any changes are made during the handler execution.
        """
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
