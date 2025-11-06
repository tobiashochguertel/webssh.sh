# webssh.sh

[![Tests](https://github.com/tobiashochguertel/webssh.sh/actions/workflows/test.yml/badge.svg)](https://github.com/tobiashochguertel/webssh.sh/actions/workflows/test.yml)
[![Python 3.8+](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)

Shell Helpers about WebSSH

## Installation
```bash
pip install webssh-sh
```

## Usage
### wshcopy
Helper which allows you to write to your own terminal clipboard (on your computer) through your remote terminal connection.

```bash
echo "WebSSH is awesome!" | wshcopy
```

If you use tmux >= 3.3 you will need either :
* `set -g allow-passthrough on` **THEN** `echo "WebSSH is awesome!" | wshcopy -t tmux`
* **OR**
* `set -g set-clipboard on` **THEN** `echo "WebSSH is awesome!" | wshcopy -t default`

## Development

### Python Version Support
This project supports Python 3.8 through 3.14+.

### Setup Development Environment
```bash
# Install development dependencies
pip install -r requirements-dev.txt

# Install package in editable mode
pip install -e .
```

### Running Tests

#### Using pytest directly
```bash
# Run all tests
pytest

# Run unit tests only
pytest tests/test_wshcopy.py

# Run integration tests
pytest tests/test_integration.py

# Run e2e tests
pytest tests/test_e2e.py

# Run with coverage
pytest --cov=wsh --cov-report=html
```

#### Using nox (recommended for multi-version testing)
```bash
# Run tests on all Python versions
nox

# Run tests on specific Python version
nox -s tests-3.11

# Run only integration tests
nox -s integration

# Run only e2e tests
nox -s e2e

# Generate coverage report
nox -s coverage
```

#### Using tox
```bash
# Run tests on all Python versions
tox

# Run tests on specific Python version
tox -e py311

# Run linting
tox -e lint
```

#### Using Make
```bash
# Run all tests
make test

# Run tests on all Python versions
make test-all

# Run linting
make lint

# Format code
make format
```

### Python 3.8+ Compatibility Strategy

This project uses `importlib.metadata` (available in Python 3.8+) instead of the deprecated `pkg_resources`:

```python
try:
    from importlib.metadata import version
except ImportError:
    from importlib_metadata import version  # Fallback for older versions
```

For Python < 3.8, the `importlib-metadata` backport is automatically installed.