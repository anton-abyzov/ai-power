---
title: "Installing Claude Code"
timestamp: "10:11-16:03"
---

# Claude Code Setup

Following official docs: https://docs.anthropic.com/en/docs/claude-code/setup

## Installation Steps

1. **Install via NPM**
```bash
npm install -g @anthropic/claude-code
```

2. **Set API Key**
```bash
export ANTHROPIC_API_KEY=your_key_here
```

3. **Initialize Project**
```bash
claude-code init
```

## Understanding the Context Window

<div style="width: 100%; height: 600px; border: 1px solid #ddd; border-radius: 8px; overflow: hidden;">
<iframe src="../../diagrams/viewer.html#StLOY6fAw2MqVGdsakh51" width="100%" height="100%" frameborder="0"></iframe>
</div>

- 200K tokens = Your working memory
- System prompt (3.1k tokens)
- System tools (11.5k tokens)
- Your messages and code

## Key Commands
See claude-commands.md for full list → Next: Creating Your UI Agent