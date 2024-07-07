# tg-schedule-bot

Telegram bot for managing schedules

---


## Run project

This project uses `poetry`.
To run the project, use this set of commands:

```bash
poetry install
```

```bash
poetry run python -m app
```

You can read more about poetry here: https://python-poetry.org/


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
