# All Claude Prompts - Episode 02

> Every prompt used in the video, ready to copy-paste

---

## 📋 AGENT CREATION

### Prompt: Create Resume Fine-Tuner Agent

**When:** Section "Create Your Agent" (4:30-5:30)

**File:** `resume-fine-tuner-agent.md`

**Paste this:**
```markdown
# Resume Fine-Tuner Agent

## Description
Expert at tailoring resumes to match job descriptions while maintaining authenticity and professionalism.

## Model
claude-sonnet-4-5-20250929

## Tools
- Read: Analyze job descriptions and existing resumes
- Write: Create tailored resume versions
- Grep: Search for specific skills and experiences
- Glob: Find relevant experience files

## Instructions

You are an expert resume writer specializing in ATS-optimized, keyword-matched resumes.

### Your Task:
1. READ the job description carefully
2. EXTRACT key requirements, technologies, and skills
3. SEARCH the experience database for matching achievements
4. WRITE a tailored resume emphasizing relevant experience
5. ENSURE all claims are backed by real experience

### Critical Rules:
- NEVER fabricate experience
- Use realistic metrics (25% improvement, not "10x")
- Vary language naturally (built, developed, worked on)
- Maintain professional tone
- Optimize for ATS parsing
```

---

## 🔍 DEMO: JOB ANALYSIS

### Prompt: Analyze Job Description

**When:** "Why Claude Sonnet 4.5" section (0:45-3:00)

**Paste this in Claude Code:**
```
Analyze this job description and identify:
1. Top 10 keywords to emphasize
2. Required vs. nice-to-have skills
3. Specific technologies mentioned
4. Experience level expectations

Job Description:
Senior Software Engineer - Cloud Platform
- 7+ years backend development
- Kubernetes, AWS, microservices
- Python or Go experience
- Team leadership skills
```

---

## 👨‍💻 DEMO 1: SOFTWARE ENGINEER

### Prompt: Create Software Engineer Resume

**When:** Demo 1 (7:30-9:30)

**Paste this in Claude Code:**
```
@resume-fine-tuner

Create a tailored resume for this Senior Backend Engineer position:

[Paste full job description here]

Use experience from experience-software-engineer.md

Output as Word document: outputs/backend-engineer-python-2025-01-15.docx

Emphasize:
- Python and FastAPI experience
- Microservices architecture
- AWS cloud experience
- Team leadership
- Performance optimization
```

---

## 📊 DEMO 2: MARKETING MANAGER

### Prompt: Create Marketing Manager Resume

**When:** Demo 2 (7:30-9:30)

**Paste this in Claude Code:**
```
@resume-fine-tuner

Create tailored resume for this Senior Marketing Manager position:

[Paste full job description here]

Use experience from experience-marketing-manager.md

Output: outputs/marketing-manager-saas-2025-01-15.docx

Emphasize:
- SEO and organic growth experience
- Content marketing strategy
- Analytics and data-driven decisions
- Team leadership
- SaaS experience
```

---

## 🏠 DEMO 3: REAL ESTATE AGENT

### Prompt: Create Real Estate Agent Resume

**When:** Demo 3 (9:30-11:30)

**Paste this in Claude Code:**
```
@resume-fine-tuner

Create tailored resume for this Senior Real Estate Agent position:

[Paste full job description here]

Use experience from experience-real-estate-agent.md

Output: outputs/real-estate-luxury-agent-2025-01-15.docx

Emphasize:
- Luxury market experience
- Sales volume and transaction count
- CRS and ABR certifications
- Client satisfaction ratings
- Marketing expertise
```

---

## 🔧 CUSTOMIZATION PROMPTS

### Modify for Different Output Formats

**For PDF output:**
```
@resume-fine-tuner

[Same as above, but add:]

Output as Markdown format: outputs/resume.md

Then I'll convert to PDF using:
pandoc resume.md -o resume.pdf
```

**For HTML web version:**
```
@resume-fine-tuner

[Same as above, but add:]

Output as HTML with clean styling: outputs/resume.html
Include inline CSS for professional appearance
```

**For LaTeX/Academic:**
```
@resume-fine-tuner

[Same as above, but add:]

Output in LaTeX format suitable for Overleaf
Use professional academic CV template structure
Include publications and research sections
```

---

## 🎯 ADVANCED PROMPTS

### Analyze Multiple Jobs at Once

```
@resume-fine-tuner

I have 3 different job descriptions below. For each one:
1. Identify key keywords
2. Recommend which parts of my experience to emphasize
3. Suggest a tailored summary statement

Job 1: [paste]
Job 2: [paste]
Job 3: [paste]

Use: experience-software-engineer.md
```

### Create Cover Letter

```
@resume-fine-tuner

Based on this job description and my experience database,
create a compelling cover letter (250-300 words).

Job Description:
[paste]

Use: experience-software-engineer.md

Tone: Professional but personable
Focus: Why I'm specifically interested in THIS role
Include: Specific achievements that match their needs
```

### Update Experience Database

```
@resume-fine-tuner

Review my experience database and suggest:
1. Metrics that could be quantified better
2. Missing keywords for my target roles
3. Achievements that should be highlighted more
4. Skills to add based on current market trends

Experience file: experience-software-engineer.md
Target roles: Senior Backend Engineer, Staff Engineer
```

---

## 🏷️ TIPS FOR WRITING EFFECTIVE PROMPTS

### DO:
✅ Be specific about file names and paths
✅ List exact requirements to emphasize
✅ Specify output format (.docx, .pdf, .md)
✅ Include realistic context (job description, company)
✅ Request specific sections (summary, skills, etc.)

### DON'T:
❌ Be vague ("make it better")
❌ Ask to fabricate experience
❌ Request unrealistic metrics
❌ Skip the experience database reference
❌ Forget to specify output location

---

## 📚 PROMPT TEMPLATES BY INDUSTRY

### Tech/Software Engineering
```
@resume-fine-tuner

Create tailored resume for [POSITION] at [COMPANY]:

[Job description]

Use: experience-software-engineer.md
Output: outputs/[company]-[role]-2025-01-15.docx

Emphasize:
- [Primary technology stack]
- [Architecture/methodology]
- [Scale/performance metrics]
- [Team leadership if applicable]
- [Domain knowledge if relevant]
```

### Marketing/Growth
```
@resume-fine-tuner

Create tailored resume for [POSITION] at [COMPANY]:

[Job description]

Use: experience-marketing-manager.md
Output: outputs/[company]-[role]-2025-01-15.docx

Emphasize:
- [Channel expertise - SEO, paid, content, etc.]
- [Growth metrics and KPIs]
- [Industry experience - B2B, B2C, SaaS, etc.]
- [Team/budget management]
- [Tools and platforms]
```

### Real Estate
```
@resume-fine-tuner

Create tailored resume for [POSITION] at [BROKERAGE]:

[Job description]

Use: experience-real-estate-agent.md
Output: outputs/[brokerage]-[specialty]-2025-01-15.docx

Emphasize:
- [Market specialization - luxury, commercial, etc.]
- [Sales volume and transaction counts]
- [Certifications - CRS, ABR, etc.]
- [Client satisfaction ratings]
- [Marketing and technology skills]
```

---

## 🚀 QUICK REFERENCE

**Basic resume generation:**
```
@resume-fine-tuner

Job: [paste description]
Experience: [file name]
Output: outputs/[filename].docx
```

**With specific emphasis:**
```
@resume-fine-tuner

Job: [paste]
Experience: [file]
Output: [filename]
Emphasize: [keyword 1], [keyword 2], [keyword 3]
```

**Multiple formats:**
```
@resume-fine-tuner

Job: [paste]
Experience: [file]
Outputs:
- outputs/resume.docx (Word)
- outputs/resume.md (Markdown for PDF conversion)
- outputs/resume.html (Web version)
```

---

**COPY, PASTE, CUSTOMIZE, GENERATE! 🎯**