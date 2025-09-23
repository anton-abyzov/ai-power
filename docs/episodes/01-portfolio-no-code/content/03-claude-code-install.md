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

### Understanding the Context Window

<div style="width: 100%; max-width: 1200px; margin: 2rem auto; text-align: center;" data-testid="excalidraw-diagram">
<img src="../../diagrams/frames/essential-plugins.svg"
     alt="Essential Plugins"
     title="Essential Plugins"
     data-frame-id="StLOY6fAw2MqVGdsakh51"
     data-frame-name="Essential Plugins"
     style="width: 100%; height: auto; max-height: 600px; object-fit: contain; border: 1px solid #e1e4e8; border-radius: 8px; background: white;">
</div>

200K tokens = Your working memory
System prompt (3.1k tokens)
System tools (11.5k tokens)
Your messages and code

Key Commands
See claude-commands.md for full list
→ Next: Creating Your UI Agent