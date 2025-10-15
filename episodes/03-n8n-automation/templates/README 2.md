# N8N Workflow Templates

Import-ready JSON workflow files for common automation patterns.

## 📥 HOW TO IMPORT

1. Open N8N dashboard
2. Click "Add Workflow" → "Import from File"
3. Select JSON file from this folder
4. Configure credentials (Gmail, Slack, etc.)
5. Test workflow
6. Activate

## 📋 AVAILABLE TEMPLATES

### 1. workflow-email-to-slack.json
**Description:** Monitors Gmail for urgent emails and posts to Slack
**Nodes:** Gmail Trigger → Filter → Slack Post
**Setup Time:** 5 minutes
**Credentials Needed:** Gmail, Slack

**Use Case:**
- Never miss urgent emails
- Team notification for critical messages
- Filter by subject keywords

---

### 2. workflow-ai-support.json
**Description:** AI-powered customer support with human approval
**Nodes:** Gmail Trigger → Claude API → Slack Review → Wait → Gmail Send
**Setup Time:** 15 minutes
**Credentials Needed:** Gmail, Slack, Anthropic API

**Use Case:**
- Auto-draft support responses
- Human-in-the-loop for quality
- Sentiment analysis
- Faster response times

---

### 3. workflow-content-pipeline.json
**Description:** Automated content generation from RSS feeds
**Nodes:** RSS Trigger → Fetch → 5× Claude API (parallel) → Airtable → Slack
**Setup Time:** 20 minutes
**Credentials Needed:** Anthropic API, Airtable, Slack

**Outputs Generated:**
- LinkedIn post
- Twitter thread
- Blog draft
- Short summary
- Sora 2 video prompt

**Use Case:**
- Content marketing automation
- Multi-platform distribution
- Consistent posting schedule

---

## 🛠️ WORKFLOW STRUCTURE EXAMPLES

### Simple Email → Slack
```json
{
  "name": "Email to Slack Notification",
  "nodes": [
    {
      "type": "n8n-nodes-base.gmailTrigger",
      "parameters": {
        "event": "messageReceived",
        "filters": {
          "subject": "urgent"
        }
      }
    },
    {
      "type": "n8n-nodes-base.slack",
      "parameters": {
        "channel": "#alerts",
        "text": "🚨 Urgent email from {{ $json.from }}"
      }
    }
  ]
}
```

### AI Support Workflow
```json
{
  "name": "AI Customer Support",
  "nodes": [
    {
      "type": "n8n-nodes-base.gmailTrigger",
      "parameters": {
        "event": "messageReceived",
        "filters": {
          "to": "support@example.com"
        }
      }
    },
    {
      "type": "n8n-nodes-base.httpRequest",
      "parameters": {
        "url": "https://api.anthropic.com/v1/messages",
        "method": "POST",
        "body": {
          "model": "claude-sonnet-4-5-20250929",
          "messages": [{
            "role": "user",
            "content": "Analyze this support email and draft a reply: {{ $json.body }}"
          }]
        }
      }
    },
    {
      "type": "n8n-nodes-base.slack",
      "parameters": {
        "channel": "#support-review",
        "text": "New ticket - AI draft ready"
      }
    }
  ]
}
```

---

## ⚙️ CONFIGURATION NOTES

### Gmail Trigger
- **OAuth Setup:** Follow N8N's Gmail OAuth flow
- **Polling Interval:** Default 5 minutes (adjustable)
- **Filters:** Subject, from, to, label
- **Output:** Email object with subject, body, from, attachments

### Slack Node
- **OAuth Setup:** Install N8N app to your workspace
- **Channel Selection:** Public or private channels
- **Message Formatting:** Supports Markdown and Slack blocks
- **Output:** Message timestamp, channel ID

### Claude API (HTTP Request)
- **Authentication:** Bearer token in headers
- **Model:** claude-sonnet-4-5-20250929 (recommended)
- **Max Tokens:** 1024-4096 (depending on task)
- **Output:** JSON with content array

### Airtable Node
- **API Key:** Generate from Airtable account settings
- **Base ID:** Found in Airtable URL
- **Table Name:** Exact match required
- **Output:** Record ID, created time

---

## 🚨 COMMON ISSUES

### "Authentication failed"
- **Gmail:** Reconnect OAuth, check Gmail API enabled
- **Slack:** Reinstall N8N app, verify bot permissions
- **Claude:** Check API key, verify account has credits

### "Workflow not triggering"
- **Check Active Toggle:** Must be ON
- **Verify Polling Interval:** May need to wait
- **Check Filters:** Too restrictive?
- **Test Manually:** Click "Execute Workflow"

### "Node execution error"
- **Check Previous Node Output:** Data format may be wrong
- **Validate JSON:** Use Code node to inspect data
- **Add Error Trigger Node:** Catch and handle errors
- **Review Logs:** Click "Executions" tab

---

## 📚 LEARN MORE

- **N8N Documentation:** https://docs.n8n.io
- **N8N Community:** https://community.n8n.io
- **Claude API Docs:** https://docs.anthropic.com
- **YouTube Tutorial:** [Link to Episode 03 video]

---

## 🤝 CONTRIBUTE

Found a better way to structure a workflow? Open a PR!

1. Fork this repo
2. Create your workflow in N8N
3. Export as JSON
4. Add to this folder with README description
5. Submit PR

Let's build the automation library together.

---

**NOTE:** Actual JSON files will be added after video production. For now, use the workflow builder instructions in the main script and START_HERE.md to create these workflows manually.

**Coming Soon:**
- workflow-social-media-scheduler.json
- workflow-data-sync-airtable-notion.json
- workflow-lead-enrichment.json
- workflow-invoice-automation.json
- workflow-report-generation.json
