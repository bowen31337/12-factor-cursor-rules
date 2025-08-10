# Tests

This folder contains a small validation script to check action JSON files against the local tool schemas.

Run examples:
  python3 tests/validate_action.py tests/sample_action_valid.json
  python3 tests/validate_action.py tests/sample_action_invalid.json

If you have `jsonschema` installed (pip install jsonschema), the script will use it for full validation,
otherwise it will run a small built-in validator for common checks.
