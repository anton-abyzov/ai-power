# ⏰ TIMESTAMPS - Episode 03: N8N + SORA 2 Automation

**Video Duration:** 46:47
**Segments:** 558
**Generated:** October 15, 2025

---

## 📺 YOUTUBE CHAPTERS (Copy-paste ready)

```
[00:00] Introduction - SORA 2 AI Video Demos
[00:21] What You Can Build with AI Automation  
[00:37] SORA 2 Overview & Why It Matters
[00:44] Real-World Automation Examples
[01:43] N8N + SORA 2 Integration Power
[02:01] Pricing & Access Requirements
[02:06] Method 1: iOS Mobile Application
[02:38] Method 2: Web Platform
[03:02] Method 3: API for Automation
[03:24] API Pricing Deep Dive
[03:53] ChatGPT Plus vs Pro Comparison
[05:17] SORA 2 iOS/Web App Walkthrough
[07:40] Profile Page & Cameo Features
[08:27] Creating Your First Video
[10:44] Video Generation & Troubleshooting
[12:05] Handling Violations & Policy Issues
[14:21] Final Video Result & Engagement
[15:08] N8N Introduction - What & Why
[15:50] Visual Workflow Builder
[16:51] Three Ways to Install N8N
[17:09] N8N Cloud Setup
[17:18] Local Install (Recommended)
[18:43] Auto-Start Configuration
[19:14] First Workflow - Manual Trigger
[19:27] Building SORA 2 Automation Workflow
[20:06] Form Submission Trigger
[21:05] SORA 2 API Documentation
[22:07] API Authentication Setup
[23:21] Organization Verification
[23:26] Building the Complete Flow
[26:11] Video Metadata & Status
[27:31] Conditional Logic & Loops
[29:23] Landscape Orientation Settings
[30:51] Discord Webhook Integration
[31:01] DEBUGGING: Rearranging Broken Workflow
[33:08] Prompt Structure & Parameters
[34:01] Testing Complete Workflow
[35:31] Form Submission & Production URL
[38:12] Production Flow Improvements
[39:32] Cameo API Limitation Discovery
[40:40] Discord Message Formatting Fix
[41:37] Final Result - 12 Second Video
[42:18] N8NMCP Server Integration
[44:06] Building Workflow with Claude Desktop
[44:36] Importing Generated Workflow
[45:32] Testing MCP-Generated Workflow
[46:05] MCP Success & Final Thoughts
[46:27] Conclusion & Call to Action
```

---

## 🎯 CHAPTER DESCRIPTIONS

### Part 1: SORA 2 Introduction (00:00 - 15:08)

**[00:00] Introduction - SORA 2 AI Video Demos**
- Soccer/sports AI-generated footage
- Hook: "Everything you just saw, built with AI"

**[00:21] What You Can Build with AI Automation**
- Resume fine-tuning automation
- Lead management, CRM enrichment
- AI customer support, content creation

**[00:37] SORA 2 Overview & Why It Matters**  
- Released September 30, 2025
- Business value proposition
- Integration with N8N

**[02:01] Pricing & Access Requirements**
- Three access methods overview
- Organization verification requirements
- Cost structure preview

**[02:06] Method 1: iOS Mobile Application**
- App Store download
- Perfect for testing prompts
- US & Canada availability (VPN workaround)

**[02:38] Method 2: Web Platform**
- Browser-based access (sora.gpt.com)
- Same features as iOS
- Performance considerations

**[03:02] Method 3: API for Automation**
- API platform login
- Organization verification required
- Driver's license or state-issued ID

**[03:24] API Pricing Deep Dive**
- $0.10/second (Standard) to $0.50/second (HD)
- Business automation cost examples
- Spending limit recommendations

**[03:53] ChatGPT Plus vs Pro Comparison**
- Plus: $20/mo, 50 videos/month, 10-second max
- Pro: $200/mo, 500 videos/month, 20-second max
- Watermark differences

**[05:17] SORA 2 iOS/Web App Walkthrough**
- Main feed, community videos
- Trending prompts, remix functionality
- Instagram/TikTok-like interface

**[07:40] Profile Page & Cameo Features**
- Posts, drafts, likes sections
- Cameo personalized video creation
- Face upload process

**[08:27] Creating Your First Video**
- Sam Altman handshake prompt example
- Image upload functionality
- Orientation settings (portrait/landscape)

**[10:44] Video Generation & Troubleshooting**
- 3-5 minute processing time
- Page refresh issues
- Draft review process

**[12:05] Handling Violations & Policy Issues**
- Content moderation challenges
- Using AI to fix prompts (ChatGPT/Claude)
- Resubmission strategies

**[14:21] Final Video Result & Engagement**
- Successful video showcase
- Invite code giveaway (first 5 comments)
- Sharing functionality (incognito mode)

---

### Part 2: N8N Setup & Installation (15:08 - 19:27)

**[15:08] N8N Introduction - What & Why**
- Fair-code workflow automation
- vs Zapier/Make.com comparison
- Self-hosted advantages

**[15:50] Visual Workflow Builder**
- 400+ integrations
- Gmail, Discord, Obsidian, Claude AI
- No-code/low-code approach

**[16:51] Three Ways to Install N8N**
- Local environment (free)
- Remote machine/Hostinger (paid)
- N8N Cloud (paid)

**[17:09] N8N Cloud Setup**
- Account creation
- Standard trial process

**[17:18] Local Install (Recommended)**
- npx n8n command
- Node.js version requirements (v22+)
- localhost:5678 access

**[18:43] Auto-Start Configuration**
- Terminal command setup
- Cost comparison: $0 vs $20/mo cloud

**[19:14] First Workflow - Manual Trigger**
- Create workflow button
- Manual trigger setup
- Basic workflow concepts

---

### Part 3: Building SORA 2 Workflow (19:27 - 31:01)

**[19:27] Building SORA 2 Automation Workflow**
- Goal: AI video generation on demand
- Manual trigger → Prompt → API → Discord notification

**[20:06] Form Submission Trigger**
- Removing manual trigger
- Form creation: title, text area
- Prompt input field setup

**[21:05] SORA 2 API Documentation**
- Official docs navigation
- Create video endpoint
- Request/response structure

**[22:07] API Authentication Setup**
- OpenAI API key creation
- Bearer token configuration
- Credentials storage in N8N

**[23:21] Organization Verification**
- Driver's license upload requirement
- Verification for company or individual
- General settings tab

**[23:26] Building the Complete Flow**
- POST request to create video
- 60-second wait node
- GET request to check status

**[26:11] Video Metadata & Status**
- Video ID retrieval
- Completed/in-progress/failed states
- Duration, size, and other metadata

**[27:31] Conditional Logic & Loops**
- IF condition: status = "completed"
- False branch → wait → retry
- True branch → get video content

**[29:23] Landscape Orientation Settings**
- Form field additions
- Portrait vs landscape options
- Duration parameter (4/8/12 seconds)

**[30:51] Discord Webhook Integration**
- Discord server setup
- Creating text channel
- Webhook URL configuration

**[31:01] DEBUGGING: Rearranging Broken Workflow**
- Connection issues
- Parallel message sending
- Node rearrangement

---

### Part 4: Testing & Production (31:01 - 42:18)

**[33:08] Prompt Structure & Parameters**
- JSON properties from POST response
- Prompt, video ID, status, size, seconds
- Form data mapping

**[34:01] Testing Complete Workflow**
- Deep sea diver prompt (3-part structure)
- Orientation: landscape, duration: 12 seconds
- Test vs production URL difference

**[35:31] Form Submission & Production URL**
- Activating workflow
- Production URL access
- Test execution vs live execution

**[38:12] Production Flow Improvements**
- Naming workflow nodes
- Clearing execution history
- Status checking improvements

**[39:32] Cameo API Limitation Discovery**
- Human face references blocked via API
- Cameo ≠ API access
- Modifying prompt to remove names

**[40:40] Discord Message Formatting Fix**
- Special character errors
- Simplifying message content
- Timestamp-only approach

**[41:37] Final Result - 12 Second Video**
- Successful execution
- Discord notification review
- Video quality showcase

---

### Part 5: MCP Integration (42:18 - 46:47)

**[42:18] N8NMCP Server Integration**
- Model Context Protocol introduction
- Claude controlling N8N workflows
- GitHub installation guide

**[44:06] Building Workflow with Claude Desktop**
- Config file setup (developer settings)
- Prompt: "Build workflow that sends Discord test message"
- JSON workflow generation

**[44:36] Importing Generated Workflow**
- Saving JSON to file
- Import from file option
- Workflow visualization

**[45:32] Testing MCP-Generated Workflow**
- Manual trigger execution
- Discord message error
- Fixing undefined variables

**[46:05] MCP Success & Final Thoughts**
- Working Discord notification
- "Real results, real time saved"
- "This is life-changing"

**[46:27] Conclusion & Call to Action**
- Subscribe, like, comment
- Soccer footage outro
- "Make some noise"

---

## 🎬 KEY MOMENTS

### Most Valuable Timestamps

**For Beginners:**
- [15:08] N8N introduction
- [17:18] Local installation guide
- [20:06] First form trigger

**For API Integration:**
- [21:05] SORA 2 API docs
- [22:07] Authentication setup
- [23:26] Complete workflow build

**For Debugging:**
- [31:01] Workflow rearrangement
- [39:32] Cameo API limitation
- [40:40] Discord formatting fix

**For Advanced Users:**
- [42:18] MCP server integration
- [44:06] Claude-generated workflows
- [46:05] MCP success demonstration

---

## 📝 NOTES FOR VIDEO DESCRIPTION

**Full timestamp list formatted for YouTube description:**
- Copy the chapter list above (starting with [00:00])
- Paste directly into YouTube description
- YouTube will auto-create chapters

**Important:**
- First timestamp MUST be [00:00]
- Minimum 3 chapters required
- Each chapter must be at least 10 seconds

**Generated by:** OpenAI Whisper (base model)
**Transcription accuracy:** ~95%
**Manual review:** Recommended for final publication

---

