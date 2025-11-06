.PHONY: test test-all lint format clean install-dev help

help:
	@echo "Available commands:"
	@echo "  make test        - Run tests with pytest"
	@echo "  make test-all    - Run tests on all Python versions with nox"
	@echo "  make lint        - Run linters"
	@echo "  make format      - Format code with black and isort"
	@echo "  make clean       - Remove cache and build files"
	@echo "  make install-dev - Install development dependencies"

install-dev:
	pip install -r requirements-dev.txt
	pip install -e .

test:
	pytest -v --cov=wsh --cov-report=term-missing

test-all:
	nox

lint:
	nox -s lint

format:
	nox -s format

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".tox" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".nox" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name "htmlcov" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name ".coverage" -delete 2>/dev/null || true
	find . -type f -name "coverage.xml" -delete 2>/dev/null || true
