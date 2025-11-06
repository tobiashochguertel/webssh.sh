#!/usr/bin/env bash
# Script to test across multiple Python versions

set -e

echo "================================"
echo "Testing webssh-sh across Python versions"
echo "================================"
echo ""

PYTHON_VERSIONS=("3.8" "3.9" "3.10" "3.11" "3.12" "3.13" "3.14")
FAILED_VERSIONS=()
SUCCESSFUL_VERSIONS=()

for version in "${PYTHON_VERSIONS[@]}"; do
    python_cmd="python${version}"
    
    # Check if Python version is available
    if ! command -v "$python_cmd" &> /dev/null; then
        echo "⚠️  Python $version not found, skipping..."
        echo ""
        continue
    fi
    
    echo "Testing with Python $version..."
    echo "----------------------------"
    
    # Create temporary venv for this version
    venv_dir="venv_test_${version}"
    
    # Clean up old venv if exists
    if [ -d "$venv_dir" ]; then
        rm -rf "$venv_dir"
    fi
    
    # Create and activate venv
    "$python_cmd" -m venv "$venv_dir"
    source "$venv_dir/bin/activate"
    
    # Install package and test dependencies
    pip install -q --upgrade pip
    pip install -q -e .
    pip install -q pytest pytest-cov pytest-mock
    
    # Run tests
    if pytest -v --tb=short; then
        echo "✅ Python $version: PASSED"
        SUCCESSFUL_VERSIONS+=("$version")
    else
        echo "❌ Python $version: FAILED"
        FAILED_VERSIONS+=("$version")
    fi
    
    # Deactivate and clean up
    deactivate
    rm -rf "$venv_dir"
    
    echo ""
done

# Summary
echo "================================"
echo "Test Summary"
echo "================================"

if [ ${#SUCCESSFUL_VERSIONS[@]} -gt 0 ]; then
    echo "✅ Passed: ${SUCCESSFUL_VERSIONS[*]}"
fi

if [ ${#FAILED_VERSIONS[@]} -gt 0 ]; then
    echo "❌ Failed: ${FAILED_VERSIONS[*]}"
    exit 1
else
    echo ""
    echo "🎉 All tests passed!"
    exit 0
fi
