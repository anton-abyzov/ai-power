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

![Context Window](../diagrams/frames/frame-5.svg)

200K tokens = Your working memory
System prompt (3.1k tokens)
System tools (11.5k tokens)
Your messages and code

## Key Commands

The most common Claude commands you'll use:

```bash
# Start Claude in your project
claude

# Create an agent
claude agent create ui-expert

# Use an agent for a task
claude --agent ui-expert "build portfolio site"
```

[View Full Command Reference →](claude-commands.md)

---

<div class="navigation-footer" style="display: flex; justify-content: space-between; margin-top: 3rem; padding: 2rem 0; border-top: 1px solid #e0e0e0;">
  <div>
    <a href="../content/02-ai-tools-landscape/" style="text-decoration: none;">
      <div style="color: #666; font-size: 0.9rem;">← Previous</div>
      <div style="color: #7c4dff; font-weight: 600;">AI Tools Landscape</div>
    </a>
  </div>
  <div style="text-align: right;">
    <a href="../content/04-agent-creation/" style="text-decoration: none;">
      <div style="color: #666; font-size: 0.9rem;">Next →</div>
      <div style="color: #7c4dff; font-weight: 600;">Agent Creation</div>
    </a>
  </div>
</div>