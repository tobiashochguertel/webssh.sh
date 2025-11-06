# Deprecation Warnings

## Setuptools License Format Warnings

The build process may show deprecation warnings about `project.license` format:

```
SetuptoolsDeprecationWarning: `project.license` as a TOML table is deprecated
```

**Status**: These are informational warnings about future setuptools changes (setuptools 77.0.0+).

**Why we keep current format**:
- Current format (`license = {text = "MIT"}`) works with setuptools 61.0+
- New SPDX format (`license = "MIT"`) requires setuptools 77.0.0+ (released 2025)
- We support Python 3.8+ which may have older setuptools in some environments
- The warnings do NOT affect build success or package functionality

**Action timeline**:
- By 2026-Feb-18: Update to SPDX format when setuptools 77.0.0+ is widely adopted
- Current builds: ✅ Working perfectly, warnings are cosmetic only

**References**:
- https://packaging.python.org/en/latest/guides/writing-pyproject-toml/#license
- https://github.com/pypa/setuptools/issues/3823
