# -*- coding: utf-8 -*-
# mypy: ignore-errors

"""This module contains user schemas."""

from typing import Type

from aiogram.utils import markdown
from aiogram.utils.link import create_tg_link
from pydantic import ConfigDict
from tortoise.contrib.pydantic import PydanticModel, pydantic_model_creator

from app.db.models.user_model import UserModel

__all__ = [
    "UserSchema",
    "CreateUserSchema",
]

UserSchemaType: Type[PydanticModel] = pydantic_model_creator(
    UserModel,
    name="User",
)
CreateUserSchemaType: Type[PydanticModel] = pydantic_model_creator(
    UserModel,
    name="CreateUser",
    exclude=("created_at", "updated_at"),
)


class UserSchema(UserSchemaType):
    """UserSchema class to represent the schema for a user.

    This class inherits from PydanticModel and provides a property `get_full_name`
    to retrieve the full name of the user by concatenating the first name and last name.

    Attributes:
        Inherits all attributes from PydanticModel.

    Properties:
        `get_full_name`: A property that returns the full name of the user
            by concatenating the first name and last name.
        `model_config`: ConfigDict
            Configuration for the Pydantic model.

    Note:
        This class is used to define the schema for a user in the application.

    """

    model_config = ConfigDict(extra="ignore")

    @property
    def full_name(self) -> str:
        """A property that returns the full name of the user."""
        return f"{self.first_name} {self.last_name}".strip()

    @property
    def url(self) -> str:
        """A property that returns the URL of the user."""
        return create_tg_link("user", id=self.id)

    def mention_html(self) -> str:
        """A property that returns the HTML formatted mention of the user."""
        name = f"@{self.username}" if self.username is not None else self.full_name
        return markdown.hlink(name, self.url)


class CreateUserSchema(CreateUserSchemaType):
    """CreateUserSchema class to represent the schema for creating a new user.

    This class inherits from PydanticModel and is used to define the schema
    for creating a new user in the application.

    Attributes:
        Inherits all attributes from CreateUserSchemaType.

        `model_config`: ConfigDict
            Configuration for the Pydantic model.

    Note:
        This class is specifically tailored for creating a new user and excludes
        the 'created_at' and 'updated_at' fields.

    """

    model_config = ConfigDict(extra="ignore")
