MAP ?= maps/example.txt
VENV = .venv

install:
	uv sync

run: $(VENV)
	uv run python -m main.py $(MAP)

debug:
	uv run python -m pdb main.py $(MAP)

clean:
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type d -name ".mypy_cache" -exec rm -rf {} +
	rm -rf .ruff_cache .pytest_cache dist build *.egg-info

lint:
	uv run flake8 . --exclude $(VENV)
	uv run mypy . --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs

lint-strict:
	uv run flake8 . --exclude $(VENV)
	uv run mypy . --strict

.PHONY: install run debug clean lint lint-strict