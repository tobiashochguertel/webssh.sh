# Testing Guide

This document describes the testing strategy for webssh-sh, including support for Python 3.8 through 3.14+.

## Test Structure

The test suite is organized into three categories:

### 1. Unit Tests (`tests/test_wshcopy.py`)
- **Purpose**: Test individual functions in isolation
- **Coverage**: 
  - `read_stdin()` - stdin reading logic
  - Terminal detection functions (`is_tmux()`, `is_screen()`)
  - OSC52 sequence generation
  - CLI functionality
- **Run**: `pytest tests/test_wshcopy.py -v`

### 2. Integration Tests (`tests/test_integration.py`)
- **Purpose**: Test module execution via subprocess
- **Coverage**:
  - Command-line interface
  - Argument parsing
  - Input/output handling
  - Terminal type flags
- **Run**: `pytest tests/test_integration.py -v`

### 3. End-to-End Tests (`tests/test_e2e.py`)
- **Purpose**: Simulate real-world usage scenarios
- **Coverage**:
  - Piping content to wshcopy
  - File redirection
  - Unicode handling
  - Large content handling
- **Run**: `pytest tests/test_e2e.py -v`

## Running Tests

### Quick Test
```bash
# Run all tests with current Python version
pytest

# Run with coverage
pytest --cov=wsh --cov-report=html
```

### Test Across Multiple Python Versions

#### Using nox (Recommended)
```bash
# Install nox
pip install nox

# Run tests on all Python versions
nox

# Run tests on specific version
nox -s tests-3.11

# Run specific test type
nox -s integration
nox -s e2e

# Run with custom pytest arguments
nox -s tests -- -k test_cli
```

#### Using tox
```bash
# Install tox
pip install tox

# Run tests on all Python versions
tox

# Run on specific version
tox -e py311

# Run linting
tox -e lint
```

#### Using custom script
```bash
# Make executable (if not already)
chmod +x test_all_versions.sh

# Run tests across all installed Python versions
./test_all_versions.sh
```

#### Using Makefile
```bash
# Run tests with current Python
make test

# Run tests on all Python versions (via nox)
make test-all

# Run linting
make lint

# Format code
make format
```

## Python Version Compatibility

### Compatibility Strategy

The project uses `importlib.metadata` for version retrieval, which is:
- Built-in for Python 3.8+
- Available via `importlib-metadata` backport for older versions

```python
try:
    from importlib.metadata import version
except ImportError:
    from importlib_metadata import version
```

### Deprecated Feature: pkg_resources

Python 3.12+ deprecated `pkg_resources` (from setuptools). We've migrated to `importlib.metadata` which is:
- **Standard library** (Python 3.8+)
- **Faster** (no scanning of installed packages)
- **Recommended** by Python packaging guidelines

References:
- [Python Issue #2485](https://github.com/mu-editor/mu/issues/2485)
- [PEP 566 - Metadata for Python Software Packages 2.1](https://peps.python.org/pep-0566/)

### Testing Matrix

| Python Version | Status | Notes |
|---------------|--------|-------|
| 3.8 | ✅ Supported | Uses importlib.metadata (built-in) |
| 3.9 | ✅ Supported | Uses importlib.metadata (built-in) |
| 3.10 | ✅ Supported | Uses importlib.metadata (built-in) |
| 3.11 | ✅ Supported | Uses importlib.metadata (built-in) |
| 3.12 | ✅ Supported | pkg_resources deprecated |
| 3.13 | ✅ Supported | pkg_resources deprecated |
| 3.14+ | ✅ Supported | pkg_resources deprecated |

## Continuous Integration

Tests run automatically on GitHub Actions for:
- **Operating Systems**: Ubuntu, macOS, Windows
- **Python Versions**: 3.8, 3.9, 3.10, 3.11, 3.12, 3.13
- **Trigger**: Push to main/master, Pull requests

See `.github/workflows/test.yml` for configuration.

## Coverage Requirements

- **Target**: 90%+ code coverage
- **Current**: 93%+
- **Reports**: 
  - Terminal output
  - HTML report in `htmlcov/`
  - XML report in `coverage.xml`

## Test Development Guidelines

### Writing New Tests

1. **Unit tests**: Test functions in isolation with mocked dependencies
2. **Integration tests**: Test subprocess execution with real inputs
3. **E2E tests**: Test complete workflows as users would use them

### Best Practices

- Use descriptive test names: `test_<what>_<condition>_<expected>`
- Use pytest fixtures for common setup
- Mock external dependencies (stdin, environment variables)
- Test both success and failure paths
- Include edge cases (empty input, large input, unicode)

### Running Specific Tests

```bash
# Run tests matching pattern
pytest -k test_cli

# Run specific test file
pytest tests/test_wshcopy.py

# Run specific test class
pytest tests/test_wshcopy.py::TestCLI

# Run specific test method
pytest tests/test_wshcopy.py::TestCLI::test_cli_version

# Run with verbose output
pytest -vv

# Run with stdout capture disabled
pytest -s
```

## Troubleshooting

### Test Failures

1. **Import errors**: Ensure package is installed: `pip install -e .`
2. **Missing Python version**: Install via pyenv or system package manager
3. **Coverage issues**: Install pytest-cov: `pip install pytest-cov`

### Common Issues

**Issue**: Tests fail with "externally-managed-environment"  
**Solution**: Use virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -e .
```

**Issue**: Python version not found  
**Solution**: Install via pyenv:
```bash
pyenv install 3.11.0
pyenv global 3.11.0
```

## Performance

Test execution times (approximate):
- Unit tests: ~0.1s
- Integration tests: ~0.3s
- E2E tests: ~0.3s
- **Total**: ~0.7s per Python version

## Contributing

When contributing, ensure:
1. All tests pass: `pytest`
2. Coverage remains above 90%: `pytest --cov=wsh`
3. Tests pass on multiple Python versions: `nox`
4. Code is formatted: `make format`
5. No linting errors: `make lint`
