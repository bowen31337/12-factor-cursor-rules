#!/usr/bin/env python3
"""Simple validator for Cursor action against local tool JSON Schemas.

Usage:
  python3 tests/validate_action.py tests/sample_action_valid.json

The script will:
  - load the action file (first arg)
  - lookup a schema for action['action'] in ops/tool-schemas/<action>.json
  - validate params against the schema (using jsonschema if installed)
  - run basic checks (confidence threshold, explain presence)
"""
import sys, json, os, re

def is_email(s):
    # simple email check
    return bool(re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", s))

def lightweight_validate(schema, data):
    errs = []
    # check required
    for field in schema.get('required', []):
        if field not in data:
            errs.append(f"Missing required field: {field}")
    # check types (string only for this example)
    props = schema.get('properties', {})
    for k, v in props.items():
        if k in data:
            expected = v.get('type')
            if expected == 'string' and not isinstance(data[k], str):
                errs.append(f"Field {k} expected string, got {type(data[k]).__name__}")
            # simple format check for email
            if v.get('format') == 'email' and isinstance(data[k], str) and not is_email(data[k]):
                errs.append(f"Field {k} is not a valid email: {data[k]}")
    return errs

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 tests/validate_action.py <action-file.json>")
        sys.exit(2)
    action_path = sys.argv[1]
    with open(action_path, 'r', encoding='utf-8') as f:
        action = json.load(f)

    action_name = action.get('action')
    if not action_name:
        print("Action JSON must include top-level 'action' field.")
        sys.exit(2)

    schema_path = os.path.join('ops', 'tool-schemas', f"{action_name}.json")
    if not os.path.exists(schema_path):
        print(f"No schema found for action '{action_name}' at {schema_path}")
        sys.exit(2)

    with open(schema_path, 'r', encoding='utf-8') as f:
        schema = json.load(f)

    params = action.get('params', {})
    errors = []
    # try to use jsonschema if available
    try:
        import jsonschema
        validator = jsonschema.Draft7Validator(schema)
        for e in validator.iter_errors(params):
            errors.append(f"{e.message} (at {list(e.path)})")
    except Exception:
        # fallback lightweight validation
        errors.extend(lightweight_validate(schema, params))

    # confidence check
    conf = action.get('confidence', 0.0)
    if conf < 0.6:
        errors.append(f"Low confidence: {conf} < 0.6 (clarify instead of executing)")

    if 'explain' not in action or not isinstance(action.get('explain'), str) or not action.get('explain').strip():
        errors.append("Missing or empty 'explain' field (one-line rationale required)")

    if errors:
        print("VALIDATION FAILED:\n-----------------")
        for e in errors:
            print(" -", e)
        sys.exit(1)
    else:
        print("VALIDATION PASSED: action looks good to execute.")


if __name__ == '__main__':
    main()
