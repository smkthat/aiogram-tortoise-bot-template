# -*- coding: utf-8 -*-

"""
This module contains models for user.
"""

from tortoise import fields, models


class UserModel(models.Model):
    """Model for tasks."""

    id = fields.IntField(pk=True)
    first_name = fields.CharField(max_length=30)
    last_name = fields.CharField(max_length=30)
    username = fields.CharField(max_length=30)
    is_blocked: bool = False
    is_banned: bool = False

    # pylint: disable=too-few-public-methods
    class Meta:
        """Meta settings class."""

        table = "users"

    def __str__(self) -> str:
        return (
            "{class_name}("  # pylint: disable=consider-using-f-string
            "id={id}, "
            "username={username}, "
            "first_name={first_name}, "
            "last_name={last_name})"
        ).format(
            class_name=self.__class__.__name__,
            id=self.id,
            username=self.username,
            first_name=self.first_name,
            last_name=self.last_name,
        )
