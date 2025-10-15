# 🎯 START HERE - Episode 03
## N8N + SORA 2 Automation: Build a Real Video Generation Workflow

**Date:** October 12, 2025
**Sora 2 Released:** September 30, 2025
**Status:** Production Ready ✅
**Video Duration:** 46 minutes 47 seconds

---

## 📺 WATCH THE VIDEO

**YouTube Link:** https://youtu.be/c7xZb556RkI

### What You'll See in This Video

This is a **REAL build with actual debugging** - not a polished demo!

You'll watch me:
- **Install N8N locally** (free, self-hosted)
- **Access SORA 2** on iOS, Web, and API
- **Build ONE complete workflow** from scratch: Form → SORA 2 API → Discord notifications
- **Debug real errors** including policy violations, infinite loops, and API failures
- **Discover limitations** like cameo blocking via API
- **Fix broken workflows** live on camera
- **Integrate N8NMCP** with Claude Desktop

**Duration:** 46:47
**Difficulty:** Intermediate to Advanced
**Prerequisites:** Basic programming knowledge, willingness to debug
**Note:** This shows the REAL work - bugs, edge cases, and all!

---

## 🎯 WHAT YOU'LL BUILD

### SORA 2 Video Generation Workflow

**The ONE workflow built in this video:**

```
User Form Submission
       ↓
   (Prompt, Orientation, Duration)
       ↓
   HTTP POST to SORA 2 API
       ↓
   Discord: "Video generation started"
       ↓
   Wait 60 seconds
       ↓
   Get Video Status
       ↓
   Is Status = "completed"?
   ├─ NO → Is Status = "failed"?
   │        ├─ YES → Discord: "Generation failed"
   │        └─ NO → Loop back to Wait
   └─ YES → Get Video Content
            ↓
        Discord: "Video ready!" + metadata
```

**What it does:**
- Accepts video prompts via web form
- Generates videos automatically with SORA 2 API
- Handles completion, failure, and in-progress states
- Sends Discord notifications at each step
- Supports landscape/portrait orientation
- Configurable video duration (4, 8, 12 seconds)

**Real debugging covered:**
- [31:01] Rearranging broken workflow connections
- [36:42] Handling "failed" status from API
- [38:00] Fixing infinite loop in wait logic
- [39:38] Discovering cameo API blocks human faces
- [40:26] Discord message formatting errors

**Time to build:** ~90 minutes (with debugging)
**API cost per video:** $0.40-$1.20 for 4-12 second videos

---

## 📂 WHAT'S IN THIS REPOSITORY

```
episodes/03-n8n-automation/
├── 🎯 START_HERE.md                      ← You are here
├── 📹 THE_FULL_SCRIPT.md                 ← Detailed video breakdown
├── ⏰ TIMESTAMPS.md                      ← 50 YouTube chapters
├── 📄 FULL_TRANSCRIPT.txt                ← Complete transcript (558 segments)
├── SORA_2_VIDEO_PROMPTS.md               ← Example video prompts
│
├── prompts/
│   ├── n8n-automation-agent.md           ← N8N workflow assistant
│   └── claude-workflow-prompts.md        ← Reusable prompts
│
└── templates/
    └── README.md                          ← Template info
```

**Note:** No pre-built workflow JSON files. You'll build it from scratch in the video!

---

## 🚀 QUICK START

### Step 1: Access SORA 2 (Choose Your Method)

**Method 1: iOS App** (Easiest for testing)
- Download "Sora by OpenAI" from App Store
- Available in US & Canada (VPN works for others)
- Requires invite OR ChatGPT Plus ($20/mo)

**Method 2: Web Interface** (Shown in video)
- Visit: https://sora.gpt.com
- Same features as iOS
- Works in any browser

**Method 3: API** (For automation - shown in video)
- Requires OpenAI API key
- Organization verification required (driver's license, 1-2 days)
- **EXPENSIVE:** $0.10-$0.50 per second of video
- Set spending limits BEFORE using!

**ChatGPT Pricing Options:**
- **Plus ($20/mo):** 30 videos/day, up to 10 seconds, has watermark
- **Pro ($200/mo):** 500 videos/month, up to 20 seconds, no watermark

---

### Step 2: Install N8N Locally (Free)

**What I use in the video:**

```bash
# Install Node.js 22+ first (if needed)
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.1/install.sh | bash
nvm install 22
nvm use 22

# Install and run N8N
npx n8n

# Access at: http://localhost:5678
```

**First time:**
- Create username and password
- Start building workflows

**Alternative options:**
- N8N Cloud: $20/month (easier, no setup)
- Docker: `docker run -p 5678:5678 n8nio/n8n`

---

### Step 3: Build the Workflow (Follow Video)

**Key workflow sections shown:**

1. **[19:27] Form submission trigger** - Create input form for prompts
2. **[23:26] HTTP POST to SORA 2 API** - Send video generation request
3. **[24:30] Wait node** - Pause while video generates
4. **[24:46] Get video status** - Check if completed/failed/in-progress
5. **[27:31] If conditions** - Branch logic for different statuses
6. **[27:48] Get video content** - Retrieve generated video
7. **[30:51] Discord webhooks** - Notifications at each step

**Debugging moments you'll see:**
- [31:01] Fixing broken connections
- [36:42] Handling failed videos
- [38:06] Fixing infinite loops
- [39:38] API cameo limitation discovered
- [40:40] Discord message formatting

---

### Step 4: Test with Real Prompts

**Example from video ([34:07]):**

```
[0-3 seconds] Extreme close-up of professional dive helmet with LED lights
[3-6 seconds] Camera pulls back revealing professional deep sea diving suit
[6-9 seconds] Wide shot showing diver suspended in deep ocean void
[9-12 seconds] Camera orbits showing diver ascending slowly

Technical: Professional atmospheric video, cinematic lighting
Branding: Subtle "EasyChamp" watermark
```

**Simpler version that works:**

```
Professional deep sea diver in full diving suit, suspended in deep ocean,
surrounded by darkness, LED helmet lights glowing, camera slowly orbiting,
cinematic underwater photography, 4K quality
```

**Critical lesson from video:** Don't use cameo/human face references via API - they get blocked by moderation!

---

## 💰 SORA 2 PRICING - KNOW BEFORE YOU BUILD

**API Pricing (Per Second):**
- Standard quality: $0.10/second
- Pro 720p: $0.30/second
- HD 1080p: $0.50/second

**Real costs from video:**
- 4-second test video: $0.40 (standard)
- 12-second production video: $1.20-$6.00 (depending on quality)

**Monthly scenarios:**
- 10 videos/day × 10 seconds = $300/month
- 50 videos/day × 15 seconds = $6,750/month

**🚨 CRITICAL:** Set spending limits at https://platform.openai.com/settings/billing/limits

---

## 🔧 N8N BASICS (From Video)

**What is N8N?** ([15:08])
- Fair code workflow automation
- Like Zapier but self-hosted
- Your data, your server
- FREE forever (self-hosted)
- 400+ integrations
- Visual workflow builder

**Three ways to install:** ([16:51])
1. **Local** (what I use) - FREE, npm/npx
2. **Docker** - Isolated, portable
3. **N8N Cloud** - $20/month, no setup

**Key concepts shown:**
- **Nodes:** Individual steps (HTTP Request, Wait, If, Discord)
- **Triggers:** What starts the workflow (Manual, Form, Webhook)
- **Connections:** How nodes pass data
- **Credentials:** Secure API key storage
- **Executions:** Workflow run history

---

## 🐛 REAL DEBUGGING FROM VIDEO

### Issue 1: Policy Violation ([12:50])
**Problem:** Video request rejected for "potential fraud/scam"
**Solution:** Remove specific person names, use generic descriptions
**Lesson:** SORA blocks brand names and public figures

### Issue 2: Infinite Loop ([36:42])
**Problem:** Workflow keeps waiting forever, never completes
**Solution:** Add "failed" status check before looping back to wait
**Lesson:** Always handle failure states, not just success

### Issue 3: Cameo API Blocking ([39:32])
**Problem:** API blocks human face references (cameo) even with verification
**Solution:** Use generic descriptions ("professional diver" instead of "Anton Abyzov")
**Lesson:** Cameo via API = moderation blocked

### Issue 4: Discord Formatting ([40:26])
**Problem:** Complex prompts break Discord message formatting
**Solution:** Send simple metadata instead of full prompt text
**Lesson:** Sanitize data before sending to external APIs

---

## 🤖 N8NMCP INTEGRATION ([42:18])

**What is N8NMCP?**
- Model Context Protocol server for N8N
- Lets Claude Desktop control N8N workflows
- Generate workflows with natural language

**Setup steps shown:**
1. Install N8NMCP from GitHub
2. Add to Claude Desktop config
3. Restart Claude Desktop
4. Ask Claude: "Build a workflow that sends Discord test message on manual trigger"
5. Import generated JSON into N8N
6. Test and fix any issues

**Result:** Working workflow generated by Claude in seconds!

---

## 📊 WHAT YOU'LL LEARN

### Technical Skills
- ✅ N8N installation and configuration
- ✅ HTTP API integration (SORA 2)
- ✅ OAuth setup (Discord webhooks)
- ✅ Conditional logic (If nodes)
- ✅ Loop handling (Wait + status checks)
- ✅ Error handling (failed states)
- ✅ Form triggers (user input)
- ✅ JSON data mapping

### Real-World Skills
- ✅ Debugging production workflows
- ✅ Handling API failures gracefully
- ✅ Cost management (API spending)
- ✅ Security (API key storage)
- ✅ User experience (Discord notifications)
- ✅ Edge case handling (policy violations)

---

## ⚡ KEY TAKEAWAYS

1. **Automation isn't theory** - You'll see real bugs and fixes
2. **APIs fail** - Build error handling from the start
3. **Costs add up fast** - SORA 2 API is expensive, test carefully
4. **Human faces are blocked via API** - Use generic descriptions
5. **Discord is perfect for notifications** - Simple, reliable, instant
6. **N8N is powerful** - Visual workflows beat code for most tasks
7. **N8NMCP is the future** - Generate workflows with Claude

---

## 🔗 ESSENTIAL RESOURCES

### Documentation
- **N8N Docs:** https://docs.n8n.io
- **SORA 2 API:** https://platform.openai.com/docs/guides/video-generation
- **N8NMCP GitHub:** https://github.com/n8n-io/n8n-mcp

### Tools You'll Need
- **N8N:** https://n8n.io (local install) or https://n8n.cloud
- **SORA 2:** https://sora.gpt.com or iOS app
- **OpenAI API:** https://platform.openai.com (for automation)
- **Discord:** https://discord.com (for notifications)

### Community
- **Discord Server:** https://discord.gg/UYg4BGJ65V
- **YouTube Channel:** https://youtube.com/@antonabyzov
- **GitHub Repo:** https://github.com/anton-abyzov/ai-power

---

## 🎯 NEXT STEPS

### Right Now (5 minutes)
1. ✅ Watch the video: https://youtu.be/c7xZb556RkI
2. ✅ Download SORA 2 iOS app OR visit sora.gpt.com
3. ✅ Sign up for ChatGPT Plus ($20/mo) if you want to test SORA 2

### Today (2 hours)
1. ✅ Install N8N locally (`npx n8n`)
2. ✅ Create OpenAI API key
3. ✅ Set spending limits on OpenAI account
4. ✅ Create Discord webhook
5. ✅ Follow video to build the workflow

### This Week (5 hours)
1. ✅ Test with 5-10 different prompts
2. ✅ Understand all edge cases shown in video
3. ✅ Customize workflow for your use case
4. ✅ Install N8NMCP and test Claude integration
5. ✅ Share your results in Discord

---

## 🚨 CRITICAL WARNINGS

### API Key Security
- Never expose OpenAI API keys in public code
- Never commit keys to GitHub
- Use N8N credentials system (encrypted)
- One leaked key = unlimited charges

### Cost Management
- Set hard spending limits BEFORE testing
- Test prompts in iOS/Web app first (cheaper)
- Start with 4-second videos (cheaper)
- Monitor OpenAI dashboard daily

### Organization Verification
- Required for SORA 2 API access
- Upload government ID (driver's license works)
- Takes 1-2 business days
- Without verification = no API access

### Cameo Limitation
- Human face references blocked via API
- Works in iOS/Web app
- Doesn't work in API automation
- Use generic descriptions instead

---

## ✅ CHECKLIST: ARE YOU READY?

**Before starting:**
- [ ] Node.js 18+ installed
- [ ] OpenAI account created
- [ ] OpenAI organization verified (for API)
- [ ] Discord account and server
- [ ] 2-3 hours of focused time
- [ ] Willingness to debug and iterate

**After completing:**
- [ ] N8N running locally
- [ ] SORA 2 workflow functional
- [ ] Discord notifications working
- [ ] Tested with 3+ prompts
- [ ] Understand all debugging moments
- [ ] N8NMCP installed and tested

---

## 🎬 FINAL WORDS

This isn't a perfect tutorial. It's a REAL build.

You'll see me:
- Make mistakes
- Debug live
- Discover limitations
- Rearrange workflows
- Fix formatting issues
- Learn as I go

**That's the point.**

Real automation has bugs. Real APIs fail. Real workflows need iteration.

If you want a polished demo, this isn't it.

If you want to learn how automation ACTUALLY works - including the messy parts - this is for you.

**46 minutes of real work. No shortcuts. No hiding mistakes.**

Let's build.

---

**Questions?**
- 💬 Discord: https://discord.gg/UYg4BGJ65V
- 📧 YouTube Comments: https://youtu.be/c7xZb556RkI
- 🐙 GitHub Issues: https://github.com/anton-abyzov/ai-power

**Ready to start?**
👉 Watch the video: https://youtu.be/c7xZb556RkI
👉 Read the script: [📹 THE_FULL_SCRIPT.md](📹%20THE_FULL_SCRIPT.md)
👉 See timestamps: [⏰ TIMESTAMPS.md](⏰%20TIMESTAMPS.md)

**Let's automate SORA 2.** 🚀
