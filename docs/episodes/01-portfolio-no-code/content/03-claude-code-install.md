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

Set API Key

bashexport ANTHROPIC_API_KEY=your_key_here

Initialize Project

bashclaude-code init
Understanding the Context Window
Show Image
📊 View in Excalidraw - Frame 5

200K tokens = Your working memory
System prompt (3.1k tokens)
System tools (11.5k tokens)
Your messages and code

Key Commands
See claude-commands.md for full list
→ Next: Creating Your UI Agent