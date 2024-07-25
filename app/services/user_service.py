# -*- coding: utf-8 -*-

"""This module provides user service."""

from typing import Any

from loguru import logger

from app.db.models.user_model import UserModel
from app.schemas.user_scheme import CreateUserSchema, UserSchema


class UserService:  # pylint: disable=too-few-public-methods
    """Class representing a user service.

    This class provides methods to interact with user data in the application database.
    It includes methods for getting or creating a user, as well
    as updating user information.

    Attributes:
        None

    Methods:
        get_or_create: Method to get an existing user or create a new user based
            on the provided data.
        update: Method to update the information of an existing user.

    Note:
        This class is designed to handle user-related operations in the application.
    """

    @classmethod
    async def get_or_create(
        cls,
        **user_data: dict[str, Any],
    ) -> tuple[UserSchema, bool]:
        """Method to get an existing user or create a new user based on the provided data.

        Args:
            **user_data (dict[str, Any]): Keyword arguments representing user data.

        Returns:
            tuple[UserSchema, bool]: A tuple containing the UserSchema object representing the user
            and a boolean indicating whether the user was created (True) or retrieved (False).

        Note:
            This method logs the user data, creates a CreateUserSchema instance,
            and then calls the UserModel's get_or_create method to interact with the database.
            It returns a UserSchema object created from the database user and a flag indicating
            if the user was newly created or not.
        """
        logger.debug("Get or create user {}", user_data)
        crete_user_schema = CreateUserSchema(**user_data)
        db_user, is_created = await UserModel.get_or_create(
            **crete_user_schema.model_dump(),
        )
        return await UserSchema.from_tortoise_orm(db_user), is_created

    @classmethod
    async def update(cls, user: UserSchema) -> None:
        """Method to update the information of an existing user.

        Args:
            user (UserSchema): The user object containing the updated information.

        Returns:
            None

        Raises:
            None
        """
        logger.debug("Update user {}", user)
        db_user = await UserModel.get(id=user.id)

        for attr in user.model_fields:
            setattr(db_user, attr, getattr(user, attr))

        await db_user.save()
