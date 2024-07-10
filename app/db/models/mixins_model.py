# -*- coding: utf-8 -*-

"""
This module contains a base model.
"""

from tortoise import fields


class DateTimeModelMixin:  # pylint: disable=too-few-public-methods
    """
    A mixin class that adds 'created_at' and 'updated_at' fields to a model
    for tracking the creation and last update timestamps.

    Attributes:
        `created_at` (fields.DatetimeField): A field that automatically sets
            the timestamp when an instance is created.
        `updated_at` (fields.DatetimeField): A field that automatically updates
            the timestamp when an instance is modified.
    """

    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)
