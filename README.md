# tg-schedule-bot

Telegram bot for managing schedules

---

## Poetry build-system

This project uses `poetry`.
To run the project, use this set of commands:

```bash
poetry install
```

The lock command allows you to fix dependencies by updating the `poetry.lock` file:

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
poetry run python -m app
```

## Configuration

This application can be configured with environment variables.

You can create `.env` file in the root directory and place all
environment variables here.

All environment variables should start with "**BOT_**" prefix.

For example if you see in your "app/settings.py" a variable named like
`random_parameter`, you should provide the "**BOT_RANDOM_PARAMETER**"
variable to configure the value.
This behaviour can be changed by overriding `env_prefix` property
in `app.settings.Settings.Config`.

An example of .env file:

```dotenv
BOT_ENVIRONMENT="dev"
BOT_TOKEN="True"
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
pre-commit run --all-files --verbose --show-diff-on-failure
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
