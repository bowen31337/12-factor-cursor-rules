# 12-Factor Agents — Cursor Rules

This repository contains Cursor project rules (.mdc files) adapted from the "12-Factor Agents" guide.
Place the `.cursor/rules/` directory into your project root so Cursor can load these rules.

Structure:
```
.cursor/
  rules/
    00_index.mdc
    01_intent-to-tool.mdc
    ...
    12_stateless-reducer.mdc
```

Usage:
1. Copy the `.cursor/rules/` folder to your repository root.
2. Restart Cursor if rules don't appear immediately.
3. Optionally add `/ops/tool-schemas/*.json` and reference them in `04_structured-tools.mdc`.
