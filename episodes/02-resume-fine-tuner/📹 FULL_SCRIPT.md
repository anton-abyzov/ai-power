# Episode 02: AI-Powered Resume Fine-Tuner with Claude Code

## 🎬 Video Script (12-15 minutes - HIGH ENERGY)

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

### 🚀 CLAUDE CODE AGENTS (1:00-2:30)
**[Screen: Claude Code interface]**

"Claude Code agents - AI assistants that follow YOUR exact instructions. In Episode 1, we built portfolios with UI agents. Now we're creating something even more powerful."

**[YouTube Card @ 1:10: "Episode 01: Portfolio Builder" - top right]**

**[Show Excalidraw: Agent Architecture Diagram]**
![[Agent workflow.excalidraw]]

"Think of it like this: You feed the agent your ENTIRE career history once. Every project, every skill, every achievement. Then it becomes your personal resume expert, instantly matching your experience to ANY job description."

**[Quick examples on screen with vocal cues]**
"Watch the transformation:
- Developers: Generic Python developer BECOMES specialized ML Engineer
- Marketers: Basic content writer TRANSFORMS INTO SEO specialist
- Project Managers: Standard PM EVOLVES INTO Agile Coach
- And hundreds more combinations..."

**[Bridge to next section]**
"But first, let's set up your workspace. This takes 30 seconds..."

---

### 🏗️ QUICK SETUP (2:30-3:30)
**[Terminal commands on screen]**

"Quick tip that'll save you hours - skip those annoying permission prompts. Add this to your shell config file:"

```bash
function claude() {
  command claude --dangerously-skip-permissions "$@"
}
source ~/.zshrc
```

**[Vocal instruction]**
"For Windows users, check the GitHub repo for PowerShell instructions."

"Now organize your workspace with three simple folders:"

```bash
mkdir -p resumes/{templates,outputs,job-descriptions}
```

**[File structure visual with explanation]**
"Templates store your base resumes. Outputs hold tailored versions. Job descriptions save what worked. Simple system, massive results."

**[Bridge with energy]**
"Now comes the magic - building your AI resume expert..."

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
![[Experience Matrix.excalidraw]]
"More detail = Better matches. Feed it everything."

---

### 🎯 LIVE DEMO (5:30-8:00)
**[Screen: Real job description from inbox]**

"Let me show you the power of this system. Here's a REAL job from my inbox this morning:"

```
Senior Full Stack Developer – Healthcare
- Python, React, PostgreSQL
- HIPAA compliance required
- 7+ years experience minimum
- Remote, $180K-220K
```

**[Terminal command with vocal explanation]**
```bash
claude "resume-fine-tuner: Healthcare Full Stack role [paste JD]"
```

**[Vocal cue for demo]**
"Watch what happens in real-time. The agent extracts keywords, matches them to my experience, and generates a targeted resume."

**[Show 3-step process visualization with narration]**
"Step 1: EXTRACT - The agent identifies Python, React, Healthcare, HIPAA as critical keywords
Step 2: MATCH - It searches my experience database for relevant projects
Step 3: GENERATE - Creates a perfectly tailored resume emphasizing healthcare experience"

**[Split screen comparison with vocal emphasis]**
"Look at the difference. The generic resume says 'Python developer with 10 years experience.'
The tailored one says 'Healthcare-focused full stack engineer with HIPAA-compliant system expertise.'

Which one gets the interview? Exactly."

**[Show actual metrics]**
"Processing time: 30 seconds. Response rate improvement: From 15 percent TO 45 percent. That's triple the interviews."

**[YouTube Card @ 7:30: "See Complete Agent Setup" - links to GitHub]**

**[Examples for other industries with vocal transitions]**
"And this works for ANY role:
- Marketing Manager BECOMES Growth Marketing Lead
- Project Manager TRANSFORMS INTO Agile Coach
- Data Analyst EVOLVES INTO Business Intelligence Expert
- Sales Rep BECOMES Enterprise Account Executive"

**[Bridge to next section]**
"Want to maximize your results? Here are the pro strategies..."

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