---
title: "Claude CLI Commands"
---

# Claude CLI Commands Reference

## Essential Commands

### Basic Operations
```bash
# Initialize a new Claude project
claude init

# Start interactive session
claude

# Run a single command
claude "explain this code"

# Work with files
claude "analyze main.py"
```

### Working with Agents
```bash
# Create a new agent
claude agent create ui-expert

# Use a specific agent
claude --agent ui-expert "create landing page"

# List available agents
claude agent list
```

### Project Management
```bash
# Save conversation context
claude save

# Load previous context
claude load

# Clear context
claude clear
```

### Advanced Features
```bash
# Use with specific model
claude --model claude-3-opus "complex task"

# Set max tokens
claude --max-tokens 4000 "generate documentation"

# Stream responses
claude --stream "explain architecture"
```

## Useful Shortcuts

| Command | Description |
|---------|-------------|
| `Ctrl+C` | Cancel current operation |
| `Ctrl+D` | Exit Claude session |
| `/help` | Show help in session |
| `/clear` | Clear conversation |
| `/save` | Save current context |

## Configuration

Your Claude configuration is stored in `.claude/config.json`:

```json
{
  "api_key": "YOUR_API_KEY",
  "default_model": "claude-3-opus",
  "max_tokens": 4000,
  "temperature": 0.7
}
```

## Tips

- Use agents for specialized tasks to get better results
- Save your context regularly when working on complex projects
- Stream responses for long-running tasks
- Use `--verbose` flag for debugging

---

[← Back to Claude Setup](03-claude-code-install.md) | [Next: Agent Creation →](04-agent-creation.md)