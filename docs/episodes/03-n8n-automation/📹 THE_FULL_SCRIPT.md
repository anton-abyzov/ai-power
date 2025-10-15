# 📹 THE FULL SCRIPT - Episode 03
## N8N + SORA 2 Automation: The ACTUAL Recording

**Published:** October 15, 2025
**Video Duration:** 46 minutes 47 seconds
**YouTube:** https://youtu.be/c7xZb556RkI
**Format:** Live build with real debugging

---

## ⚠️ IMPORTANT NOTE

This document describes what was ACTUALLY recorded, not what was originally planned.

The original script was for an 18-minute polished tutorial. The actual recording became a 46-minute real build session with:
- Live debugging
- API errors
- Policy violations
- Workflow rearrangements
- Discovery of API limitations
- Unscripted problem-solving

**For the complete verbatim transcript:** See [📄 FULL_TRANSCRIPT.txt](📄%20FULL_TRANSCRIPT.txt)
**For exact timestamps:** See [⏰ TIMESTAMPS.md](⏰%20TIMESTAMPS.md)

---

## 📊 VIDEO STRUCTURE (ACTUAL)

### Total Duration: 46:47
### Segments: 558 (from Whisper transcription)
### Chapters: 50 (YouTube timestamps)

### High-Level Breakdown:

| Section | Time | Duration | Description |
|---------|------|----------|-------------|
| **Introduction** | 00:00-02:06 | 2:06 | SORA 2 demos, automation benefits, access methods |
| **SORA 2 Overview** | 02:06-15:08 | 13:02 | Pricing, iOS/Web walkthrough, cameo feature, policy handling |
| **N8N Introduction** | 15:08-19:27 | 4:19 | What is N8N, installation options, local setup |
| **Building Workflow** | 19:27-42:18 | 22:51 | Form trigger, SORA API, Discord, debugging, testing |
| **N8NMCP Integration** | 42:18-46:27 | 4:09 | MCP setup, Claude workflow generation, testing |

---

## 🎬 SECTION 1: INTRODUCTION & DEMOS
**[00:00] - [02:06]** | **Duration: 2:06**

### What Happens:

**[00:00-00:21]** AI-generated SORA 2 video demos shown
- Carnegie Hall performance
- Champions League goal
- Mission Impossible stunts
- "Everything you just saw, built with AI"

**[00:21-00:37]** Value proposition
- "In less than 30 minutes, you'll know exactly how"
- SORA 2 introduction, released September 30, 2025
- Why it matters for business

**[00:44-02:01]** Automation capabilities mentioned
- Resume fine-tuning (from Episode 02)
- Lead management
- LinkedIn data automation
- AI customer support
- Content creation
- N8N + SORA 2 API integration

**[02:01-02:06]** Transition to pricing discussion

### Key Quotes:

> "Everything you just saw, built with AI. In less than 30 minutes, you'll know exactly how."

> "Last week I saved 40 hours. This is my resume fine tuning automation."

---

## 🎬 SECTION 2: SORA 2 DEEP DIVE
**[02:06] - [15:08]** | **Duration: 13:02**

### Part A: Access Methods & Pricing [02:06-05:17]

**Three ways to access SORA 2:**

1. **iOS mobile application** [02:06]
   - Download from App Store
   - Perfect for testing prompts

2. **Web platform** [02:12]
   - Login with ChatGPT credentials
   - Access at platform.openai.com
   - Works in any browser

3. **API for automation** [02:38]
   - Requires organization verification
   - Driver's license or state-issued ID
   - 90-day reverification if rejected
   - **EXPENSIVE:** $0.10-$0.50 per second

**API Cost Breakdown [03:24]:**
- $5 for 10-second HD video
- $50 for 100 seconds
- Hundreds per month for business automation

**ChatGPT Plans [03:53]:**
- **Plus ($20/mo):** 30 videos/24 hours, up to 10 seconds, watermark
- **Pro ($200/mo):** 500 videos/month, up to 20 seconds, no watermark

### Part B: iOS/Web App Walkthrough [05:17-15:08]

**[05:17]** Mobile app demonstration starts
- Download "Sora AI" from App Store
- US & Canada only (VPN workaround mentioned)

**[05:59]** Connectivity issue discovered
- iPhone recording via QuickTime causes internet issues
- Switched to web version at sora.gpt.com

**[06:18]** Web interface tour
- Instagram/TikTok-like feed
- Community videos and trending prompts
- Like, follow, remix features

**[07:40]** Profile page features
- Posts, Cameos, Likes sections
- Drafts (unpublished work)

**[08:27]** Creating first video
- Prompt: "Sam Altman welcomes Anton Abyzov as new CTO of OpenAI"
- Image upload feature
- Orientation settings (portrait/landscape)
- Video generation queue

**[10:44]** Generation issues
- 3-5 minute wait time
- Policy violation handling
- Page refresh needed

**[12:05]** Handling violations [IMPORTANT]
- "May violate our guard rails around potential fraudulent or scam activity"
- Solution: Use ChatGPT/Claude to rewrite prompt
- Remove specific person names
- Make prompt generic

**[14:21]** Successful generation
- Final video shown
- Remix feature demonstrated

**[14:34]** Invite codes giveaway
- First 5 commenters with workflow ideas get SORA access

---

## 🎬 SECTION 3: N8N INTRODUCTION
**[15:08] - [19:27]** | **Duration: 4:19**

### What is N8N? [15:08]

**Core Concept:**
- Fair code workflow automation
- Like Zapier or Make.com but self-hosted
- Your data, your server
- No limits: unlimited workflows, unlimited executions
- Open source, FREE forever
- Code when needed (JavaScript)

**Visual workflow builder** [15:50]
- For SecOps, DevOps, many other workflows
- 400+ integrations (Gmail, Discord, Obsidian, Google Sheets, Claude AI, OpenAI)

**Key Philosophy:**
"If it has an API, N8N connects to it."

### Three Installation Methods [16:51]

**1. Local Environment** [16:54]
- What Anton uses in the video
- Free, simple, perfect for learning

**2. Remote Machine/VM** [16:57]
- Hostinger or other VM services
- Paid service (~$10/month)

**3. N8N Cloud** [17:09]
- Create username
- Start trial
- Standard paid service ($20/month)

### Local Installation Walkthrough [17:18]

**Command shown:**
```bash
npx n8n
```

**Issue encountered:** [17:40]
- Node.js version too old
- Need version 22+

**Solution:** [17:48]
- Visit nodejs.org
- Download version 22.20
- Use NVM (Node Version Manager)

**NVM commands shown:** [18:05]
```bash
nvm ls           # List installed versions
nvm use 22       # Switch to version 22
npx n8n          # Start N8N
```

**Success:** [18:25]
- N8N starts on localhost:5678
- First-time setup screen shown

**Auto-start setup mentioned** [18:43]
- Command available on request (in comments)

### Cost Comparison [18:59]

- **Local:** FREE (only needs Node.js)
- **N8N Cloud:** $20/month starter plan
- **Hostinger:** ~$10/month (Black Friday discounts)

**Huge savings with self-hosted approach!**

---

## 🎬 SECTION 4: BUILDING THE WORKFLOW
**[19:27] - [42:18]** | **Duration: 22:51**

This is the CORE of the video - building the SORA 2 automation workflow with real debugging.

### Workflow Overview [19:27]

**Goal:** Generate AI videos with SORA 2 on demand

**Flow:**
1. Manual trigger OR form submission
2. Enter video prompt
3. OpenAI API generates video
4. Discord notification when ready

### Building the Workflow (Detailed Steps)

For complete step-by-step breakdown with exact timestamps, see the transcript sections:

**[19:27-20:06]** Form Submission Trigger setup
**[21:05-23:26]** SORA 2 API Documentation review
**[23:26-27:31]** HTTP POST Request configuration
**[27:31-28:35]** Conditional logic and video retrieval
**[28:35-30:51]** Form input improvements (orientation, duration)
**[30:51-33:30]** Discord webhook integration

### 🐛 REAL DEBUGGING MOMENTS

#### [31:01] Debugging #1: Rearranging Broken Workflow
**Problem:** Nodes connected incorrectly after adding Discord
**Solution:** Remove and reconnect in proper order
**Lesson:** N8N visual layout matters for execution flow

#### [36:42] Debugging #2: Infinite Loop Bug
**Problem:** Workflow loops forever on failed videos
**Solution:** Add explicit "failed" status check before looping
**Lesson:** Always handle failure states, not just success

#### [39:32] Debugging #3: Cameo API Blocking [CRITICAL DISCOVERY]
**Problem:** Human face references blocked via API (but work in iOS/Web)
**Solution:** Use generic descriptions without names
**Lesson:** API has stricter moderation than UI apps

**Quote from video:**
> "It took me some time to understand that actually OpenAI API blocks human face references. It means cameo via API equals moderation blocked."

#### [40:26] Debugging #4: Discord Formatting
**Problem:** Complex prompts break Discord message formatting
**Solution:** Send simple metadata instead of full prompt
**Lesson:** Sanitize data before external API calls

### Production Testing [34:01-42:18]

**[34:07]** Complex prompt prepared
- Deep sea diver scene
- Structured by time segments
- Professional atmospheric video

**[35:31]** Production URL testing
- Simple prompt: "Sam Altman welcomes Anton Abyzov in Tesla office"
- Status: Failed (policy violation)

**[39:43]** Modified prompt without names
- "Professional deep sea diver" instead of person names
- Landscape orientation, 12-second maximum duration

**[41:16]** Successful result
- 12-second video generated
- Professional deep sea diver exactly as specified
- "Oh wow, this is insane" [41:44]

---

## 🎬 SECTION 5: N8NMCP INTEGRATION
**[42:18] - [46:05]** | **Duration: 3:47**

### What is N8NMCP? [42:18]

**N8N Model Context Protocol**
- Lets Claude control N8N workflows
- Generate workflows using natural language
- Available on GitHub

### Installation & Configuration [42:36]

**Steps shown:**
1. Go to N8NMCP GitHub repository
2. Copy Claude Desktop configuration
3. Edit Claude Desktop settings (Developer → Edit Config)
4. Paste N8NMCP configuration
5. Restart Claude Desktop

### Testing N8NMCP [44:06]

**Test prompt:**
> "Build a workflow that sends Discord test diagnostic message on manual trigger"

**Claude generates:**
- JSON workflow definition
- Manual trigger node
- Discord message node
- Pre-configured structure

**Import and test:**
- Save JSON to file
- Import into N8N
- Test execution

**[45:43] Issue discovered:**
- Claude included undefined variables
- Remove dynamic variables
- Execute again - Success!

**[46:05] Result:**
> "We've just leveraged N8NMCP server to generate a new workflow. This is truly insane."

---

## 🎬 SECTION 6: CLOSING
**[46:05] - [46:47]** | **Duration: 0:42**

### Final Message

> "Real results, real time saved. This is not productivity. This is life-changing."

> "You build a system that worked for you. This is the future."

### B-Roll Visuals [46:27]

- Ocean/wave footage
- Dramatic closing shots

### Call to Action [46:40]

> "Coming in hot, subscribe, like, and comment below your next idea. Make some noise."

---

## 📊 KEY LEARNINGS FROM ACTUAL RECORDING

### What Viewers Actually Saw:

1. **Real debugging** - 4 major issues fixed live
2. **API limitations discovered** - Cameo blocking via API
3. **Cost considerations** - Emphasized throughout
4. **Iteration process** - Multiple attempts shown
5. **Production workflow** - From test to working solution

### Debugging Summary:

| Issue | Timestamp | Problem | Solution |
|-------|-----------|---------|----------|
| #1 | [31:01] | Broken connections | Rearrange nodes |
| #2 | [36:42] | Infinite loop | Add failed status check |
| #3 | [39:32] | Cameo API blocking | Generic descriptions |
| #4 | [40:26] | Discord formatting | Simplify messages |

---

## 🎯 WHAT MAKES THIS VALUABLE

### Why This Format Works:

1. **Authenticity** - Shows reality, not perfection
2. **Educational** - Learning from errors
3. **Relatable** - Everyone hits bugs
4. **Memorable** - "Cameo API = blocked" sticks
5. **Practical** - Saves viewers time by showing what doesn't work

### Key Differences from Plan:

| Planned | Actual |
|---------|--------|
| 18 minutes | 46:47 minutes |
| Polished demo | Real debugging |
| Perfect workflow | 4 major fixes |
| Scripted | Unscripted discoveries |
| Theory-focused | Problem-solving focused |

---

## 📁 RELATED FILES

- **[📄 FULL_TRANSCRIPT.txt](📄%20FULL_TRANSCRIPT.txt)** - Complete 558-segment verbatim transcript
- **[⏰ TIMESTAMPS.md](⏰%20TIMESTAMPS.md)** - 50 YouTube chapters with timestamps
- **[🎯 START_HERE.md](🎯%20START_HERE.md)** - Quick start guide
- **[SORA_2_VIDEO_PROMPTS.md](SORA_2_VIDEO_PROMPTS.md)** - Example prompts

---

## 📺 VIDEO METADATA

**Title:** I Spent 48 Hours Automating SORA 2 - Here's What ACTUALLY Works

**Duration:** 46:47

**Description:** See POSTING-STRATEGY-OCT-15-2025.md for full YouTube description

**Tags:** sora 2, n8n, automation, ai video generation, workflow automation, debugging, real tutorial

**Category:** Science & Technology

**Audience:** Developers, automation enthusiasts, AI early adopters

**Skill Level:** Intermediate to Advanced

---

**This was the REAL recording. No script followed. Just building, debugging, and learning live.**

**That's what makes it valuable.** 🚀
