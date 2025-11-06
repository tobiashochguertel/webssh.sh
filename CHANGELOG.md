# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Python 3.8 through 3.14+ support
- Comprehensive test suite (unit, integration, e2e)
- pytest-based testing framework
- nox configuration for multi-version testing
- tox configuration for multi-version testing
- GitHub Actions CI workflow for automated testing
- Makefile for convenient development commands
- `test_all_versions.sh` script for local multi-version testing
- `TESTING.md` comprehensive testing documentation
- `pyproject.toml` for modern Python packaging
- Code formatting configuration (black, isort)
- Coverage reporting (HTML, XML, terminal)

### Changed
- **BREAKING**: Replaced deprecated `pkg_resources` with `importlib.metadata`
  - Required for Python 3.12+ compatibility
  - Improves performance and follows modern Python packaging standards
- Updated `setup.py` with Python version classifiers
- Enhanced `README.md` with development and testing instructions
- Fixed invalid escape sequence warning for Python 3.14+

### Deprecated
- None

### Removed
- `pkg_resources` dependency (deprecated in Python 3.12+)

### Fixed
- Invalid escape sequence `\D` changed to raw string `r'\D'` for Python 3.14+
- Added proper Python version compatibility handling

### Security
- None

## [22.11.8] - Original Version
- Initial version with `wshcopy` command
- OSC52 sequence support for clipboard operations
- tmux and screen terminal support
