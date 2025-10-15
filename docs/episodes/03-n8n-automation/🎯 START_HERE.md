# 🎯 START HERE - Episode 03
## N8N Automation Superpowers with Sora 2 AI Videos

**Date:** October 12, 2025
**Sora 2 Released:** September 30, 2025
**Status:** Production Ready ✅

---

## 📺 WATCH THE VIDEO FIRST

**YouTube Link:** [Insert your video link here]

This tutorial shows you how to:
- Install N8N (cloud or self-hosted)
- Build your first automation workflow
- Integrate Claude Sonnet 4.5 AI via MCP
- Create SORA 2 video generation workflow
- Handle debugging & edge cases in production
- Save 20-40 hours per week
- Generate cinematic AI videos with Sora 2

**Duration:** 46 minutes 47 seconds
**Difficulty:** Intermediate to Advanced
**Prerequisites:** Basic programming knowledge, willingness to debug, API familiarity helpful
**Note:** This is a REAL build with actual debugging - not a polished demo!

---

## 🎯 WHAT YOU'LL BUILD

### 1. Simple Email → Slack Workflow
- Automatically notify team of urgent emails
- Filter by subject keywords
- Instant Slack notifications
- **Time to build:** 10 minutes

### 2. AI-Powered Support Workflow
- Customer emails → Claude analyzes → Draft reply
- Human approval step
- Automated response sending
- **Time to build:** 20 minutes

### 3. Content Generation Pipeline
- RSS feed monitoring
- Claude generates LinkedIn, Twitter, blog content
- Sora 2 video prompt generation
- Save to database, notify in Slack
- **Time to build:** 30 minutes

### 4. Generate Sora 2 Videos
- 15 viral video prompt ideas included
- Cinematic 16:9 footage at 1080p
- Perfect for YouTube, presentations, social media
- **Time to generate:** 2 hours (batch process)

**Total time investment:** 90 minutes setup
**Time saved per week:** 20-40 hours

---

## 📂 REPOSITORY STRUCTURE

```
episodes/03-n8n-automation/
├── 🎯 START_HERE.md                      ← You are here
├── 📹 THE_FULL_SCRIPT.md                 ← Complete video script
├── SORA_2_VIDEO_PROMPTS.md               ← 15 viral video ideas
│
├── prompts/
│   ├── n8n-automation-agent.md           ← Claude agent for N8N workflows
│   └── claude-workflow-prompts.md        ← Reusable Claude prompts
│
├── templates/
│   ├── workflow-email-to-slack.json      ← Import-ready N8N workflow
│   ├── workflow-ai-support.json          ← AI customer support
│   └── workflow-content-pipeline.json    ← Content automation
│
├── workspace/
│   ├── QUICK_START_GUIDE.md              ← 5-minute setup guide
│   ├── TROUBLESHOOTING.md                ← Common issues & fixes
│   └── examples/
│       ├── sample-email-filter.json
│       ├── sample-claude-prompt.md
│       └── sample-webhook-config.md
│
└── diagrams/
    ├── n8n-workflow-overview.excalidraw
    └── content-pipeline-flow.excalidraw
```

---

## 🚀 QUICK START (5 MINUTES)

### Step 1: Choose Your N8N Installation Method

**Option A: N8N Cloud (Easiest - 60 seconds)**

1. Visit: **https://n8n.cloud**
2. Click "Get Started Free"
3. Sign up with email or Google
4. Verify email
5. Log in to dashboard

**Pros:** No setup, automatic updates, secure
**Cons:** Monthly cost ($20 after free tier), data on their servers

---

**Option B: Standalone Local Install (Recommended for Tutorial - 5 minutes)**

**Requirements:**
- macOS, Linux, or Windows with WSL
- Node.js 18+ installed
- npm or pnpm package manager

**Install with npm (Global):**
```bash
# Install N8N globally
npm install -g n8n

# Start N8N
n8n start

# Access at: http://localhost:5678
```

**Install with pnpm (Faster):**
```bash
# Install pnpm if not installed
npm install -g pnpm

# Install N8N
pnpm install -g n8n

# Start N8N
n8n start
```

**What happens:**
- N8N installs to your system globally
- Data stored in: `~/.n8n` folder
- Access at: `http://localhost:5678`
- Runs on your machine (your data, your control)
- FREE forever

**Stop N8N:**
- Press `Ctrl + C` in terminal

**Restart N8N:**
```bash
n8n start
```

**Check if running:**
```bash
# Open browser to:
http://localhost:5678
```

**Pros:** Free, full control, no data sent to cloud, perfect for learning
**Cons:** Manual updates, must be running to work

---

**Option C: Docker (Advanced - 2 minutes)**

**Requirements:**
- Docker installed and running

```bash
docker run -d \
  --name n8n \
  -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n \
  n8nio/n8n

# Access at: http://localhost:5678
```

**Pros:** Isolated environment, easy to reset, portable
**Cons:** Requires Docker knowledge

---

**🎥 In This Tutorial:**
- I'm using **standalone local install** (Option B)
- It's free, fast, and perfect for learning
- You'll see my local N8N at `http://localhost:5678`
- Once comfortable, you can switch to cloud or Docker

---

### Step 2: Import First Workflow (2 minutes)

1. Click **"Add workflow"** → **"Import from File"**
2. Select: `templates/workflow-email-to-slack.json`
3. Click **"Import"**
4. Workflow appears on canvas

---

### Step 3: Connect Your Apps (2 minutes)

1. Click **Gmail node** → **"Create new credential"**
2. Follow OAuth flow → Grant permissions
3. Click **Slack node** → **"Create new credential"**
4. Grant Slack permissions
5. Select your channel (e.g., `#alerts`)

---

### Step 4: Test & Activate (1 minute)

1. Click **"Execute Workflow"** button
2. Send yourself a test email with "urgent" in subject
3. Watch workflow execute
4. Check Slack for notification
5. Toggle **"Active"** switch ON

**Done!** Your first workflow is live and running.

---

## 🔗 ESSENTIAL RESOURCES

### Official Documentation
- **N8N Docs:** https://docs.n8n.io
- **Sora 2 Guide:** https://platform.openai.com/docs/guides/video-generation
- **Claude API:** https://docs.anthropic.com/en/api/getting-started
- **MCP Protocol:** https://www.anthropic.com/news/model-context-protocol

### Tools You'll Need
- **N8N Cloud:** https://n8n.cloud (free tier available)
- **Sora 2 Access:** https://platform.openai.com/sora (requires OpenAI account)
- **Claude API Key:** https://console.anthropic.com (sign up for API access)
- **Gmail Account:** For email automation
- **Slack Workspace:** For notifications

### API Keys Required
- ✅ Anthropic API Key (Claude integration)
- ⚠️ OpenAI API Key (Sora 2 videos - optional)
- ⚠️ N8N Cloud account (or Docker for self-hosted)

---

## 📚 FILE GUIDE

### 📹 THE_FULL_SCRIPT.md
- **Complete 13-minute video script**
- Time-stamped sections
- Voiceover scripts
- Screen recording instructions
- Production notes
- **Read this for full understanding**

### SORA_2_VIDEO_PROMPTS.md
- **15 viral video ideas**
- Detailed prompts ready to use
- Cinematography guidance
- Aspect ratio recommendations
- Usage tips for each video
- **Use these to generate your B-roll**

### prompts/n8n-automation-agent.md
- **Claude agent definition**
- Helps build N8N workflows via chat
- Debugging assistance
- Optimization suggestions
- **Use with Claude Code or Claude.ai**

### templates/*.json
- **Ready-to-import N8N workflows**
- Just import and configure
- Fully documented nodes
- Best practices included
- **Fastest way to get started**

---

## 💡 LEARNING PATH

### Beginner (Week 1)
1. ✅ Sign up for N8N Cloud
2. ✅ Import email-to-Slack workflow
3. ✅ Test and activate
4. ✅ Understand nodes: Trigger → Filter → Action
5. ✅ Build second simple workflow (e.g., RSS → Slack)

### Intermediate (Week 2)
1. ✅ Add HTTP Request node (call external APIs)
2. ✅ Integrate Claude API for AI analysis
3. ✅ Build AI support workflow
4. ✅ Add Code node for custom JavaScript
5. ✅ Create multi-step workflows with branching

### Advanced (Week 3-4)
1. ✅ Build content generation pipeline
2. ✅ Parallel execution (multiple Claude calls)
3. ✅ Error handling and retries
4. ✅ Webhook triggers for external integrations
5. ✅ Self-host N8N with Docker (optional)

### Expert (Ongoing)
1. ✅ Create custom nodes (if needed)
2. ✅ Integrate MCP when production-ready
3. ✅ Build complex multi-tool workflows
4. ✅ Share templates with community
5. ✅ Automate your entire business

---

## 🎥 SORA 2 VIDEO GENERATION GUIDE

### ⚠️ CRITICAL: READ THIS FIRST

**Sora 2 Access Methods (Released September 30, 2025):**

1. **iOS App** (Available Now)
   - Download: "Sora by OpenAI" from App Store
   - Availability: US & Canada (expanding soon)
   - Pricing: Free with invite, ChatGPT Plus ($20/mo), or Pro ($200/mo)
   - Perfect for: Testing prompts, personal use

   **Plus vs Pro:**
   - **ChatGPT Plus ($20/mo):** Unlimited Sora access, 50 videos/month, priority during peak
   - **ChatGPT Pro ($200/mo):** 500 videos/month, faster generation, longer videos (20 sec), priority features
   - **Recommendation:** Plus for most users, Pro for businesses/serious creators

2. **Web Interface** (sora.com)
   - Works on any browser
   - Same pricing as iOS app
   - Easier for desktop workflow

3. **API Access** (For N8N Automation)
   - Status: **Invite-only** (Public launch: November 2025)
   - Requires: OpenAI API key + Organization verification
   - **EXPENSIVE** - Read pricing below before automating

   **Organization Verification Required:**
   - Can be individual person OR company
   - Upload government ID from 90+ supported countries
   - Accepted: Driver's license, passport, state ID
   - Verification time: 1-2 business days
   - Purpose: Prevent abuse, ensure accountability for high-cost API
   - Benefits: Higher rate limits, business features

4. **Android App**
   - Status: **Not available yet** (in development)
   - No release date announced

---

### 💰 SORA 2 PRICING (API) - KNOW BEFORE YOU BUILD

**Per-Second Pricing Model:**

| Quality | Cost/Second | 10-sec Video | 30-sec Video |
|---------|-------------|--------------|--------------|
| **Standard** | $0.10 | $1.00 | $3.00 |
| **Pro 720p** | $0.30 | $3.00 | $9.00 |
| **Pro HD 1080p** | $0.50 | $5.00 | $15.00 |

**Real Business Scenarios:**

**Scenario 1: Product Demo Videos**
- 100 products × 15 seconds × $0.50 (HD) = **$750 per batch**
- Monthly updates? **$750/month**

**Scenario 2: Daily Social Content**
- 10 videos/day × 10 seconds × $0.10 (Standard) = $10/day
- **$300/month minimum**

**Scenario 3: High-Volume Content**
- 50 videos/day × 15 seconds × $0.30 (720p) = $225/day
- **$6,750/month** 😱

---

### 🚨 MANDATORY WARNINGS

**1. API Key Security:**
- Never expose your OpenAI API key in public code
- Never commit API keys to GitHub
- One leaked key = unlimited charges to your account
- Use environment variables ONLY

**🎥 In the video:**
- I'll show you how to create an OpenAI API key
- I'll demonstrate proper N8N credential storage
- **IMPORTANT:** I will delete that API key immediately after recording
- You should NEVER share API keys publicly
- Treat API keys like passwords - they give full access to your account

**2. Company Authorization:**
- **REQUIRED:** Get written approval if using for business
- Costs escalate FAST with automation
- $1,000+ monthly bills are common
- Budget discussion with finance team before building

**3. Set Spending Limits:**
- **MUST DO:** Set hard cap in OpenAI billing
- Go to: https://platform.openai.com/settings/billing/limits
- Set maximum monthly spend
- Get alerts at 50%, 75%, 90%

**4. Test Before Automating:**
- Use iOS app or web UI to test prompts FIRST
- Get prompts perfect manually
- THEN automate with API
- This saves hundreds of dollars in failed generations

**5. For This Tutorial:**
- We're generating 5 videos (~20 seconds total)
- Cost: $2-10 depending on quality
- For B-roll/demonstration purposes only
- **Not production-scale automation**

---

### Is Sora 2 Worth It?

**High-Value Use Cases (YES):**
- Product demos worth $10,000+ in sales
- Marketing videos generating qualified leads
- Training content saving 100+ employee hours
- Brand videos replacing $5,000 production costs

**Bulk Content (MAYBE):**
- Social media clips: Consider templates instead
- Daily posting: Calculate ROI carefully
- High-volume needs: Static images may be cheaper

**Personal/Learning (START HERE):**
- Test with iOS app (free/included in Plus)
- Generate 5-10 videos to learn
- Then decide on API automation

---

### Step 1: Access Sora 2

**Recommended Path:**
1. Download iOS app OR visit sora.com
2. Sign up for ChatGPT Plus ($20/mo) if needed
3. Test prompts from `SORA_2_VIDEO_PROMPTS.md`
4. Refine until perfect
5. THEN consider API automation

**For API Access:**
1. Visit: https://platform.openai.com/sora
2. Check API availability status
3. Join waitlist if not yet invited
4. Set spending limits BEFORE first generation

---

### Step 2: Use Included Prompts

1. Open: `SORA_2_VIDEO_PROMPTS.md`
2. Choose a prompt (e.g., "Outer Space Piano")
3. Copy entire prompt
4. Paste into Sora 2 interface (iOS/Web)
5. Test and refine
6. Save successful prompts for API use

---

### Step 3: Configure Settings

- **Resolution:** 1080p (costs more but looks professional)
- **Aspect Ratio:** 16:9 (YouTube), 9:16 (Shorts), 1:1 (Instagram)
- **Duration:** 10-20 seconds (keep short to control costs)
- **Style:** Cinematic (default)

**Cost-Saving Tips:**
- Start with Standard quality ($0.10/sec)
- Use 5-10 second videos (not 20)
- Generate HD only for final versions
- Batch generate to minimize iterations

---

### Step 4: Generate & Download

**In iOS/Web UI:**
- Click "Generate"
- Wait 2-5 minutes for processing
- Download video in highest quality
- Use in your projects

**Via N8N API (Advanced):**
- Only after testing prompts manually
- Only after setting spending limits
- Only with company authorization
- Monitor costs closely

---

### Top 5 Recommended Prompts:
1. **Outer Space Piano** - Impossible scenario, visually stunning ($0.50 for 5-sec HD)
2. **Champions League Goal** - Universal appeal, high energy ($0.40 for 4-sec HD)
3. **Burj Khalifa Dive** - Mission Impossible vibes, adrenaline ($0.30 for 3-sec HD)
4. **Sam Altman Handshake** - Tech credibility, insider access ($0.40 for 4-sec HD)
5. **Everest Summit** - Ultimate achievement, inspirational ($0.50 for 5-sec HD)

**Total for 5 B-roll videos:** ~$2.10 (HD) or ~$0.42 (Standard)

---

## ⚡ COMMON USE CASES

### Email & Communication
- Urgent email → Team notification
- Support email → AI analysis → Draft reply
- Newsletter signup → Welcome sequence
- Meeting request → Auto-schedule → Send confirmation

### Content Creation
- Blog post → Summarize → Social posts (LinkedIn, Twitter)
- YouTube video → Transcribe → Blog article
- RSS feed → Content curation → Newsletter
- Podcast → AI summary → Show notes

### Data & CRM
- Form submission → Add to CRM → Notify team
- New customer → Onboarding email sequence
- Payment received → Update spreadsheet → Thank you email
- Survey response → Analyze → Store in database

### Social Media
- New content → Schedule posts across platforms
- Mention detected → Sentiment analysis → Reply
- Competitor post → Analyze → Alert team
- Trending topic → Generate comment → Post

### E-commerce
- New order → Update inventory → Send confirmation
- Abandoned cart → Reminder email sequence
- Product review → Analyze sentiment → Respond
- Low stock → Reorder alert → Purchase order

---

## 🐛 TROUBLESHOOTING

### Workflow Not Triggering
**Problem:** Workflow doesn't execute when expected
**Solutions:**
1. Check "Active" toggle is ON
2. Verify trigger node is configured correctly
3. Check execution logs: Click "Executions" tab
4. Test trigger manually: Click "Execute Workflow"
5. Check API rate limits (if using external APIs)

### Gmail/Slack Not Connecting
**Problem:** OAuth connection fails
**Solutions:**
1. Clear browser cookies and cache
2. Try incognito/private browsing mode
3. Ensure popup blockers are disabled
4. Re-authorize from N8N credentials page
5. Check Google/Slack admin settings

### Claude API Errors
**Problem:** Claude API returns errors or timeouts
**Solutions:**
1. Verify API key is correct: Check Anthropic console
2. Check API usage limits: May need to upgrade plan
3. Reduce token count in prompt
4. Add retry logic with "Retry On Fail" node setting
5. Check API status: https://status.anthropic.com

### Workflow Executes But No Output
**Problem:** Workflow runs but doesn't do what you expect
**Solutions:**
1. Check each node's output: Click node → View "Output" tab
2. Add "Set" node to debug: Display variables
3. Check filter conditions: May be too restrictive
4. Verify data format matches node expectations
5. Test with simpler data first

### Self-Hosted N8N Issues
**Problem:** Docker container won't start or crashes
**Solutions:**
1. Check Docker logs: `docker logs n8n`
2. Verify port 5678 isn't in use: `lsof -i :5678`
3. Update to latest N8N image: `docker pull n8nio/n8n`
4. Check disk space: N8N needs storage for data
5. Reset data: Remove `~/.n8n` folder (WARNING: Deletes workflows)

**Full troubleshooting guide:** See `workspace/TROUBLESHOOTING.md`

---

## 📊 SUCCESS METRICS

### Week 1 Goals
- [ ] N8N installed and running
- [ ] First workflow active
- [ ] Gmail and Slack connected
- [ ] At least 1 successful automation execution
- [ ] Understand basic node types

### Week 2 Goals
- [ ] 3+ workflows running
- [ ] Claude API integrated
- [ ] AI-powered workflow operational
- [ ] Custom JavaScript in Code node
- [ ] 5+ hours saved this week

### Month 1 Goals
- [ ] 10+ workflows active
- [ ] Content pipeline running
- [ ] 20+ hours saved per week
- [ ] Comfortable with N8N interface
- [ ] Contributing workflows to community

### Long-term Goals
- [ ] Business mostly automated
- [ ] 30-40 hours saved weekly
- [ ] Teaching others N8N
- [ ] Custom integrations built
- [ ] Exploring MCP integration

---

## 🤝 COMMUNITY & SUPPORT

### Get Help
- **N8N Forum:** https://community.n8n.io
- **Discord:** https://discord.gg/n8n (active community)
- **GitHub Issues:** https://github.com/n8n-io/n8n/issues
- **YouTube:** Search "N8N tutorial" for more examples
- **This Repo:** Open GitHub issue for questions

### Share Your Work
- Comment on YouTube video with your results
- Share workflows on N8N community forum
- Open PR to this repo with improvements
- Tag on Twitter: @antonabyzov @n8n_io
- Write blog post about your automation journey

### Stay Updated
- Subscribe to YouTube channel for Episode 4 (MCP integration)
- Star this GitHub repo for updates
- Follow N8N blog: https://blog.n8n.io
- Follow Anthropic for MCP news: https://anthropic.com/news

---

## 🎯 NEXT STEPS

### Right Now (5 minutes)
1. ✅ Read this START_HERE.md (you're doing it!)
2. ✅ Sign up for N8N Cloud: https://n8n.cloud
3. ✅ Open `📹 THE_FULL_SCRIPT.md` for detailed walkthrough

### Today (30 minutes)
1. ✅ Import first workflow template
2. ✅ Connect Gmail and Slack
3. ✅ Test email-to-Slack automation
4. ✅ Activate workflow

### This Week (2-3 hours)
1. ✅ Build AI support workflow
2. ✅ Get Claude API key
3. ✅ Test Claude integration
4. ✅ Build second custom workflow

### This Month (10-15 hours)
1. ✅ Build content pipeline
2. ✅ Generate Sora 2 videos
3. ✅ Create 10+ workflows
4. ✅ Measure time saved
5. ✅ Share results in YouTube comments

---

## 🚨 IMPORTANT NOTES

### MCP (Model Context Protocol)
- **Status:** Not production-ready as of October 2025
- **What is it:** Standard protocol for AI ↔ tool communication
- **When to use:** Wait for N8N native support (coming soon)
- **Current workaround:** Use HTTP webhooks (shown in video)
- **Episode 4 Preview:** Full MCP integration when stable

### Security Best Practices
- ✅ Store API keys in N8N credentials (encrypted)
- ✅ Use environment variables for sensitive data
- ✅ Enable 2FA on all connected accounts
- ✅ Review workflow permissions regularly
- ✅ Self-host for maximum data control

### Cost Considerations

**N8N:**
- **Cloud:** $20/month (5 workflows, 2,500 executions)
- **Self-Hosted:** FREE (Docker - only infrastructure costs)

**Claude API:**
- Input: $3 per 1M tokens
- Output: $15 per 1M tokens
- Typical support email analysis: ~$0.01

**Sora 2 API (EXPENSIVE):**
- Standard: $0.10/second ($1 for 10-sec video)
- Pro HD: $0.50/second ($5 for 10-sec video)
- **Monthly estimates:**
  - Light use (10 videos/month): $10-50
  - Medium use (100 videos/month): $100-500
  - Heavy use (1000 videos/month): $1,000-5,000

**Total Monthly Costs:**
- **Starter (learning):** $0 (self-hosted N8N + free tiers)
- **Small business:** $50-100 (N8N Cloud + Claude + light Sora 2)
- **Medium business:** $200-500 (includes automation + AI + moderate video)
- **Enterprise:** $1,000+ (high-volume video generation)

**⚠️ CRITICAL:** Set spending limits on OpenAI account BEFORE automating Sora 2

### Legal & Compliance
- Review terms of service for all connected tools
- Ensure GDPR/privacy compliance if handling user data
- Don't automate anything against platform ToS
- Get user consent for AI-generated communications
- Keep backups of critical workflows

---

## ✅ CHECKLIST: ARE YOU READY?

Before diving in, make sure you have:

**Accounts:**
- [ ] N8N Cloud account (or Docker installed)
- [ ] Gmail account
- [ ] Slack workspace
- [ ] Anthropic account (Claude API)
- [ ] OpenAI account (Sora 2 - optional)

**Tools:**
- [ ] Modern web browser (Chrome/Firefox/Edge)
- [ ] Text editor (VS Code recommended)
- [ ] Terminal access (for self-hosted)
- [ ] GitHub account (to access this repo)

**Knowledge:**
- [ ] Basic understanding of automation concepts
- [ ] Familiarity with APIs (helpful but not required)
- [ ] Comfortable following technical tutorials
- [ ] Willing to experiment and troubleshoot

**Mindset:**
- [ ] Ready to invest 2-3 hours learning
- [ ] Open to trying new tools
- [ ] Willing to iterate and improve
- [ ] Excited about saving 20-40 hours/week

**If you checked most boxes, you're ready! Let's build.**

---

## 🎬 FINAL WORDS

Automation isn't the future. It's now.

Someone is building these workflows today while you're reading.
They'll save 30 hours next week. You won't.

Same knowledge. Different action.

So stop reading. Start building.

Open N8N. Import a workflow. Test it. Activate it.

Then build workflow #2. Then #3.

In one month, your business runs itself.

**All the resources are here. The blueprint is complete.**

Now it's your turn.

Go build something incredible.

---

**Questions? Stuck? Found a bug?**
- Open GitHub issue: [repo-link]
- Comment on YouTube video: [video-link]
- Join N8N Discord: https://discord.gg/n8n

**Ready to start?**
👉 Next: Open `📹 THE_FULL_SCRIPT.md` for complete tutorial
👉 Or: Jump to `templates/` and import your first workflow

**Let's automate your life. Right now.** 🚀
