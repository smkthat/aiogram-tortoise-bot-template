# -*- coding: utf-8 -*-

"""This module is a database tests."""

import pytest
from loguru import logger
from pytest_mock import MockFixture
from tortoise import Tortoise, connections
from tortoise.exceptions import BaseORMException, ConfigurationError

from src.db.config import TORTOISE_CONFIG, get_models_modules
from src.db.engine import database_close, database_init


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
        # Given
        mocker.patch("tortoise.Tortoise.init", return_value=None)
        # When
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
        # Given
        mock_logger = mocker.patch.object(logger, "debug")
        await database_init()
        # When
        mock_logger.assert_any_call("Initializing Tortoise...")
        mock_logger.assert_any_call("Tortoise inited!")

    @pytest.mark.asyncio
    async def test_tortoise_orm_initializes_without_exceptions(
        self,
        mocker: MockFixture,
    ) -> None:
        """Tortoise ORM initializes without any exceptions."""
        # Given
        mocker.patch("tortoise.Tortoise.init", return_value=None)
        try:
            # When
            await database_init()
        except BaseORMException as e:
            # Then
            pytest.fail(f"Initialization failed with exception: {e}")

    @pytest.mark.asyncio
    async def test_invalid_database_url_in_configuration(
        self,
        mocker: MockFixture,
    ) -> None:
        """Database URL in the configuration is invalid."""
        # Given
        invalid_config = TORTOISE_CONFIG.copy()
        invalid_config["connections"]["default"] = "invalid_url"
        # When
        mocker.patch("src.db.config.TORTOISE_CONFIG", invalid_config)
        # Then
        with pytest.raises(ConfigurationError):
            await database_init()

    @pytest.mark.asyncio
    async def test_network_issues_during_database_connection(
        self,
        mocker: MockFixture,
    ) -> None:
        """Network issues occur during database connection."""
        # Given
        mocker.patch(
            "tortoise.Tortoise.init",
            side_effect=ConnectionError("Network issue"),
        )
        # When, Then
        with pytest.raises(ConnectionError):
            await database_init()

    @pytest.mark.asyncio
    async def test_tortoise_init_fails_due_to_incorrect_model_definitions(
        self,
        mocker: MockFixture,
    ) -> None:
        """Tortoise initialization fails due to incorrect model definitions."""
        # Given
        mocker.patch(
            "tortoise.Tortoise.init",
            side_effect=ValueError("Incorrect model definitions"),
        )

        # When, Then
        with pytest.raises(ValueError):
            await database_init()

    @pytest.mark.asyncio(fixture=init_database)
    async def test_successfully_closes_all_connections(
        self,
        mocker: MockFixture,
    ) -> None:
        """Test that successfully closes all database connections."""
        # Given
        mock_close_all = mocker.patch.object(
            connections,
            "close_all",
            return_value=None,
        )
        # When
        await database_close()
        # Then
        mock_close_all.assert_called_once()

    @pytest.mark.asyncio(fixture=init_database)
    async def test_handles_no_open_connections(
        self,
        mocker: MockFixture,
    ) -> None:
        """Handles the scenario where no database connections are open."""
        # Given
        mock_close_all = mocker.patch.object(
            connections,
            "close_all",
            return_value=None,
        )
        # When
        await database_close()
        # Then
        mock_close_all.assert_called_once()

    def test_retrieve_list_of_model_modules_from_default_directory(
        self,
        mocker: MockFixture,
    ) -> None:
        """Retrieve a list of model modules from the default directory."""
        # Given
        mocker.patch('os.listdir', return_value=['module1.py', 'module2.py'])
        expected_modules = ['src.db.models.module1', 'src.db.models.module2']
        # When
        result = get_models_modules()
        # Then
        assert result == expected_modules

    def test_directory_does_not_exist(self, mocker: MockFixture) -> None:
        """The Directory does not exist."""
        # Given
        mocker.patch('os.listdir', side_effect=FileNotFoundError)
        # When
        result = get_models_modules()
        # Then
        assert result == []

    def test_directory_is_empty(self, mocker: MockFixture) -> None:
        """The Directory is empty."""
        # Given
        mocker.patch('os.listdir', return_value=[])
        # When
        result = get_models_modules()
        # Then
        assert result == []

    def test_correctly_format_module_names(self, mocker: MockFixture) -> None:
        """The module names are correctly formatted."""
        # Given
        mocker.patch('os.listdir', return_value=['module1.py', 'module2.py'])
        expected_modules = ['src.db.models.module1', 'src.db.models.module2']
        # When
        result = get_models_modules()
        # Then
        assert result == expected_modules

    def test_retrieve_list_of_modules_from_default_directory(
        self,
        mocker: MockFixture,
    ) -> None:
        """Retrieve a list of model modules from a specified directory."""
        # Given
        mocker.patch('os.listdir', return_value=['module1.py', 'module2.py'])
        expected_modules = ['src.db.models.module1', 'src.db.models.module2']
        # When
        result = get_models_modules()
        # Then
        assert result == expected_modules

    def test_directory_contains_files_starting_with_double_underscore(
        self,
        mocker: MockFixture,
    ) -> None:
        """The Directory contains Python files starting with '__'."""
        # Given
        mocker.patch(
            'os.listdir',
            return_value=['module1.py', '__module2.py', '__module3.py'],
        )
        expected_modules = ['src.db.models.module1']
        # When
        result = get_models_modules()
        # Then
        assert result == expected_modules
