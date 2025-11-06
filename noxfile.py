import nox

# Define Python versions to test
PYTHON_VERSIONS = ["3.8", "3.9", "3.10", "3.11", "3.12", "3.13", "3.14"]


@nox.session(python=PYTHON_VERSIONS)
def tests(session):
    """Run tests with pytest"""
    session.install("pytest>=7.0", "pytest-cov>=4.0", "pytest-mock>=3.10")
    session.install("-e", ".")
    session.run("pytest", *session.posargs)


@nox.session(python=PYTHON_VERSIONS)
def integration(session):
    """Run integration tests"""
    session.install("pytest>=7.0")
    session.install("-e", ".")
    session.run("pytest", "tests/test_integration.py", "-v", *session.posargs)


@nox.session(python=PYTHON_VERSIONS)
def e2e(session):
    """Run end-to-end tests"""
    session.install("pytest>=7.0")
    session.install("-e", ".")
    session.run("pytest", "tests/test_e2e.py", "-v", *session.posargs)


@nox.session(python="3.11")
def lint(session):
    """Run linters"""
    session.install("flake8", "black", "isort")
    session.run("flake8", "wsh", "tests")
    session.run("black", "--check", "wsh", "tests")
    session.run("isort", "--check-only", "wsh", "tests")


@nox.session(python="3.11")
def format(session):
    """Format code with black and isort"""
    session.install("black", "isort")
    session.run("black", "wsh", "tests")
    session.run("isort", "wsh", "tests")


@nox.session(python="3.11")
def coverage(session):
    """Generate coverage report"""
    session.install("pytest>=7.0", "pytest-cov>=4.0", "pytest-mock>=3.10")
    session.install("-e", ".")
    session.run(
        "pytest",
        "--cov=wsh",
        "--cov-report=html",
        "--cov-report=term",
        *session.posargs
    )
