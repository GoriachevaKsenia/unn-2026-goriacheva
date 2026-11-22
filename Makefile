.PHONY: install test ruff-cs-check ruff-cs-fix ruff-linter-check ruff-linter-fix mypy-check check build

install:
	pip install -r requirements-dev.txt

test:
	python -m unittest discover -s tests -v

ruff-cs-check:
	ruff format --check .

ruff-cs-fix:
	ruff format .

ruff-linter-check:
	ruff check .

ruff-linter-fix:
	ruff check --fix .

mypy-check:
	mypy

check: ruff-cs-check ruff-linter-check mypy-check test

build:
	docker build -t unn-2026-goriacheva-bot .