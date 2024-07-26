# -*- coding: utf-8 -*-

"""This module contains database config."""
import os
from typing import Any, List

from loguru import logger

from src.settings import settings


def get_models_modules(
    models_dir: str = 'src.db.models',
) -> List[str]:
    """Retrieve a list of model modules from the specified directory.

    Args:
        models_dir (str): The directory path where the model modules
            are located.
            Defaults to 'src.db.models'.

    Returns:
        List[str]: A list of model modules found in the directory
            or empy list.

    Raises:
        FileNotFoundError: If the specified directory is not found.
        PermissionError: If there is a permission error accessing
            the directory.

    Example:
        If the models are located in 'src.db.models',
        calling get_models_modules()
        will return a list of model modules like
        ['src.db.models.module1', 'src.db.models.module2'].
    """
    try:
        models_path = os.path.join(
            settings.app_path,
            models_dir.replace('.', '/'),
        )
        return [
            f"{models_dir.replace('/', '.')}.{file_name[:-3]}"
            for file_name in os.listdir(models_path)
            if file_name.endswith('.py') and not file_name.startswith('__')
        ]
    except (FileNotFoundError, PermissionError) as e:
        logger.error(f"Error accessing models directory: {e}")
        return []


# or use for manual providing models (example: ['src.db.models.user_model'])
# MODELS_MODULES: List[str] = ["src.<path>.<to>.<model_module_name>"]

# use for automatically detect modules from models directory
MODELS_MODULES = get_models_modules()

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
