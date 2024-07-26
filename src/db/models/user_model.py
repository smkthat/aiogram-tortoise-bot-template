# -*- coding: utf-8 -*-

"""This module contains models for user."""

from tortoise import fields, models

from src.db.model_mixins.datetime_model_mixin import DateTimeModelMixin


class UserModel(
    models.Model,
    DateTimeModelMixin,
):  # pylint: disable=too-few-public-methods
    """Model for bot users."""

    id = fields.IntField(pk=True)
    first_name = fields.CharField(max_length=30, null=True)
    last_name = fields.CharField(max_length=30, null=True)
    username = fields.CharField(max_length=30, null=True)
    is_blocked = fields.BooleanField(default=False)
    is_banned = fields.BooleanField(default=False)

    class Meta:  # pylint: disable=too-few-public-methods
        """Meta settings class."""

        table = "users"
        description = "Model for bot users."

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
