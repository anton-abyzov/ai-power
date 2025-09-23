---
title: "Installing Claude"
timestamp: "10:11-16:03"
---

# Claude Setup

Following official docs: https://docs.anthropic.com/en/docs/claude/setup

## Installation Steps

1. **Install via NPM**
```bash
npm install -g @anthropic/claude
```

2. **Set API Key**
```bash
export ANTHROPIC_API_KEY=your_key_here
```

3. **Initialize Project**
```bash
claude init
```

### Understanding the Context Window

![[episodes/01-portfolio-no-code/diagrams/all-diagrams.excalidraw.md#^frame=StLOY6fAw2MqVGdsakh51]]

200K tokens = Your working memory
System prompt (3.1k tokens)
System tools (11.5k tokens)
Your messages and code

## Key Commands
See claude-commands.md for full list
→ Next: Creating Your UI Agent