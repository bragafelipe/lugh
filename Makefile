SHELL := /bin/bash

.PHONY: setup test lint

setup:
	python -m venv .venv
	. .venv/bin/activate && pip install -U pip && pip install -r requirements-dev.txt

test:
	. .venv/bin/activate && pytest -q

lint:
	. .venv/bin/activate && ruff check src tests
