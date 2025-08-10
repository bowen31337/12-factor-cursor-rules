# 12-Factor Cursor Rules v3

A comprehensive implementation of the **12-Factor Agents** methodology for Cursor AI, featuring structured tool schemas, validation systems, and best practices for AI agent development.

## 🎯 Overview

This project implements a systematic approach to building reliable, maintainable, and scalable AI agents using the 12-Factor methodology adapted for Cursor AI development. It provides a robust foundation for creating AI agents that follow industry best practices.

## 🏗️ Architecture

The project follows the **12-Factor Agents** methodology:

1. **Intent-to-Tool** - Clear mapping between user intent and tool execution
2. **Prompts** - Modular, versioned prompt management
3. **Context Window** - Efficient context management and retrieval
4. **Structured Tools** - JSON Schema validation for all tool invocations
5. **State** - Canonical state management with audit logging
6. **Lifecycle** - Explicit control flow with START/PAUSE/RESUME/CANCEL
7. **Human-in-Loop** - Structured human review and approval workflows
8. **Control Flow** - Deterministic orchestration with explicit branching
9. **Error Handling** - Comprehensive error management with retry logic
10. **Small Agents** - Single-purpose agents composed via orchestrator
11. **Triggers** - Normalized trigger handling with validation
12. **Stateless Reducer** - Pure, testable state transitions

## 📁 Project Structure

```
12-factor-cursor-rules-v3/
├── ops/
│   └── tool-schemas/          # JSON Schema definitions for tools
│       └── send_email.json    # Email tool schema
├── tests/
│   ├── validate_action.py     # Action validation script
│   ├── sample_action_valid.json
│   ├── sample_action_invalid.json
│   └── README.md
└── README.md
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- Cursor AI

### Installation

1. Clone the repository:
```bash
git clone https://github.com/bowen31337/12-factor-cursor-rules-v3.git
cd 12-factor-cursor-rules-v3
```

2. Install dependencies:
```bash
pip install jsonschema
```

### Validation

Test action validation with the provided examples:

```bash
# Test valid action
python3 tests/validate_action.py tests/sample_action_valid.json

# Test invalid action
python3 tests/validate_action.py tests/sample_action_invalid.json
```

## 🔧 Tool Schema System

All tools must have machine-readable JSON Schema definitions stored in `/ops/tool-schemas/<tool>.json`. The validation system ensures:

- **Type Safety**: All parameters conform to defined schemas
- **Required Fields**: Validation of mandatory parameters
- **Format Validation**: Email, URL, and custom format checking
- **Confidence Thresholds**: Minimum confidence levels for execution
- **Explanation Requirements**: Rationale for all actions

### Example Tool Schema

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "send_email",
  "type": "object",
  "properties": {
    "to": {
      "type": "string",
      "format": "email"
    },
    "subject": {
      "type": "string"
    },
    "body": {
      "type": "string"
    }
  },
  "required": ["to", "subject", "body"],
  "additionalProperties": false
}
```

### Example Action Object

```json
{
  "action": "send_email",
  "params": {
    "to": "user@example.com",
    "subject": "Welcome to 12-Factor Agents",
    "body": "Thank you for implementing best practices!"
  },
  "confidence": 0.95,
  "explain": "Send welcome email to new user with high confidence"
}
```

## 🧪 Testing

The project includes a comprehensive validation system:

- **Schema Validation**: JSON Schema compliance checking
- **Confidence Thresholds**: Minimum 0.6 confidence required
- **Explanation Validation**: Required rationale for all actions
- **Type Checking**: Runtime type validation
- **Format Validation**: Email, URL, and custom format validation

### Running Tests

```bash
# Validate a single action file
python3 tests/validate_action.py path/to/action.json

# The script will:
# 1. Load the action file
# 2. Lookup the corresponding schema
# 3. Validate parameters against the schema
# 4. Check confidence and explanation requirements
```

## 📋 Best Practices

### 1. Structured Actions
Always use the canonical action format:
```json
{
  "action": "tool_name",
  "params": { /* tool-specific parameters */ },
  "confidence": 0.0,
  "explain": "one-line rationale"
}
```

### 2. Confidence Thresholds
- **< 0.6**: Ask clarifying questions instead of executing
- **≥ 0.6**: Safe to execute with proper validation
- **≥ 0.9**: High confidence, minimal risk

### 3. Error Handling
Use compact JSON error format:
```json
{
  "code": "VALIDATION_ERROR",
  "summary": "Invalid email format",
  "retryable": true,
  "details": "Email must be valid format"
}
```

### 4. State Management
Maintain canonical state object:
```json
{
  "run_id": "unique-identifier",
  "step": "current_step",
  "prev_state_hash": "hash-of-previous-state",
  "outputs": [],
  "metadata": {}
}
```

## 🔄 Lifecycle Management

The system supports explicit control flow:

- **START**: Initialize new run
- **PAUSE**: Persist state and surface pause reason
- **RESUME**: Verify state hash and show context diff
- **CANCEL**: Abort current run
- **REPLAY**: Replay previous run

## 🤝 Human-in-Loop

For actions requiring human consent:
```json
{
  "action": "human_review",
  "params": {
    "review_id": "unique-review-id",
    "prompt": "Review this action",
    "options": ["approve", "modify", "reject"],
    "deadline": "2024-01-01T00:00:00Z"
  }
}
```

## 📈 Benefits

- **Reliability**: Structured validation prevents runtime errors
- **Maintainability**: Clear separation of concerns and modular design
- **Scalability**: Deterministic orchestration and state management
- **Auditability**: Complete audit trail of all actions
- **Testability**: Pure functions and comprehensive test coverage
- **Human Oversight**: Built-in human review workflows

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Guidelines

- Follow the 12-Factor Agents methodology
- Add JSON Schema for all new tools
- Include comprehensive tests
- Update documentation for new features
- Maintain backward compatibility

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Inspired by the [12-Factor App](https://12factor.net/) methodology
- Built for the Cursor AI development community
- Designed for enterprise-grade AI agent development

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/bowen31337/12-factor-cursor-rules-v3/issues)
- **Discussions**: [GitHub Discussions](https://github.com/bowen31337/12-factor-cursor-rules-v3/discussions)
- **Documentation**: [Wiki](https://github.com/bowen31337/12-factor-cursor-rules-v3/wiki)

---

**Built with ❤️ for the AI development community**
