# -*- coding: utf-8 -*-

"""This module contains database config."""

from typing import Any, List

from app.settings import settings

MODELS_MODULES: List[str] = ["app.db.models.user_model"]

TORTOISE_CONFIG: dict[str, Any] = {
    "connections": {
        "default": str(settings.db_url),
    },
    "apps": {
        "models": {
            "models": MODELS_MODULES + ["aerich.models"],
            "default_connection": "default",
        },
    },
}
