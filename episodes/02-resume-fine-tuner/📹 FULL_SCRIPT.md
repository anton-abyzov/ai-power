# Episode 02: AI-Powered Resume Fine-Tuner with Claude Code

## 🎬 Video Script (10-15 minutes)

---

### 🔥 HOOK (0:00-0:30)
**[Scene: Screen recording showing inbox with multiple job offers]**

"Getting 50+ recruiter messages a week? Backend today, frontend tomorrow, cloud architect next week? I'll show you how I use Claude Code to instantly tailor my resume for each opportunity - turning a 2-hour task into 2 minutes. And yes, this actually helped me land multiple 6-figure remote offers."

**[Quick montage: Show different job descriptions - Senior .NET Developer, Cloud Architect, ML Engineer]**

"Different roles need different resumes. Let me show you the AI-powered system I built that adapts my 18 years of experience to ANY job description."

---

### 📊 THE PROBLEM (0:30-1:30)
**[Screen: Show typical developer's broad experience - multiple languages, clouds, frameworks]**

"Here's the reality for experienced developers:"

**[Show Excalidraw diagram: Broad Experience vs Focused JDs]**

"You've worked with everything - C#, Python, JavaScript, Azure, AWS, Kubernetes... But that Senior .NET position? They want .NET expertise front and center. That ML role? They need to see your Python and TensorFlow first."

**[Show inbox with recruiter messages]**

"When you're getting dozens of opportunities, manually tailoring each resume is impossible. Too broad? You look unfocused. Too narrow? You miss opportunities."

**[Transition slide: "The Solution: AI-Powered Resume Fine-Tuning"]**

---

### 🚀 INTRODUCING CLAUDE CODE AGENTS (1:30-3:00)
**[Screen: Navigate to Claude Code docs]**

"In my previous episode, I showed how to create UI/UX agents for building portfolios. Today, we're taking it further - creating a resume fine-tuning agent that understands YOUR specific career."

**[Show Excalidraw: Agent Architecture Diagram]**

"Claude Code agents are custom AI assistants that follow your specific instructions. Think of them as specialized team members who know exactly how to present your experience."

**[Quick reference to previous video with overlay pointing to Episode 01]**

"If you haven't seen how we set up Obsidian and Claude Code, check out Episode 1 - link in the description."

---

### 🏗️ SETTING UP THE WORKSPACE (3:00-4:00)
**[Screen recording: Terminal and file system]**

"First, let's organize our resume workspace:"

```bash
cd ~/Documents
mkdir -p resumes/{templates,outputs,job-descriptions}
```

**[Show file structure in VS Code or Obsidian]**

"We'll keep:
- Templates: Your base resume formats
- Outputs: Tailored versions for each application
- Job Descriptions: Save these for reference"

**[Important note on screen]**
"Quick note: We're using markdown for easy editing, but you can export to PDF, Word, or even LaTeX later."

---

### 🤖 CREATING THE RESUME AGENT (4:00-6:30)
**[Screen: Open Claude Code configuration]**

"Now for the magic - let's create our resume fine-tuner agent:"

**[Type out the agent configuration, highlighting key sections]**

```yaml
name: resume-fine-tuner
description: Tailors resumes to specific job descriptions
tools: Read, Write, Grep, Glob
```

**[Excalidraw: Show agent workflow - Input JD → Extract Keywords → Match Experience → Generate Output]**

"The agent needs to:
1. Extract key requirements from the job description
2. Map them to your experience
3. Reorganize and emphasize relevant skills
4. Maintain authenticity - no fake experience"

**[Show the comprehensive experience database being added]**

"Here's the critical part - feed it ALL your experience upfront:"

```yaml
experience:
  - company: Carnival Corporation
    period: 2023-Present
    technologies: [Azure, .NET 8, Kafka, Kubernetes]
    achievements:
      - Built loyalty platform for 20M+ passengers
      - Reduced latency by 25% through optimization
  # ... more entries
```

**[Important callout]**
"Notice how I keep metrics modest and realistic? 25% improvement is believable. 10x performance? That screams AI-generated."

---

### 📝 DEFINING YOUR EXPERIENCE (6:30-8:00)
**[Screen: Show sample experience file structure]**

"The key is organizing your experience by:
- Technologies used
- Quantifiable achievements
- Specific modules built
- Team sizes and scope"

**[Show Excalidraw: Experience Mapping Matrix]**

"Think of it as a database of your career that the AI can query:"

```markdown
## Project: Healthcare Data Platform
- **Company**: Olympus Corporation
- **Tech Stack**: FHIR, HL7, Azure Functions, .NET Core
- **Achievements**:
  - Processed 10M+ medical events daily
  - HIPAA compliant architecture
  - 95% accuracy in ML models
```

**[Pro tip overlay]**
"Pro tip: Include project codenames, specific integrations, and realistic metrics. These details make your resume stand out as authentic."

---

### 🎯 LIVE DEMO: TAILORING A RESUME (8:00-11:00)
**[Screen recording: Actual Claude Code usage]**

"Let's do this live. Here's a Senior .NET Developer position from Microsoft:"

**[Copy job description]**

"Watch how we invoke the agent:"

```bash
claude "Use the resume-fine-tuner agent to create a resume for this Job Description: [paste JD]"
```

**[Show Claude Code processing]**

"See how it:
- Identifies key requirements: .NET 8, microservices, Azure
- Pulls relevant experience: Carnival, MUFG Bank projects
- Reorganizes bullets to lead with .NET achievements
- Maintains natural language - not robotic"

**[Show the generated resume]**

"In 30 seconds, we have a perfectly tailored resume. But here's the important part..."

**[Highlight natural elements]**

"Look at the language variety:
- 'Worked on' instead of always 'Led'
- Mix of metrics: 25%, roughly 30%, ~10ms
- Some bullets without metrics - keeping it real"

---

### 💡 ADVANCED TECHNIQUES (11:00-12:30)
**[Screen: Show filename organization]**

"Smart file naming for tracking:"
```
experience_microsoft_senior_dotnet_john_2024-01.md
experience_google_ml_engineer_sarah_2024-01.md
```

**[Show Excalidraw: Multiple Resume Versions Strategy]**

"Create variants for different focus areas:
- Backend-heavy version
- Cloud architecture focus
- Leadership emphasis
- Startup vs Enterprise"

**[Quick tip overlay]**
"Save successful applications! When similar roles come up, you can reuse proven resumes."

---

### 🎨 FORMAT OPTIONS (12:30-13:30)
**[Screen: Show different output formats]**

"The agent outputs markdown, but you can easily convert:"

**[Quick demo of each]**
- **PDF**: Use Pandoc or markdown-pdf
- **Word**: Direct export from most editors
- **LaTeX**: For that academic/technical look (great for research roles)
- **Web**: Host on GitHub Pages for a living resume

**[Show Overleaf.com briefly]**
"For LaTeX fans, Overleaf gives you beautiful, ATS-friendly PDFs."

---

### 📈 RESULTS & BEST PRACTICES (13:30-14:30)
**[Screen: Show success metrics]**

"Using this system:
- Response rate increased from 15% to 45%
- Interview requests within 24 hours
- Multiple competing offers for negotiation"

**[Excalidraw: Do's and Don'ts diagram]**

**DO's:**
✅ Keep metrics realistic (15-30% improvements)
✅ Mix technical and soft achievements
✅ Update agent with new projects regularly
✅ Save job descriptions for pattern analysis

**DON'Ts:**
❌ Claim 10x improvements everywhere
❌ Add skills you don't have
❌ Use identical language for every bullet
❌ Forget to proofread the output

---

### 🎬 CLOSING & CALL TO ACTION (14:30-15:00)
**[Screen: Back to terminal with agent running]**

"You now have an AI assistant that knows your entire career and can instantly optimize it for any opportunity. No more generic resumes. No more missed opportunities."

**[Show the GitHub repo]**

"I've put the complete agent configuration, sample resumes, and setup guide in the GitHub repo - link below. Star it if this helps!"

**[Final screen with links]**

"Next episode: Building an AI code reviewer that catches bugs before production. Subscribe and hit the bell - you don't want to miss this one."

**[End screen elements]**
- Subscribe button
- Episode 01 thumbnail (Portfolio Builder)
- GitHub repo link
- Discord community link

---

## 🎥 Production Notes

### Required Screen Recordings:
1. Inbox with recruiter messages
2. Claude Code agent creation
3. Live resume generation demo
4. File organization system
5. Multiple output formats

### Excalidraw Diagrams Needed:
1. Broad Experience vs Focused JDs
2. Agent Architecture Workflow
3. Experience Mapping Matrix
4. Multiple Resume Versions Strategy
5. Do's and Don'ts Checklist

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
- **Total Duration**: 14-15 minutes
- **Editing Time**: 4-6 hours
- **Recording Time**: 2-3 hours (multiple takes)
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