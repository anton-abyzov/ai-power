# Resume Fine-Tuner Workspace

## Quick Start

1. **Open this folder in VS Code:** `code episodes/02-resume-fine-tuner/workspace`
2. **Open integrated terminal** (Cmd+` or Ctrl+`)
3. **Start Claude Code:** `claude`
4. **Use the agent:** `@resume-fine-tuner`

## Folder Structure

```
workspace/
├── resume-fine-tuner.md      # Agent configuration
├── experience-db/             # Your experience databases
│   ├── software-engineer.md
│   ├── marketing-manager.md
│   └── real-estate-agent.md
├── job-descriptions/          # Save job postings here
│   └── senior-backend-engineer-sample.md
├── outputs/                   # Generated resumes
└── templates/                 # Base resume templates
```

## How to Use

### 1. Choose Your Experience Database

Pick the one that matches your profession:
- `experience-db/software-engineer.md`
- `experience-db/marketing-manager.md`
- `experience-db/real-estate-agent.md`

**Or create your own** following the same structure!

### 2. Find a Real Job

Go to LinkedIn and find a job you want to apply for. Copy the full job description.

### 3. Run the Agent

**Two ways to call the agent:**
- `@resume-fine-tuner` (with @ symbol)
- `resume-fine-tuner` (just the name)

In Claude Code terminal:

```bash
@resume-fine-tuner

Create a tailored resume for this [Job Title] position at [Company]:

[Paste full job description here]

Use experience database: experience-db/software-engineer.md

Output file: outputs/resume-company-role-2025-10-01.md

Emphasize:
- [Key skill 1]
- [Key skill 2]
- [Key skill 3]

Ensure 90%+ keyword match while maintaining authenticity.
```

### 4. Review Generated Resume

Open the file in `outputs/` folder and review the tailored resume.

### 5. Convert to Your Preferred Format

**Option 1: Keep as Markdown (Simplest)**
- Clean, ATS-friendly, ready to paste
- No extra tools needed

**Option 2: Convert to LaTeX PDF (Optional - For Beautiful Output)**
- Copy content to Overleaf
- Use template from `../samples/example-latex-resume.tex`
- Compile to beautiful PDF
- **Note:** LaTeX is NOT required! Plain text works great.

**Option 3: Convert to Word**
```bash
pandoc outputs/resume-output.md -o outputs/resume-output.docx
```

**Option 4: Convert to PDF**
```bash
pandoc outputs/resume-output.md -o outputs/resume-output.pdf
```

## Example Demo Prompt

```
@resume-fine-tuner

Create a tailored resume for this Senior Backend Engineer position:

[Copy from job-descriptions/senior-backend-engineer-sample.md]

Use experience database: experience-db/software-engineer.md

Output file: outputs/senior-backend-engineer-techscale-2025-10-01.md

Emphasize:
- Python and FastAPI expertise
- Kubernetes and AWS cloud experience
- Microservices architecture
- Performance optimization
- Team leadership and mentoring

Ensure 90%+ keyword match while maintaining authenticity.
```

## Tips for Best Results

### 1. Customize Your Experience Database
Replace the sample data with YOUR actual experience. The more detailed, the better the output.

### 2. Be Specific in Your Prompt
Tell the agent exactly what to emphasize based on the job requirements.

### 3. Iterate
After generating, you can ask Claude to refine:
- "Make the summary more concise"
- "Add more metrics to the first project"
- "Emphasize leadership throughout"

### 4. Use Real Jobs
For best results, use actual job postings from LinkedIn, not generic descriptions.

## What the Agent Does

1. **Reads** the job description thoroughly
2. **Extracts** key requirements, technologies, soft skills
3. **Searches** your experience database for matches
4. **Prioritizes** most relevant experiences
5. **Writes** tailored resume emphasizing job-specific wins
6. **Optimizes** for ATS keywords without keyword stuffing

## Quality Standards

The agent ensures:
- ✅ 90%+ keyword match with job description
- ✅ Every bullet starts with strong action verb
- ✅ Every achievement includes metrics
- ✅ No buzzwords without substance
- ✅ Professional ATS-compatible formatting

## Why Claude Sonnet 4.5?

- **77.2% SWE-bench score** - Best coding model available
- **Better instruction following** - Less hallucination
- **Superior keyword matching** - Contextual understanding
- **Smoother workflow** - Consistent, reliable results

## Troubleshooting

### Agent not found?
Make sure you're in the `workspace/` directory when you start Claude Code.

### Generated resume too generic?
- Add more detail to your experience database
- Be more specific in your prompt about what to emphasize

### Want different format?
Use Pandoc to convert markdown to any format you need.

## Next Steps

1. Customize your experience database with YOUR real experience
2. Find real jobs on LinkedIn to apply for
3. Generate tailored resumes in 2 minutes
4. Apply with confidence!

---

**Questions?** Check the main Episode 02 documentation or open an issue on GitHub.

**Ready to record the demo?** See `../📹 THE_FULL_SCRIPT.md` for the complete video script.
