---
title: "Understanding Claude Code Agents"
timestamp: "1:30-3:00"
---

# Claude Code Agents: Your AI Team Members

## What Are Claude Code Agents?

Claude Code agents are specialized AI assistants that follow your specific instructions and domain knowledge. Think of them as expert team members who:
- **Understand** your specific context
- **Follow** your exact processes
- **Remember** your preferences
- **Execute** complex tasks autonomously

## How Agents Differ from Regular Claude

### Regular Claude Code
```bash
claude "Write a Python function to sort a list"
```
- General purpose
- No specialized knowledge
- Starts fresh each time

### With Custom Agents
```bash
claude "Use the resume-fine-tuner agent to optimize for this Microsoft role"
```
- Domain-specific expertise
- Knows YOUR career history
- Follows YOUR resume strategy
- Consistent output format

## The Power of Specialized Agents

In Episode 01, we created a UI/UX agent for portfolio building. Today's resume agent is even more powerful because it:

### 1. Maintains Your Complete Experience
```yaml
experience_database:
  - 18 years of projects
  - Technologies mastered
  - Quantifiable achievements
  - Team sizes and budgets
  - Client names and industries
```

### 2. Understands Resume Best Practices
- ATS optimization
- Keyword density
- Natural language variety
- Realistic metrics
- Industry standards

### 3. Adapts to Different Markets
- **US Style**: No photo, emphasis on achievements
- **European Style**: More detailed, may include photo
- **Academic**: Publications and research focus
- **Startup vs Enterprise**: Different emphasis

## Agent Architecture

```yaml
name: resume-fine-tuner
description: Optimizes resumes for specific roles
tools: [Read, Write, Grep, Glob]
capabilities:
  - Parse job descriptions
  - Extract key requirements
  - Match to your experience
  - Reorganize content
  - Generate multiple formats
```

## Reference: Claude Code Documentation

For detailed agent creation, see the official docs:
[docs.claude.com/claude-code/sub-agents](https://docs.claude.com/en/docs/claude-code/sub-agents)

Key concepts:
- **Arguments**: Pass job descriptions as input
- **Tools**: Access to file operations
- **Context**: Your experience database
- **Output**: Structured resume content

## Why This Approach Works

### 1. Consistency at Scale
- Same quality for application #1 or #100
- No fatigue or shortcuts
- Maintains your voice

### 2. Speed Without Sacrifice
- 2 minutes vs 2 hours
- Higher quality than rushed manual edits
- Time for what matters: preparation

### 3. Continuous Improvement
- Learn from successful applications
- Refine agent instructions
- Build pattern library

---

<div class="navigation-footer">
  <div>
    <a href="../01-the-problem/">
      <div>← Previous</div>
      <div>The Problem</div>
    </a>
  </div>
  <div style="text-align: right;">
    <a href="../03-workspace-setup/">
      <div>Next →</div>
      <div>Workspace Setup</div>
    </a>
  </div>
</div>