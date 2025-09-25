# Episode 02: AI-Powered Resume Fine-Tuner with Claude Code

## 🎬 Video Script (10 minutes - HIGH ENERGY)

---

### 🔥 HOOK (0:00-0:30)
**[Scene: Split screen - One developer manually editing resumes, another using AI]**

"You won't be replaced by AI. But you WILL be replaced by someone using AI to do YOUR job faster and better."

**[Screen: Inbox flooding with 50+ recruiter messages]**

"Watch how to turn ANY resume into the PERFECT match for ANY job - in 2 minutes. Works for developers, marketers, project managers - anyone."

**[Quick montage: Different resumes transforming - Software Engineer → .NET Expert, Marketing Manager → Growth Hacker, PM → Agile Coach]**

"2-hour task. 2 minutes. Let's go."

---

### 📊 THE PROBLEM (0:30-1:00)
**[Screen: Show experience spread - Developer with 10 skills, Marketer with 15 campaigns, PM with 20 projects]**

"Your experience is broad. Job descriptions are specific."

**[Show Excalidraw diagram: Broad Experience vs Focused JDs]**
![[Broad vs Focused.excalidraw]]

"Generic resume = ignored. Tailored resume = interview. But who has time to customize for EVERY opportunity?"

**[Screen: Scroll through LinkedIn showing 50+ unread messages]**

"The opportunities are EVERYWHERE - remote, high-paying, waiting. You just need the right approach."

---

### 🚀 CLAUDE CODE AGENTS (1:00-2:00)
**[Screen: Claude Code interface]**

"Claude Code agents - AI assistants that follow YOUR exact instructions."

**[Show Excalidraw: Agent Architecture Diagram]**
![[Agent workflow.excalidraw]]

"Feed it your ENTIRE career once. It tailors PERFECT resumes forever."

**[Quick examples on screen]**
"Works for:
- Developers: Python → ML Engineer, Java → Backend Architect
- Marketers: Content → SEO Specialist, Growth → Performance Marketer
- PMs: Agile → Scrum Master, Product → Strategy Lead"
- ... many more

**[Reference badge: "New to Claude Code? Episode 01 in description"]**

---

### 🏗️ QUICK SETUP (2:00-2:30)
**[Terminal commands on screen]**

"Skip permission prompts - add to .zshrc:"

```bash
function claude() {
  command claude --dangerously-skip-permissions "$@"
}
source ~/.zshrc
```

"Organize your workspace:"

```bash
mkdir -p resumes/{templates,outputs,job-descriptions}
```

**[File structure visual]**
"Three folders. That's it. Templates, outputs, job descriptions."

---

### 🤖 CREATE YOUR AGENT (2:30-4:00)
**[Screen: Agent configuration file]**

"The setup - 30 seconds:"

```yaml
name: resume-fine-tuner
description: Tailors resumes to job descriptions
tools: Read, Write, Grep, Glob
```

"The magic - your COMPLETE experience database:"

```yaml
experience:
  - company: Tech Company
    period: 2023-Present
    technologies: [Azure, .NET 8, Kafka, Kubernetes]
    achievements:
      - Built platform for 20M+ users
      - Improved performance by 25%

  # For Marketers:
  - campaigns: Q4 Product Launch
    metrics: 150% ROI, 10K leads
    channels: [Google, Meta, LinkedIn]

  # For PMs:
  - product: Mobile Banking App
    users: 500K active
    methodology: Scrum, SAFe
```

**[Key point on screen]**
"Realistic metrics = Believable resume. 25% improvement ✓ | 10x performance ✗"

---

### 📝 YOUR EXPERIENCE DATABASE (4:00-4:30)
**[Screen: Experience structure]**

"Structure EVERYTHING - the AI needs data:"

```markdown
## For Developers:
- Tech Stack: [List ALL technologies]
- Scale: Users, transactions, data
- Results: Performance gains, cost savings

## For Marketers:
- Campaigns: Names, budgets, channels
- Metrics: CTR, CAC, LTV, ROI
- Tools: CRM, analytics, automation

## For PMs:
- Products: Names, users, revenue
- Methods: Agile, Scrum, SAFe
- Results: Launch times, adoption rates
```

**[Show Excalidraw: Experience Mapping Matrix]**
![[]]
"More detail = Better matches. Feed it everything."

---

### 🎯 LIVE DEMO (4:30-6:30)
**[Screen: Real job description from inbox]**

"Real job. Real demo. Watch this:"

```
Senior Full Stack Developer – Healthcare
- Python, React, PostgreSQL
- HIPAA compliance
- 7+ years required
```

**[Terminal command]**
```bash
claude "resume-fine-tuner: Healthcare Full Stack role [paste JD]"
```

**[Show 3-step process visualization]**
"1. EXTRACT: Python, React, Healthcare, HIPAA
2. MATCH: Pulls YOUR healthcare projects
3. GENERATE: Perfect resume in 30 seconds"

**[Split screen: Generic vs Tailored resume]**

"Before: Generic Python developer
After: Healthcare-focused full stack expert with HIPAA experience

Time: 30 seconds. Response rate: 3x higher."

**[Examples for other roles]**
"Marketing Manager → Growth Marketing Lead: 45 seconds
Project Manager → Agile Coach: 35 seconds
Data Analyst → Business Intelligence Expert: 40 seconds"

---

### 💡 PRO TIPS (6:30-7:00)
**[Screen: File naming system]**

"Track everything:"
```
microsoft_dotnet_2024-01.docx → Interview ✓
google_ml_2024-01.docx → Offer ✓
```

**[Show Excalidraw: Multiple Resume Versions Strategy]**

"Build your arsenal:
- Technical version (for engineers)
- Leadership version (for managers)
- Startup version (move fast)
- Enterprise version (process-focused)"

"Reuse winners. Track what works."

---

### 🎨 OUTPUT FORMATS (7:00-7:30)
**[Screen: Format conversions]**

"Any format you need:"

```bash
# PDF: pandoc resume.md -o resume.pdf
# Word: Already generates .docx
# Web: Push to GitHub Pages
```

"ATS-friendly. Human-readable. Professional."

---

### 📈 RESULTS (7:30-8:30)
**[Screen: Success metrics animation]**

"The numbers don't lie:
- 15% → 45% response rate
- 2 hours → 2 minutes per application
- 5 interviews → 20+ interviews monthly"

**[Excalidraw: Do's and Don'ts diagram]**

"DO: Realistic metrics, varied language, save winners
DON'T: Fake skills, 10x claims, robotic text"

**[Testimonial cards]**
"Developer: 3 offers in 2 weeks
Marketer: Doubled salary in 3 months
PM: Remote role at FAANG"

---

### 🔍 FIND OPPORTUNITIES (8:30-9:00)
**[Screen: Platform logos]**

"Where to look:
- LinkedIn: Set 'Open to Work' → 50+ messages weekly
- AngelList: Startups with equity
- Dice/Indeed: Volume play
- Your spam folder: Hidden gems!"

**[Security alert]**
"⚠️ PHISHING WARNING: Fake job sites steal credentials. ONLY apply through official channels."

### 🎬 CLOSING (9:00-10:00)
**[Screen: Split view - Manual vs AI-powered job seeker]**

"Two paths:
1. Keep doing it manually. Get left behind.
2. Use AI. Get ahead. NOW."

**[GitHub repo on screen]**
"github.com/anton-abyzov/ai-power
Complete code. Ready to use. FREE."

**[Final message, bold text]**
"You have 2 choices:
Watch others use AI to take your opportunities.
Or BE the one taking them.

Your move."

**[End screen]**
- SUBSCRIBE (big, centered)
- Episode 01: Portfolio Builder (card)
- GitHub: anton-abyzov/ai-power (link)

---

## 🎥 Production Notes

### Required Screen Recordings:
1. Inbox with recruiter messages
2. Claude Code agent creation
3. Live resume generation demo
4. File organization system
5. Multiple output formats

### Excalidraw Diagrams (5 Total - Perfect for 10 min):
1. Broad Experience vs Focused JDs (0:45)
2. Agent Architecture Workflow (1:15)
3. Experience Mapping Matrix (4:20)
4. Multiple Resume Versions Strategy (6:40)
5. Do's and Don'ts Checklist (7:45)

### B-Roll Suggestions:
- Typing on mechanical keyboard
- Multiple monitors with different JDs
- Success notifications (interview invites)
- PDF resume outputs
- GitHub stars increasing

### Voiceover Energy:
- Confident and practical
- Emphasize time savings
- Real experience, not theory
- Conversational, not preachy

---

## 📊 Estimated Timeline:
- **Total Duration**: 10 minutes SHARP
- **Editing Time**: 3-4 hours (fast cuts)
- **Recording Time**: 1-2 hours (high energy takes)
- **Thumbnail Creation**: 30 minutes
- **Upload & SEO**: 30 minutes

## 🔗 Links to Include:
- GitHub Repo: github.com/yourusername/ai-power
- Episode 01: Previous portfolio video
- Claude Code Docs: docs.claude.com/claude-code
- Overleaf (optional mention): overleaf.com
- Discord Community: your-discord-link

## 🏷️ YouTube Tags:
- claude code
- ai resume builder
- resume optimization
- developer resume
- tailored resume
- job application automation
- claude agents
- ai powered tools
- remote work
- software engineer resume
- .NET developer
- cloud architect resume
- resume fine tuning
- job search automation
- tech career