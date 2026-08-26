.PHONY: test lint format check

test:
	uv run pytest -v

lint:
	uv run ruff check .

format:
	uv run ruff format .

check: lint test
