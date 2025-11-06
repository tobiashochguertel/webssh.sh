# Contributing to webssh-sh

Thank you for your interest in contributing! This document provides guidelines for contributing to webssh-sh.

## Getting Started

### Prerequisites
- Python 3.8 or higher
- Git
- pip

### Setup Development Environment

1. **Fork and clone the repository**
```bash
git clone https://github.com/YOUR_USERNAME/webssh.sh.git
cd webssh.sh
```

2. **Create a virtual environment**
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install development dependencies**
```bash
pip install -r requirements-dev.txt
pip install -e .
```

## Development Workflow

### Making Changes

1. **Create a branch**
```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/your-bug-fix
```

2. **Make your changes**
- Write clear, concise code
- Follow PEP 8 style guidelines
- Add docstrings for new functions/classes
- Update documentation if needed

3. **Write tests**
- Add unit tests for new functions
- Add integration tests for new features
- Ensure all tests pass

### Testing

```bash
# Run all tests
make test

# Run tests with coverage
pytest --cov=wsh --cov-report=html

# Run tests on multiple Python versions
make test-all  # or: nox

# Run specific test
pytest tests/test_wshcopy.py::TestCLI::test_cli_version
```

### Code Quality

```bash
# Format code
make format
# or
black wsh tests
isort wsh tests

# Run linters
make lint
# or
flake8 wsh tests
```

### Commit Messages

Use clear, descriptive commit messages:
- `Add: <description>` for new features
- `Fix: <description>` for bug fixes
- `Update: <description>` for updates to existing features
- `Refactor: <description>` for code refactoring
- `Docs: <description>` for documentation changes
- `Test: <description>` for test-related changes

Example:
```
Add: Support for custom terminal types

- Add --terminal-type flag
- Add tests for custom terminal detection
- Update README with usage examples
```

### Pull Request Process

1. **Update documentation**
   - Update README.md if needed
   - Update CHANGELOG.md
   - Add/update docstrings

2. **Ensure tests pass**
```bash
pytest
nox  # Test multiple Python versions
```

3. **Push your changes**
```bash
git push origin feature/your-feature-name
```

4. **Create a Pull Request**
   - Use a clear title and description
   - Reference any related issues
   - Include screenshots if applicable

5. **Code Review**
   - Address review comments
   - Keep the PR focused on a single change

## Testing Guidelines

### Test Structure
- **Unit tests**: Test individual functions (`tests/test_wshcopy.py`)
- **Integration tests**: Test subprocess execution (`tests/test_integration.py`)
- **E2E tests**: Test real-world scenarios (`tests/test_e2e.py`)

### Writing Tests
```python
def test_function_name_condition_expected():
    """Test description"""
    # Arrange
    input_data = "test"
    
    # Act
    result = function_to_test(input_data)
    
    # Assert
    assert result == expected_value
```

### Test Coverage
- Aim for 90%+ coverage
- Test both success and failure cases
- Test edge cases (empty input, large input, unicode, etc.)

## Python Version Support

This project supports Python 3.8 through 3.14+. When contributing:
- Use features available in Python 3.8+
- Test on multiple Python versions using nox
- Use `importlib.metadata` instead of `pkg_resources`

### Compatibility Example
```python
# Good: Compatible with Python 3.8+
try:
    from importlib.metadata import version
except ImportError:
    from importlib_metadata import version

# Avoid: Deprecated in Python 3.12+
import pkg_resources
```

## Code Style

### Python Style
- Follow PEP 8
- Max line length: 100 characters
- Use black for formatting
- Use isort for import sorting

### Naming Conventions
- Functions: `snake_case`
- Classes: `PascalCase`
- Constants: `UPPER_SNAKE_CASE`
- Private: `_leading_underscore`

### Documentation
- Add docstrings to all public functions/classes
- Use Google-style docstrings
- Include examples in docstrings when helpful

Example:
```python
def function_name(arg1: str, arg2: int) -> bool:
    """
    Brief description of function.
    
    Longer description if needed. Can include implementation
    details, algorithm explanations, etc.
    
    Args:
        arg1: Description of arg1
        arg2: Description of arg2
    
    Returns:
        Description of return value
    
    Raises:
        ValueError: When input is invalid
    
    Example:
        >>> function_name("test", 42)
        True
    """
    pass
```

## Questions or Issues?

- **Questions**: Open a GitHub Discussion
- **Bugs**: Open a GitHub Issue with reproduction steps
- **Features**: Open a GitHub Issue with detailed description

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
