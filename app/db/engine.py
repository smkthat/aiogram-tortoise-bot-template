# -*- coding: utf-8 -*-

"""This module is a database initializer."""

from loguru import logger
from tortoise import Tortoise, connections, run_async

from app.db.config import TORTOISE_CONFIG


async def database_init() -> None:
    """Init database."""
    logger.debug("Initializing Tortoise...")
    await Tortoise.init(
        config=TORTOISE_CONFIG,
    )
    logger.debug("Tortoise inited!")


async def database_close() -> None:
    """Close database."""
    logger.debug("Closing Tortoise...")
    await connections.close_all()
    logger.debug("Tortoise closed!")


def generate_schema() -> None:
    """Generate schema."""
    logger.debug("Generating schema...")
    run_async(Tortoise.generate_schemas())
    logger.debug("Schema generated!")
