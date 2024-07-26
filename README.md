# tg-schedule-bot

Telegram bot for managing schedules

![GitHub last commit](https://img.shields.io/github/last-commit/smkthat/tg-schedule-bot)
![project version](https://img.shields.io/badge/dynamic/toml?url=https%3A%2F%2Fraw.githubusercontent.com%2Fsmkthat%2Ftg-schedule-bot%2Fmaster%2Fpyproject.toml&query=%24.tool.poetry.version&style=flat&label=v&color=999)
![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/smkthat/tg-schedule-bot/tests.yaml?branch=dev&style=flat&label=tests)
[![codecov](https://codecov.io/github/smkthat/tg-schedule-bot/branch/dev/graph/badge.svg?token=5FD3OGMA1X)](https://codecov.io/github/smkthat/tg-schedule-bot)

![aiogram framework](https://img.shields.io/badge/dynamic/toml?url=https%3A%2F%2Fraw.githubusercontent.com%2Fsmkthat%2Ftg-schedule-bot%2Fmaster%2Fpyproject.toml&query=%24.tool.poetry.dependencies.aiogram&style=flat&logo=aiogram&label=aiogram)
![python version](https://img.shields.io/badge/dynamic/toml?url=https%3A%2F%2Fraw.githubusercontent.com%2Fsmkthat%2Ftg-schedule-bot%2Fmaster%2Fpyproject.toml&query=%24.tool.poetry.dependencies.python&style=flat&logo=python&label=python)

---

## Main configuration

- [x] Poetry dependency management
- [x] Loguru
- [x] Aiogram Framework
- [x] Tortoise ORM and Aerich migrations with PostgreSQL database
- [x] Linting with Ruff, Pylint, MyPy
- [x] Pre-commit, tests workflow, Codecov analysis

## Poetry build-system

[![Poetry](https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json)](https://python-poetry.org/)

This project uses `poetry`.
To run the project, use this set of commands:

```bash
poetry install
```

The lock command allows you to fix dependencies by updating the `poetry.lock`
file:

```bash
poetry lock
```

Be careful!
By default, poetry lock will attempt to update all dependencies to the
latest valid versions.
To avoid this, use the `--no-update` option.

```bash
poetry lock --no-update
```

Synchronize the virtual environment with the `.lock` file:

```bash
poetry lock --sync
```

You can read more about poetry here: https://python-poetry.org/

## Run project

For local running, use:

```bash
poetry run python -m src
```

## Configuration

This application can be configured with environment variables.

You can create `.env` file in the root directory and place all
environment variables here.

All environment variables should start with "**BOT_**" prefix.

For example if you see in your "src/settings.py" a variable named like
`random_parameter`, you should provide the "**BOT_RANDOM_PARAMETER**"
variable to configure the value.
This behaviour can be changed by overriding `env_prefix` property
in `src.settings.Settings.Config`.

An example of .env file:

```dotenv
BOT_ENVIRONMENT="dev"
BOT_TOKEN="123456:Your_bot_token"
BOT_DB_HOST="localhost"
```

You can read more about BaseSettings class
here: https://pydantic-docs.helpmanual.io/usage/settings/

## Pre-commit

To install `pre-commit` simply run inside the shell:

```bash
pre-commit install
```

pre-commit is very useful to check your code before publishing it.
It's configured using `.pre-commit-config.yaml` file.

By default, it runs:

* `ruff` (formats & validates)
* `black` (formats your code);
* `mypy` (validates types);

Use for local running:

```bash
pre-commit run --all-files --verbose
```

You can read more about pre-commit here: https://pre-commit.com/

## Migrations

For manual first initial database use:

```bash
aerich init-db
```

If you want to migrate your database, you should run the following commands:

```bash
# Upgrade database to the last migration.
aerich upgrade
```

### Reverting migrations

If you want to revert migrations, you should run:

```bash
aerich downgrade
```

### Migration generation

To generate migrations you should run:

```bash
aerich migrate
```

## Tests

For run tests locally, use:

```bash
poetry run pytest -vv ./tests
```

Running with coverage:

```bash
poetry run pytest -vv ./tests --cov
```
