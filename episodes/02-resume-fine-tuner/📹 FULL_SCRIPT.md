# Episode 02: AI-Powered Resume Fine-Tuner with Claude Code

> 📹 **PRODUCTION NOTE**: For detailed video creation instructions, see:
> - `_production/VIDEO_GENERATION_GUIDE.md` - How to create each visual effect
> - `_production/production-notes/` - Recording and editing guides
> - Links marked with 📹 point to specific production instructions

## 🎬 Video Script (12-15 minutes - HIGH ENERGY)

---

### 🔥 HOOK (0:00-0:30)
**[Scene: Split screen - One developer manually editing resumes, another using AI]**
*📹 [See VIDEO_GENERATION_GUIDE.md → Split-Screen Recording section for OBS setup]*

"You won't be replaced by AI. But you WILL be replaced by someone using AI to do YOUR job faster and better."

**[Screen: Inbox flooding with 50+ recruiter messages]**

"Watch how to turn ANY resume into the PERFECT match for ANY job - in 2 minutes. Works for developers, marketers, project managers, real estate agents, teachers, consultants, designers - literally ANY professional."

**[Quick montage: Different resumes transforming - Software Engineer → .NET Expert, Marketing Manager → Growth Hacker, PM → Agile Coach, Real Estate Agent → Luxury Specialist, Teacher → EdTech Consultant]**
*📹 [See VIDEO_GENERATION_GUIDE.md for Veo3 prompts and creation details]*

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
- Real Estate Agents: General agent BECOMES Luxury Property Specialist
- Teachers: Classroom teacher TRANSFORMS INTO EdTech Consultant
- Designers: Graphic designer EVOLVES INTO UX Architect
- Sales Reps: Basic sales BECOMES Enterprise Account Executive
- And hundreds more combinations..."

**[Bridge to next section]**
"But first, let's set up your workspace. This takes 30 seconds..."

---

### 🏗️ QUICK SETUP (2:30-3:30)
**[Screen: Show IDE options]**
*📹 [See VIDEO_GENERATION_GUIDE.md → Quick Setup Section Fix for recording details]*

"First, let's talk tools. You can use any IDE - VS Code, Cursor, WebStorm, any JetBrains product. I prefer VS Code - it's free and powerful."

**[Show download process]**
"Download VS Code from code.visualstudio.com. Works on Mac, Windows, and Linux."

**[Reference to Episode 01]**
"In Episode 01, I showed how to install Claude Code and set up this permissions bypass. Quick recap for new viewers:"

**[Terminal commands on screen]**
"For Mac/Linux users - add this to your .zshrc or .bashrc file:"

```bash
function claude() {
  command claude --dangerously-skip-permissions "$@"
}
source ~/.zshrc
```

**[Show Windows PowerShell]**
"Windows users - add this to your PowerShell profile:"

```powershell
function claude {
    & claude --dangerously-skip-permissions $args
}
```

**[Vocal instruction]**
"This saves hours by skipping permission prompts during development."

"Now organize your workspace with three simple folders:"

```bash
mkdir -p resumes/{templates,outputs,job-descriptions}
```

**[File structure visual with explanation]**
"Templates store your base resumes. Outputs hold tailored versions. Job descriptions save what worked. Simple system, massive results."

**[Bridge with energy]**
"Now comes the magic - building your AI resume expert..."

---

### 🤖 CREATE YOUR AGENT (3:30-5:30)
**[Screen: Agent configuration file]**

"Creating your agent takes just minutes. Here's the exact process:"

**[Type out configuration with vocal guidance]**
```yaml
name: resume-fine-tuner
description: Tailors resumes to job descriptions
tools: Read, Write, Grep, Glob
```

"This tells Claude Code what tools your agent can use. Read for analyzing job descriptions, Write for creating resumes, Grep and Glob for searching your experience."

**[Show experience database structure]**
"Now the critical part - feeding it your ENTIRE career. Watch how I structure this:"

```yaml
experience:
  # For Developers:
  - company: Tech Consultancy
    period: 2023-Present
    technologies: [Azure, .NET 8, Kafka, Kubernetes]
    achievements:
      - Built platform serving 20M+ users
      - Reduced latency by 25%
      - Led team of 8 engineers

  # For Marketers:
  - campaigns: Q4 Product Launch
    budget: $500K
    metrics: 150% ROI, 10K qualified leads
    channels: [Google Ads, Meta, LinkedIn, Email]

  # For Project Managers:
  - product: Mobile Banking Platform
    users: 500K active monthly
    team: 15 engineers, 3 designers
    methodology: Scrum, SAFe certified
```

**[Vocal explanation of structure]**
"Notice the structure? Company, period, technologies, achievements. Every detail matters. The AI uses this to match job requirements."

**[Show bad vs good metrics with vocal emphasis]**
"Critical rule for believability:
GOOD: 'Improved performance by roughly 25 percent'
BAD: 'Achieved 10x performance improvement'
GOOD: 'Managed team of 8 to 12 engineers'
BAD: 'Led massive engineering organization'

Real numbers. Real impact. Real results."

**[Bridge to next section]**
"Now let me show you how to organize this experience for maximum matching power..."

---

### 📝 YOUR EXPERIENCE DATABASE (5:30-6:30)
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

### 🎯 LIVE DEMO (6:30-8:00)
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
Step 2: MATCH - It searches your experience file - not a complex database, just a simple text file with your career history
Step 3: GENERATE - Creates a perfectly tailored resume emphasizing healthcare experience"

**[Split screen comparison with vocal emphasis]**
"Look at the difference. The generic resume says 'Python developer with 10 years experience.'
The tailored one says 'Healthcare-focused full stack engineer with HIPAA-compliant system expertise.'

Which one gets the interview? Exactly."

**[Show actual metrics]**
"Processing time: 30 seconds. Response rate improvement: From 15 percent TO 45 percent. That's triple the interviews."

**[YouTube Card @ 7:30: "See Complete Agent Setup" - links to GitHub]**

**[Examples for other industries with vocal transitions]**
*📹 [See VIDEO_GENERATION_GUIDE.md for complete transformation visuals]*
"And this works for ANY role:
- Marketing Manager BECOMES Growth Marketing Lead
- Project Manager TRANSFORMS INTO Agile Coach
- Data Analyst EVOLVES INTO Business Intelligence Expert
- Sales Rep BECOMES Enterprise Account Executive
- Real Estate Agent BECOMES Luxury Property Specialist
- Teacher BECOMES EdTech Implementation Specialist
- Nurse BECOMES Clinical Informatics Specialist
- Designer BECOMES UX Architecture Lead"

**[Bridge to next section]**
"Want to maximize your results? Here are the pro strategies..."

---

### 💡 PRO TIPS (8:00-8:30)
**[Screen: File naming system]**

"Track everything:"
```
microsoft_dotnet_2024-01.docx → Interview ✓
google_ml_2024-01.docx → Offer ✓
```

**[Show Excalidraw: Multiple Resume Versions Strategy]**
![[Version Strategy updated.excalidraw]]

"Build your arsenal:
- Technical version (for engineers)
- Leadership version (for managers)
- Startup version (move fast)
- Enterprise version (process-focused)"

"Reuse winners. Track what works."

---

### 🎨 OUTPUT FORMATS (8:30-9:00)
**[Screen: Format conversions]**

"Any format you need:"

```bash
# PDF: pandoc resume.md -o resume.pdf
# Word: Already generates .docx
# Web: Push to GitHub Pages
```

**[Show Overleaf.com briefly]**
"Pro tip: For academic or technical roles, use LaTeX templates on Overleaf. They have stunning resume templates - just export your content and paste it in. Instant professional formatting."

"ATS-friendly. Human-readable. Professional."

---

### 📈 RESULTS (9:00-10:00)
**[Screen: Success metrics animation]**

"Let me show you the real impact. These are actual results from people using this system:"

**[Show before/after metrics with vocal emphasis]**
"Response rate: From 15 percent jumps to 45 percent. That's TRIPLE.
Application time: From 2 hours down to 2 minutes. That's 60 TIMES faster.
Monthly interviews: From 5 to over 20. Four times more opportunities."

**[Excalidraw: Do's and Don'ts diagram]**
![[Excalidraw/Dos and donts.excalidraw|Dos and donts.excalidraw]]

**[Vocal walkthrough of do's and don'ts]**
"Critical rules for success:
DO use realistic metrics - say 'improved by 25 percent,' not '10x performance'
DO vary your language - mix 'built,' 'developed,' 'worked on'
DO save winning resumes - track what gets interviews

DON'T add fake skills - they'll test you
DON'T use robotic language - humans read these
DON'T send generic resumes - customization is everything"

**[Testimonial cards with real examples]**
"Real results from real users:
Software Developer: Three offers in two weeks after six months of silence
Marketing Manager: Doubled salary from 80K to 160K
Project Manager: Landed remote FAANG role after 50 rejections"

**[Bridge to opportunities]**
"But where do you find these opportunities? Let me show you the goldmines..."

---

### 🔍 FIND OPPORTUNITIES (10:00-11:00)
**[Screen: Platform logos with stats]**

"Here's where the gold is hiding:"

**[Show each platform with tips]**
"LinkedIn: Turn on 'Open to Work' privately. Result? 50 plus messages per week.
AngelList or Wellfound: Startups offering equity. Filter by 'remote' and 'well-funded.'
Dice and Indeed: Volume strategy. Set up alerts for your keywords.
Your email spam folder: No joke - real opportunities get filtered. Check weekly."

**[Security alert with real example]**
"CRITICAL WARNING: I almost got phished by a fake Microsoft recruiter site. Perfect design, convincing domain. They wanted my LinkedIn password. NEVER enter credentials outside official sites. Verify recruiter emails with the actual company."

**[Bridge to closing]**
"You now have everything. The system, the tools, the sources. What you do next determines your future..."

### 🎬 CLOSING (11:00-12:30)
**[Screen: Split view - Two developers, different paths]**

"Picture this. Two professionals. Same experience. Different approaches.

Person A: Still manually editing resumes. Two hours per application. Generic content. 15 percent response rate.

Person B: Uses Claude Code agents. Two minutes per application. Perfectly tailored. 45 percent response rate.

Six months later: Person A is still searching. Person B has multiple offers and negotiating power."

**[YouTube Card @ 11:00: "Episode 01: Build Portfolio with AI" - top right]**

**[GitHub repo with live demo]**
"Everything you need is at github.com/anton-abyzov/ai-power
The complete agent code. Setup instructions. Real examples. Totally FREE.

Plus, if you missed Episode 1 on building portfolios with AI, that's there too."

**[Final powerful message with emphasis]**
"Here's the truth: In 2024 and beyond, there are only two types of professionals.

Those who USE AI to amplify their careers.
And those who get REPLACED by the first group.

You won't be replaced by AI.
You'll be replaced by someone who knows how to use AI better than you.

The question isn't IF you should start.
It's whether you'll start TODAY, or after it's too late."

**[End screen with clear CTAs]**
- 🔴 SUBSCRIBE for more AI power techniques
- ▶️ Episode 01: Portfolio Builder with Claude Code
- 💻 GitHub: anton-abyzov/ai-power (Get the code NOW)
- 💬 Comment: Share your results

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
- **Total Duration**: 12-13 minutes (perfect for YouTube algorithm)
- **Editing Time**: 4-5 hours (dynamic cuts, transitions)
- **Recording Time**: 2-3 hours (multiple takes for energy)
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