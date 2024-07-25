# -*- coding: utf-8 -*-

"""This module is a database tests."""

import pytest
from loguru import logger
from pytest_mock import MockFixture
from tortoise import Tortoise, connections
from tortoise.exceptions import BaseORMException, ConfigurationError

from app.db.config import TORTOISE_CONFIG
from app.db.engine import database_close, database_init


@pytest.fixture(scope="function")
async def init_database() -> None:
    """Init database fixture."""
    await database_init()


class TestDatabase:
    """Database tests."""

    @pytest.mark.asyncio
    async def test_database_initializes_successfully(
        self,
        mocker: MockFixture,
    ) -> None:
        """Initializes the database successfully with the provided config.

        This test case ensures that the database initializes correctly using
        the specified configuration.
        It mocks the initialization process and verifies that the configuration
        is passed correctly to Tortoise.
        """
        mocker.patch("tortoise.Tortoise.init", return_value=None)
        await database_init()
        Tortoise.init.assert_called_once_with(  # type: ignore[attr-defined]
            config=TORTOISE_CONFIG,
        )

    @pytest.mark.asyncio
    async def test_logger_outputs_correct_debug_messages(
        self,
        mocker: MockFixture,
    ) -> None:
        """Logger outputs the correct debug messages during initialization."""
        mock_logger = mocker.patch.object(logger, "debug")
        await database_init()
        mock_logger.assert_any_call("Initializing Tortoise...")
        mock_logger.assert_any_call("Tortoise inited!")

    @pytest.mark.asyncio
    async def test_tortoise_orm_initializes_without_exceptions(
        self,
        mocker: MockFixture,
    ) -> None:
        """Tortoise ORM initializes without any exceptions."""
        mocker.patch("tortoise.Tortoise.init", return_value=None)
        try:
            await database_init()
        except BaseORMException as e:
            pytest.fail(f"Initialization failed with exception: {e}")

    @pytest.mark.asyncio
    async def test_invalid_database_url_in_configuration(
        self,
        mocker: MockFixture,
    ) -> None:
        """Database URL in the configuration is invalid."""
        invalid_config = TORTOISE_CONFIG.copy()
        invalid_config["connections"]["default"] = "invalid_url"
        mocker.patch("app.db.config.TORTOISE_CONFIG", invalid_config)
        with pytest.raises(ConfigurationError):
            await database_init()

    @pytest.mark.asyncio
    async def test_network_issues_during_database_connection(
        self,
        mocker: MockFixture,
    ) -> None:
        """Network issues occur during database connection."""
        mocker.patch(
            "tortoise.Tortoise.init",
            side_effect=ConnectionError("Network issue"),
        )
        with pytest.raises(ConnectionError):
            await database_init()

    @pytest.mark.asyncio
    async def test_tortoise_orm_initialization_fails_due_to_incorrect_model_definitions(
        self,
        mocker: MockFixture,
    ) -> None:
        """Tortoise ORM initialization fails due to incorrect model definitions."""
        mocker.patch(
            "tortoise.Tortoise.init",
            side_effect=ValueError("Incorrect model definitions"),
        )
        with pytest.raises(ValueError):
            await database_init()

    @pytest.mark.asyncio(fixture=init_database)
    async def test_successfully_closes_all_connections(
        self,
        mocker: MockFixture,
    ) -> None:
        """Test that successfully closes all database connections."""
        mock_close_all = mocker.patch.object(
            connections,
            "close_all",
            return_value=None,
        )
        await database_close()
        mock_close_all.assert_called_once()

    @pytest.mark.asyncio(fixture=init_database)
    async def test_handles_no_open_connections(
        self,
        mocker: MockFixture,
    ) -> None:
        """Handles the scenario where no database connections are open."""
        mock_close_all = mocker.patch.object(
            connections,
            "close_all",
            return_value=None,
        )
        await database_close()
        mock_close_all.assert_called_once()
