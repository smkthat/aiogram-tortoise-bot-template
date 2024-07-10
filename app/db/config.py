# -*- coding: utf-8 -*-

"""
This module contains database config.
"""

from typing import Any, List

from app.settings import settings

MODELS_MODULES: List[str] = ["app.db.models.user_model"]  # noqa: WPS407

TORTOISE_CONFIG: dict[str, Any] = {  # noqa: WPS407
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
